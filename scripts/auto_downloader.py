#!/usr/bin/env python3
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
            print(f"\n📂 CATEGORÍA: {category.upper()}")
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
    
    print("\n" + "=" * 50)
    print("🎉 DESCARGA COMPLETADA")
    print("¡Ahora puedes usar las herramientas desde el Dashboard!")

if __name__ == "__main__":
    main()
