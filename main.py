#!/usr/bin/env python3
"""
🎮 TERMUX WATCH DOGS SUITE - Lanzador Principal
Meta-Launcher de herramientas de hacking ético
"""

import os
import sys
import subprocess

def print_banner():
    print("""\033[1;36m
    ╔══════════════════════════════════════════╗
    ║               ₩₳₮₵Ⱨ ĐØ₲₴               ║
    ║           META-HACKING SUITE            ║
    ╚══════════════════════════════════════════╝
    \033[0m""")

def main():
    print_banner()
    print("\n🎯 SELECCIONA MODO DE EJECUCIÓN:")
    print("1. 🎮 Interfaz Gráfica (Dashboard)")
    print("2. 🖥️  Menú de Consola")
    print("3. 📥 Instalar/Actualizar Herramientas")
    print("4. 🚀 Descargar Todas las Herramientas")
    print("5. ❌ Salir")
    
    try:
        choice = input("\n👉 Selecciona [1-5]: ").strip()
        
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
        print("\n👋 Sesión terminada")
    except Exception as e:
        print(f"💥 Error: {e}")

if __name__ == "__main__":
    main()
