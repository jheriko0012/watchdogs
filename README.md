🎮 Termux Watch Dogs Suite
Meta-Launcher de herramientas de hacking ético con interfaz gráfica estilo Watch Dogs para Termux.

https://img.shields.io/badge/Platform-Termux-green
https://img.shields.io/badge/Python-3.8+-blue
https://img.shields.io/badge/License-MIT-yellow

✨ Características
🎨 Interfaz gráfica unificada tipo Watch Dogs

🛠️ +15 herramientas famosas integradas

📱 Optimizado para Termux (Android)

🔄 Descarga automática de herramientas

🔒 Enfoque 100% ético y educativo

🚀 Instalación Rápida
bash
# 1. Clonar repositorio
git clone https://github.com/jheriko0012/watchdogs.git
cd watchdogs

# 2. Instalar dependencias
chmod +x scripts/install.sh
./scripts/install.sh

# 3. Ejecutar
python main.py
🛠️ Herramientas Incluidas
🔍 OSINT & Reconocimiento
Sherlock - Busca usuarios en 300+ redes sociales

PhoneInfoga - Analiza números telefónicos

Recon-ng - Framework completo de reconocimiento

TheHarvester - Recolecta emails y subdominios

🌐 Web Hacking
SQLMap - Detecta SQL Injection

XSStrike - Escáner avanzado de XSS

Nikto - Escáner de vulnerabilidades web

📡 Redes & Wireless
Nmap - Escáner de red y puertos

Aircrack-ng - Auditoría WiFi

🎭 Social Engineering
SocialFish - Framework de phishing educativo

HiddenEye - Herramienta de phishing avanzada

Seeker - Geolocalización avanzada

🎮 Uso
Interfaz Gráfica (Recomendado)
bash
python main.py
# Selecciona opción 1
Descargar Herramientas
bash
python main.py
# Selecciona opción 4
# O directamente:
python scripts/auto_downloader.py
Modo Consola
bash
python main.py
# Selecciona opción 2
Ejecutar Herramientas Específicas
🔍 Buscar usuario con Sherlock
bash
cd downloaded_tools/sherlock
python sherlock.py username --timeout 10
🌐 Escanear con Nmap
bash
nmap -sS 192.168.1.0/24
💉 Testear SQL Injection
bash
cd downloaded_tools/sqlmap
python sqlmap.py -u "http://example.com/page.php?id=1" --batch
📞 Analizar número con PhoneInfoga
bash
cd downloaded_tools/phoneinfoga
python phoneinfoga.py -n +1234567890
📋 Funciones Disponibles
En Interfaz Gráfica
✅ Dashboard principal con categorías

✅ Instalación 1-click de herramientas

✅ Ejecución directa desde la interfaz

✅ Parámetros personalizables

✅ Consola integrada para resultados

✅ Progress bars visuales

En Modo Consola
✅ Menú interactivo por categorías

✅ Escaneo de red automático

✅ Análisis WiFi integrado

✅ Herramientas OSINT

✅ Utilidades del sistema

⚙️ Configuración
Archivo de Configuración
json
// config/famous_tools.json
{
  "osint": [
    {
      "name": "Sherlock",
      "github": "sherlock-project/sherlock",
      "command": "python sherlock.py {username}",
      "icon": "🔍"
    }
  ]
}
Dependencias Automáticas
El script de instalación instala:

Python 3 y pip

Nmap, SQLMap, Metasploit

Kivy (para interfaz gráfica)

Requests, BeautifulSoup4

+20 paquetes esenciales

🐛 Solución de Problemas
Error: "Kivy no instalado"
bash
pip install kivy pillow
Error: "No space left"
bash
# Limpiar cache
pkg clean
# Usar almacenamiento externo
termux-setup-storage
Error: "Git clone failed"
bash
# Verificar conexión
pkg install git -y
termux-setup-storage
Error: "Python not found"
bash
pkg install python -y
📁 Estructura del Proyecto
text
watchdogs/
├── 🎮 launcher/
│   └── main_dashboard.py      # Interfaz gráfica
├── 🛠️ downloaded_tools/       # Herramientas descargadas
├── ⚙️ config/
│   └── famous_tools.json      # Configuración
├── 🔧 scripts/
│   ├── auto_downloader.py     # Descargador
│   └── install.sh            # Instalador
├── 🎨 themes/                 # Temas visuales
├── 📚 docs/                   # Documentación
├── 📄 main.py                # Lanzador
└── 📄 requirements.txt       # Dependencias
⚠️ Uso Ético
✅ Permitido
Pruebas de penetración autorizadas

Educación en ciberseguridad

Auditorías de seguridad propias

Investigación legal

🚫 Prohibido
Ataques a sistemas sin autorización

Actividades ilegales

Daño a terceros

Violación de privacidad

Este software es solo para fines educativos.

🔄 Actualizaciones
bash
# Actualizar a la última versión
cd watchdogs
git pull origin main
bash scripts/install.sh
🐛 Reportar Problemas
Si encuentras un error:

Verifica que sigues los pasos de instalación

Revisa los issues existentes en GitHub

Crea un nuevo issue con:

Descripción del problema

Comandos ejecutados

Capturas de pantalla

👨‍💻 Autor
jheriko0012 - GitHub

📄 Licencia
MIT License - Ver LICENSE para detalles.

¡Recuerda: With great power comes great responsibility! 🕷️

text
⭐ **Si te gusta el proyecto, dale una estrella en GitHub!**
🎯 Próximas Características
Más herramientas integradas

Themes personalizables

Modo oscuro/claro

Exportación de resultados

Panel de estadísticas

¿Necesitas ayuda con algo específico? ¡Abre un issue en GitHub!

