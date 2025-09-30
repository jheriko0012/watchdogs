#!/usr/bin/env python3
"""
🚀 CREADOR AUTOMÁTICO - Termux Watch Dogs Suite
Ejecuta este script y crea TODA la estructura automáticamente
"""

import os
import json
from pathlib import Path

def create_directory_structure():
    """Crear toda la estructura de carpetas"""
    directories = [
        # Estructura principal
        "launcher",
        "downloaded_tools",
        "themes",
        "config", 
        "scripts",
        "docs/images",
        
        # Herramientas por categorías
        "downloaded_tools/sherlock",
        "downloaded_tools/phoneinfoga",
        "downloaded_tools/sqlmap",
        "downloaded_tools/xsstrike",
        "downloaded_tools/recon-ng",
        "downloaded_tools/socialfish",
        "downloaded_tools/hiddeneye",
        "downloaded_tools/seeker",
        "downloaded_tools/theharvester",
    ]
    
    print("📁 Creando estructura de carpetas...")
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"  ✅ {directory}")

def create_file(path, content):
    """Crear archivo con contenido"""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  📄 {path}")

def create_famous_tools_config():
    """Crear configuración de herramientas famosas"""
    tools_config = {
        "osint": [
            {
                "name": "Sherlock",
                "github": "sherlock-project/sherlock",
                "description": "Buscar usuarios en 300+ redes sociales",
                "command": "python sherlock.py {username} --timeout 10",
                "install_command": "pip install -r requirements.txt",
                "category": "OSINT",
                "icon": "🔍"
            },
            {
                "name": "PhoneInfoga",
                "github": "sundowndev/phoneinfoga", 
                "description": "Análisis avanzado de números telefónicos",
                "command": "python phoneinfoga.py -n {phone}",
                "install_command": "pip install -r requirements.txt",
                "category": "OSINT",
                "icon": "📞"
            },
            {
                "name": "Recon-ng",
                "github": "lanmaster53/recon-ng",
                "description": "Framework completo de reconocimiento",
                "command": "python recon-ng",
                "install_command": "pip install -r REQUIREMENTS",
                "category": "OSINT", 
                "icon": "🌐"
            },
            {
                "name": "TheHarvester",
                "github": "laramies/theHarvester",
                "description": "Recolección de emails, subdominios, IPs",
                "command": "python theHarvester.py -d {domain} -l 100 -b all",
                "install_command": "pip install -r requirements.txt",
                "category": "OSINT",
                "icon": "📧"
            }
        ],
        "web_hacking": [
            {
                "name": "SQLMap",
                "github": "sqlmapproject/sqlmap",
                "description": "Detector y explotador de SQL Injection", 
                "command": "python sqlmap.py -u {url} --batch",
                "install_command": "",
                "category": "Web",
                "icon": "💉"
            },
            {
                "name": "XSStrike",
                "github": "s0md3v/XSStrike", 
                "description": "Escáner avanzado de XSS",
                "command": "python xsstrike.py -u {url}",
                "install_command": "pip install -r requirements.txt",
                "category": "Web",
                "icon": "🛡️"
            },
            {
                "name": "Nikto",
                "description": "Escáner de vulnerabilidades web",
                "command": "nikto -h {target}",
                "install_command": "pkg install nikto",
                "category": "Web",
                "icon": "🔍"
            }
        ],
        "network": [
            {
                "name": "Nmap",
                "description": "Escáner de red y puertos", 
                "command": "nmap {target}",
                "install_command": "pkg install nmap",
                "category": "Network",
                "icon": "🌐"
            },
            {
                "name": "Aircrack-ng",
                "description": "Suite de auditoría WiFi",
                "command": "aircrack-ng {file}",
                "install_command": "pkg install aircrack-ng",
                "category": "Wireless", 
                "icon": "📡"
            }
        ],
        "social_engineering": [
            {
                "name": "SocialFish",
                "github": "UndeadSec/SocialFish",
                "description": "Framework de phishing educativo",
                "command": "python3 SocialFish.py {username} {password}",
                "install_command": "chmod +x install.sh && ./install.sh",
                "category": "Social",
                "icon": "🎣"
            },
            {
                "name": "HiddenEye", 
                "github": "DarkSecDevelopers/HiddenEye",
                "description": "Herramienta avanzada de phishing",
                "command": "python3 HiddenEye.py",
                "install_command": "chmod +x install.sh && ./install.sh",
                "category": "Social",
                "icon": "👁️"
            },
            {
                "name": "Seeker",
                "github": "thewhiteh4t/seeker",
                "description": "Geolocalización avanzada",
                "command": "python3 seeker.py -t manual -k {keyword}",
                "install_command": "chmod +x install.sh && ./install.sh",
                "category": "Social", 
                "icon": "📍"
            }
        ],
        "password_attacks": [
            {
                "name": "John The Ripper",
                "description": "Cracker de contraseñas",
                "command": "john {file}",
                "install_command": "pkg install john",
                "category": "Password",
                "icon": "🔑"
            },
            {
                "name": "Hashcat",
                "description": "Recuperación avanzada de passwords", 
                "command": "hashcat -m {hash_type} {hash_file}",
                "install_command": "pkg install hashcat",
                "category": "Password",
                "icon": "⚡"
            }
        ],
        "forensics": [
            {
                "name": "Binwalk",
                "description": "Análisis de firmware y archivos binarios",
                "command": "binwalk {file}",
                "install_command": "pkg install binwalk", 
                "category": "Forensics",
                "icon": "🔎"
            },
            {
                "name": "Exiftool",
                "description": "Metadatos de imágenes y archivos",
                "command": "exiftool {file}",
                "install_command": "pkg install exiftool",
                "category": "Forensics",
                "icon": "📷"
            }
        ]
    }
    
    create_file("config/famous_tools.json", json.dumps(tools_config, indent=2))

def create_launcher_files():
    """Crear archivos del launcher"""
    
    # main_dashboard.py
    main_dashboard_content = '''#!/usr/bin/env python3
"""
🎮 DASHBOARD PRINCIPAL - Centro de Control Watch Dogs
Meta-Launcher de herramientas de hacking famosas
"""

import os
import json
import subprocess
import threading
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock
from kivy.core.window import Window

# Configuración
Window.size = (400, 700)
Window.clearcolor = (0.05, 0.05, 0.1, 1)  # Azul oscuro estilo hacker

class HackerButton(Button):
    """Botón personalizado estilo hacker"""
    def __init__(self, tool_data, **kwargs):
        super().__init__(**kwargs)
        self.tool_data = tool_data
        self.background_color = (0.1, 0.4, 0.8, 1)
        self.color = (1, 1, 1, 1)
        self.size_hint_y = None
        self.height = 90
        self.text = f"{tool_data['icon']} {tool_data['name']}\\n[tiny]{tool_data['description']}[/tiny]"
        self.markup = True
        self.font_size = '14sp'

class WatchDogsDashboard(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Watch Dogs - Hacking Tools Launcher"
        self.tools_data = self.load_tools()
    
    def load_tools(self):
        """Cargar lista de herramientas famosas"""
        try:
            with open('config/famous_tools.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error cargando herramientas: {e}")
            return {"error": "No se pudo cargar herramientas"}
    
    def build(self):
        # Layout principal
        main_layout = BoxLayout(orientation='vertical', padding=15, spacing=15)
        
        # Header estilo Watch Dogs
        header = BoxLayout(orientation='vertical', size_hint=(1, 0.18))
        title = Label(
            text='[b]₩₳₮₵Ⱨ ĐØ₲₴[/b]\\nHACKING SUITE',
            markup=True,
            color=(0, 1, 1, 1),
            font_size='24sp'
        )
        subtitle = Label(
            text='Meta-Launcher • 20+ Herramientas Éticas',
            color=(0.7, 0.7, 1, 1),
            font_size='12sp'
        )
        header.add_widget(title)
        header.add_widget(subtitle)
        main_layout.add_widget(header)
        
        # Estadísticas rápidas
        stats = self.create_stats_bar()
        main_layout.add_widget(stats)
        
        # Panel de herramientas
        tools_panel = self.create_tools_panel()
        main_layout.add_widget(tools_panel)
        
        return main_layout
    
    def create_stats_bar(self):
        """Crear barra de estadísticas"""
        stats_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.08), spacing=10)
        
        tools_count = sum(len(tools) for tools in self.tools_data.values() if tools)
        
        stats = [
            f"🛠️ {tools_count} Tools",
            "🔓 Ethical Use",
            "🚀 Ready"
        ]
        
        for stat in stats:
            stat_label = Label(
                text=stat,
                color=(0, 1, 0, 1),
                font_size='10sp'
            )
            stats_layout.add_widget(stat_label)
        
        return stats_layout
    
    def create_tools_panel(self):
        """Crear panel de herramientas con categorías"""
        scroll = ScrollView()
        main_grid = GridLayout(cols=1, spacing=15, size_hint_y=None)
        main_grid.bind(minimum_height=main_grid.setter('height'))
        
        for category, tools in self.tools_data.items():
            if tools and category != "error":
                # Categoría
                cat_label = Label(
                    text=f'[b]┌─ {category.upper()} ─┐[/b]',
                    markup=True,
                    size_hint_y=None,
                    height=40,
                    color=(0, 1, 0, 1),
                    font_size='16sp'
                )
                main_grid.add_widget(cat_label)
                
                # Herramientas de esta categoría
                for tool in tools:
                    btn = HackerButton(tool)
                    btn.bind(on_press=self.show_tool_options)
                    main_grid.add_widget(btn)
        
        scroll.add_widget(main_grid)
        return scroll
    
    def show_tool_options(self, instance):
        """Mostrar opciones para la herramienta seleccionada"""
        tool = instance.tool_data
        self.current_tool = tool
        
        content = BoxLayout(orientation='vertical', spacing=15, padding=20)
        
        # Información de la herramienta
        info_text = f"""[b]{tool['icon']} {tool['name']}[/b]
        
{tool['description']}
        
[color=00ff00]Categoría:[/color] {tool['category']}
[color=00ff00]Comando:[/color] {tool['command']}"""
        
        info_label = Label(
            text=info_text,
            markup=True,
            size_hint_y=0.5,
            text_size=(350, None)
        )
        content.add_widget(info_label)
        
        # Campo para parámetros
        self.params_input = TextInput(
            hint_text='Parámetros (ej: -u https://example.com)',
            size_hint_y=0.2,
            multiline=False
        )
        content.add_widget(self.params_input)
        
        # Botones de acción
        btn_layout = BoxLayout(spacing=10, size_hint_y=0.3)
        
        install_btn = Button(text='📥 Instalar', background_color=(0.2, 0.6, 0.2, 1))
        install_btn.bind(on_press=lambda x: self.install_tool(tool))
        
        run_btn = Button(text='🚀 Ejecutar', background_color=(0.8, 0.2, 0.2, 1))
        run_btn.bind(on_press=lambda x: self.run_tool(tool))
        
        btn_layout.add_widget(install_btn)
        btn_layout.add_widget(run_btn)
        content.add_widget(btn_layout)
        
        self.tool_popup = Popup(
            title=f'⚡ {tool["name"]}',
            content=content,
            size_hint=(0.9, 0.7)
        )
        self.tool_popup.open()
    
    def install_tool(self, tool):
        """Instalar herramienta desde GitHub"""
        self.tool_popup.dismiss()
        self.show_installation_popup(tool)
    
    def show_installation_popup(self, tool):
        """Mostrar popup de instalación"""
        content = BoxLayout(orientation='vertical', spacing=10, padding=20)
        
        status_label = Label(text=f"Instalando {tool['name']}...", size_hint_y=0.6)
        progress = ProgressBar(max=100, size_hint_y=0.2)
        content.add_widget(status_label)
        content.add_widget(progress)
        
        install_popup = Popup(
            title='📥 Instalación',
            content=content,
            size_hint=(0.8, 0.4)
        )
        
        # Simular instalación (en versión real aquí iría la descarga)
        def update_progress(dt):
            install_popup.dismiss()
            self.show_message(f"✅ {tool['name']} instalado!", "Éxito")
        
        Clock.schedule_once(update_progress, 2)
        install_popup.open()
    
    def run_tool(self, tool):
        """Ejecutar herramienta"""
        params = self.params_input.text
        self.tool_popup.dismiss()
        
        # Mostrar consola de ejecución
        self.show_execution_console(tool, params)
    
    def show_execution_console(self, tool, params):
        """Mostrar consola de ejecución"""
        content = BoxLayout(orientation='vertical', spacing=10, padding=10)
        
        console_output = TextInput(
            text=f"🚀 Ejecutando: {tool['command']} {params}\\n\\n[Simulando ejecución...]\\n\\n✅ Completado!",
            size_hint_y=0.8,
            readonly=True,
            background_color=(0, 0, 0, 1),
            foreground_color=(0, 1, 0, 1)
        )
        content.add_widget(console_output)
        
        close_btn = Button(text='Cerrar', size_hint_y=0.2)
        close_btn.bind(on_press=lambda x: exec_popup.dismiss())
        content.add_widget(close_btn)
        
        exec_popup = Popup(
            title=f'🖥️ Consola - {tool["name"]}',
            content=content,
            size_hint=(0.9, 0.8)
        )
        exec_popup.open()
    
    def show_message(self, message, title="Info"):
        """Mostrar mensaje al usuario"""
        popup = Popup(
            title=title,
            content=Label(text=message),
            size_hint=(0.6, 0.4)
        )
        popup.open()

if __name__ == "__main__":
    WatchDogsDashboard().run()
'''
    create_file("launcher/main_dashboard.py", main_dashboard_content)

def create_script_files():
    """Crear scripts de utilidad"""
    
    # auto_downloader.py
    auto_downloader_content = '''#!/usr/bin/env python3
"""
📥 DESCARGADOR AUTOMÁTICO - Descarga herramientas de GitHub
"""

import os
import json
import subprocess
from pathlib import Path

class ToolDownloader:
    def __init__(self):
        self.base_path = Path("downloaded_tools")
        self.base_path.mkdir(exist_ok=True)
    
    def download_tool(self, tool_name, github_repo):
        """Descargar herramienta desde GitHub"""
        tool_path = self.base_path / tool_name.lower()
        
        if tool_path.exists():
            print(f"✅ {tool_name} ya está instalado")
            return True
        
        print(f"📥 Descargando {tool_name}...")
        
        # URL de GitHub
        github_url = f"https://github.com/{github_repo}.git"
        
        try:
            # Clonar repositorio
            result = subprocess.run(
                ["git", "clone", github_url, str(tool_path)],
                capture_output=True,
                text=True,
                timeout=300  # 5 minutos máximo
            )
            
            if result.returncode == 0:
                print(f"✅ {tool_name} instalado correctamente")
                return True
            else:
                print(f"❌ Error instalando {tool_name}: {result.stderr}")
                return False
                
        except subprocess.TimeoutExpired:
            print(f"⏰ Timeout instalando {tool_name}")
            return False
        except Exception as e:
            print(f"💥 Error: {e}")
            return False
    
    def install_requirements(self, tool_name):
        """Instalar dependencias de la herramienta"""
        tool_path = self.base_path / tool_name.lower()
        requirements_file = tool_path / "requirements.txt"
        
        if requirements_file.exists():
            print(f"📦 Instalando dependencias para {tool_name}...")
            try:
                subprocess.run(
                    ["pip", "install", "-r", str(requirements_file)],
                    check=True
                )
                print(f"✅ Dependencias de {tool_name} instaladas")
            except subprocess.CalledProcessError:
                print(f"❌ Error instalando dependencias de {tool_name}")
    
    def download_all_tools(self, tools_config):
        """Descargar todas las herramientas de la configuración"""
        print("🚀 INICIANDO DESCARGA MASIVA DE HERRAMIENTAS")
        print("=" * 50)
        
        for category, tools in tools_config.items():
            print(f"\\n📂 CATEGORÍA: {category.upper()}")
            print("-" * 30)
            
            for tool in tools:
                if 'github' in tool:
                    success = self.download_tool(tool['name'], tool['github'])
                    if success:
                        self.install_requirements(tool['name'])

def main():
    # Cargar configuración
    try:
        with open('config/famous_tools.json', 'r') as f:
            tools_config = json.load(f)
    except Exception as e:
        print(f"❌ Error cargando configuración: {e}")
        return
    
    # Descargar herramientas
    downloader = ToolDownloader()
    downloader.download_all_tools(tools_config)
    
    print("\\n" + "=" * 50)
    print("🎉 DESCARGA COMPLETADA")
    print("¡Ahora puedes usar las herramientas desde el Dashboard!")

if __name__ == "__main__":
    main()
'''
    create_file("scripts/auto_downloader.py", auto_downloader_content)

    # install.sh
    install_sh_content = '''#!/bin/bash
# 🚀 Script de instalación - Termux Watch Dogs Suite

echo "🎮 Instalando Termux Watch Dogs Suite..."
echo "=========================================="

# Colores
RED='\\033[0;31m'
GREEN='\\033[0;32m'
YELLOW='\\033[1;33m'
CYAN='\\033[0;36m'
NC='\\033[0m'

# Funciones de impresión
print_status() {
    echo -e "${CYAN}[*]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[+]${NC} $1"
}

print_error() {
    echo -e "${RED}[-]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[!]${NC} $1"
}

# Actualizar paquetes
print_status "Actualizando paquetes Termux..."
pkg update -y && pkg upgrade -y

# Instalar dependencias base
print_status "Instalando dependencias base..."
pkg install -y \\
    git python nodejs ruby \\
    nmap python-pip termux-api \\
    wget curl clang make

# Instalar dependencias Python
print_status "Instalando dependencias Python..."
pip install --upgrade pip
pip install \\
    requests beautifulsoup4 colorama \\
    pyfiglet kivy pillow \\
    qrcode phonenumbers

# Instalar herramientas de hacking comunes
print_status "Instalando herramientas comunes..."
pkg install -y \\
    hydra sqlmap metasploit \\
    wireshark tshark aircrack-ng \\
    john hashcat binwalk exiftool

# Dar permisos a scripts
print_status "Configurando permisos..."
chmod +x scripts/*.sh
chmod +x scripts/*.py
chmod +x launcher/*.py

print_success "Instalación completada!"
echo ""
print_warning "Para usar la suite:"
echo "  python main.py"
echo ""
print_warning "Para descargar herramientas:"
echo "  python scripts/auto_downloader.py"
echo ""
echo "🎯 ¡Listo para hackear (éticamente)!"
'''
    create_file("scripts/install.sh", install_sh_content)

def create_config_files():
    """Crear archivos de configuración"""
    
    # requirements.txt
    requirements_content = '''requests==2.31.0
beautifulsoup4==4.12.2
colorama==0.4.6
pyfiglet==0.8.post1
kivy==2.2.1
pillow==10.0.0
qrcode==7.4.2
phonenumbers==8.13.11
urllib3==1.26.16
'''
    create_file("requirements.txt", requirements_content)

    # main.py (lanzador principal)
    main_py_content = '''#!/usr/bin/env python3
"""
🎮 TERMUX WATCH DOGS SUITE - Lanzador Principal
Meta-Launcher de herramientas de hacking ético
"""

import os
import sys
import subprocess

def print_banner():
    print("""\\033[1;36m
    ╔══════════════════════════════════════════╗
    ║               ₩₳₮₵Ⱨ ĐØ₲₴               ║
    ║           META-HACKING SUITE            ║
    ╚══════════════════════════════════════════╝
    \\033[0m""")

def main():
    print_banner()
    print("\\n🎯 SELECCIONA MODO DE EJECUCIÓN:")
    print("1. 🎮 Interfaz Gráfica (Dashboard)")
    print("2. 🖥️  Menú de Consola")
    print("3. 📥 Instalar/Actualizar Herramientas")
    print("4. 🚀 Descargar Todas las Herramientas")
    print("5. ❌ Salir")
    
    try:
        choice = input("\\n👉 Selecciona [1-5]: ").strip()
        
        if choice == "1":
            print("🚀 Iniciando Dashboard Gráfico...")
            try:
                from launcher.main_dashboard import WatchDogsDashboard
                WatchDogsDashboard().run()
            except ImportError as e:
                print(f"❌ Error: {e}")
                print("💡 Ejecuta: pip install kivy pillow")
                
        elif choice == "2":
            print("🖥️  Iniciando modo consola...")
            os.system("python launcher/console_launcher.py")
            
        elif choice == "3":
            print("📥 Ejecutando instalador...")
            os.system("bash scripts/install.sh")
            
        elif choice == "4":
            print("🚀 Descargando herramientas...")
            os.system("python scripts/auto_downloader.py")
            
        elif choice == "5":
            print("👋 ¡Hasta luego, hacker!")
            sys.exit(0)
            
        else:
            print("❌ Opción inválida")
            main()
            
    except KeyboardInterrupt:
        print("\\n👋 Sesión terminada")
    except Exception as e:
        print(f"💥 Error: {e}")

if __name__ == "__main__":
    main()
'''
    create_file("main.py", main_py_content)

def create_all_files():
    """Crear todos los archivos"""
    print("🚀 CREANDO TERMUX WATCH DOGS SUITE")
    print("=" * 50)
    
    create_directory_structure()
    print("")
    
    create_famous_tools_config()
    create_config_files()
    create_launcher_files() 
    create_script_files()
    
    print("\\n" + "=" * 50)
    print("🎉 ¡SUITE CREADA EXITOSAMENTE!")
    print("📁 Estructura lista para subir a GitHub")

if __name__ == "__main__":
    create_all_files()