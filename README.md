# Bot de Telegram para Marca de Agua Automática 📸🤖

Proyecto creado para **automatizar el añadido de marcas de agua** a las fotos que mi madre (guía turística) comparte en sus redes. 
El bot permite:
- **Procesamiento de imagenes** mediante Telegram
- **Uso intuitivo** desde cualquier dispositivo móvil
- **Escalabilidad** para atender múltiples solicitudes simultáneas

---

## **Características Clave** ✨
- 🚀 **Integración con Telegram**: Procesamiento mediante comandos y envío directo de imágenes
- 🖼️ **Procesamiento en tiempo real**: Agrega marcas de agua a imágenes recibidas
- ⚡ **Operación asíncrona**: Manejo eficiente de múltiples solicitudes
- 🔒 **Marca de agua adaptable**: Tamaño y posición automáticos según imagen original
- 📲 **Feedback interactivo**: Notificaciones de estado durante el proceso

---

## **Tecnologías Utilizadas** 🛠️
```python
Python 3.10+
│
├── python-telegram-bot (API de Telegram)
├── Pillow (Procesamiento de imágenes)
├── logging (Sistema de registros)
└── asyncio (Manejo asíncrono)
```
---

## **Instalación y Configuración** ⚙️

### Requisitos:
- 🐍 Python 3.10 o superior
- 🤖 Token de bot de Telegram (obtenido de [@BotFather](https://t.me/BotFather))
- 🖼️ Archivo `marca.png` (marca de agua con transparencia)

### Pasos:
1. Clonar repositorio:
    ```bash
    git clone https://github.com/tu-usuario/watermark-bot.git
    cd watermark-bot
    ```

2. Instalar dependencias:

      ```bash
      pip install python-telegram-bot pillow
      ```


3. Configurar archivos:
  
    Coloca tu marca.png en la raíz del proyecto
  
    Edita bot.py con tu token:
  
      ```python
      TOKEN = "TU_TOKEN_AQUI"  # << Reemplaza esto
      WATERMARK_PATH = "marca.png"
      ```
      
      
4. Ejecutar el bot:
    
    ```bash
        python bot.py
    ```

---

## **Uso del Bot 🕹️**
    
    Ingresa a: https://t.me/[nombre_de_tu_bot]
    Usuario inicia chat con /start
    Envía cualquier imagen JPEG/PNG
    Recibe versión con marca de agua en <1 minuto
---    
## **Especificaciones técnicas:**
   
    ✅ Formatos soportados: JPG, PNG, WEBP
    📏 Tamaño máximo: 20MB
    ⚙️ Configuración automática:
        -Tamaño marca = 50% ancho imagen
        -Posición = Esquina inferior derecha
        -Margen = 20px
 
✨ ¡Listo! Tu bot estará activo y responderá a los comandos automáticamente.
⚠️ Nota: Para detener el servicio usa Ctrl + C en la termina
