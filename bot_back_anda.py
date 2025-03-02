import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackContext, filters
from PIL import Image
import io

# dependencias
# pip install python-telegram-bot pillow

# Configura el token de tu bot
TOKEN = "7054117313:AAHajc_CqyWnFvE3jdmN7zUQ33T4gTFZvmk"
WATERMARK_PATH = "marca.png"  # Ruta de la marca de agua

# Configuración del logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)
logger = logging.getLogger(__name__)

def add_watermark(image: Image.Image, watermark: Image.Image) -> Image.Image:
    """Añade una marca de agua a la imagen en la esquina inferior derecha con tamaño proporcional."""
    width, height = image.size
    wm_width = int(width * 0.5)  # La marca de agua será el 20% del ancho de la imagen
    wm_ratio = wm_width / watermark.width
    wm_height = int(watermark.height * wm_ratio)
    # Usar LANCZOS en lugar de ANTIALIAS para versiones recientes de Pillow
    watermark = watermark.resize((wm_width, wm_height), Image.Resampling.LANCZOS)
    
    # Posición de la marca de agua en la esquina inferior derecha
    position = (width - wm_width - 0, height - wm_height - 20)
    image.paste(watermark, position, watermark)
    return image

async def start(update: Update, context: CallbackContext) -> None:
    logger.info("Comando /start recibido")
    await update.message.reply_text("Envía una imagen y le agregaré una marca de agua.")

async def handle_photo(update: Update, context: CallbackContext) -> None:
    logger.info("Mensaje con foto recibido de %s", update.effective_user.first_name)
    try:
        await update.message.reply_text("Procesando...")
        logger.debug("Mensaje 'Procesando...' enviado")
    except Exception as e:
        logger.error("Error al enviar 'Procesando..': %s", e)
    
    try:
        photo = await update.message.photo[-1].get_file()
        logger.debug("Archivo de foto obtenido")
    except Exception as e:
        logger.error("Error al obtener el archivo de la foto: %s", e)
        return

    photo_bytes = io.BytesIO()
    try:
        await photo.download_to_memory(photo_bytes)
        logger.debug("Foto descargada en memoria")
    except Exception as e:
        logger.error("Error al descargar la foto: %s", e)
        return
    photo_bytes.seek(0)
    
    try:
        image = Image.open(photo_bytes).convert("RGBA")
        logger.debug("Imagen abierta correctamente")
    except Exception as e:
        logger.error("Error al abrir la imagen: %s", e)
        return

    try:
        watermark = Image.open(WATERMARK_PATH).convert("RGBA")
        logger.debug("Marca de agua cargada correctamente")
    except Exception as e:
        logger.error("Error al abrir la imagen de marca de agua: %s", e)
        await update.message.reply_text("Error al cargar la marca de agua.")
        return
    
    try:
        watermarked_image = add_watermark(image, watermark)
        logger.debug("Marca de agua agregada a la imagen")
    except Exception as e:
        logger.error("Error al agregar la marca de agua: %s", e)
        return
    
    output_bytes = io.BytesIO()
    try:
        watermarked_image.save(output_bytes, format="PNG")
        logger.debug("Imagen procesada guardada en buffer")
    except Exception as e:
        logger.error("Error al guardar la imagen procesada: %s", e)
        return
    
    output_bytes.seek(0)
    
    try:
        await update.message.reply_photo(photo=output_bytes)
        logger.info("Imagen procesada enviada al usuario")
    except Exception as e:
        logger.error("Error al enviar la imagen procesada: %s", e)

def main():
    logger.info("Iniciando el bot")
    application = ApplicationBuilder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    
    logger.info("Bot en modo polling")
    application.run_polling()

if __name__ == '__main__':
    main()
