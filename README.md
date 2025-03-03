# Bot de Telegram para Marcado Automático de Fotos 📸🤖

Proyecto creado para **automatizar el añadido de marcas de agua** a las fotografías que mi madre (guía turística) comparte con sus clientes. El bot permite:
- **Procesamiento remoto** mediante Telegram
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
