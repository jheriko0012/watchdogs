#!/bin/bash
# 🚀 Script de instalación - Termux Watch Dogs Suite

echo "🎮 Instalando Termux Watch Dogs Suite..."
echo "=========================================="

# Colores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

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
pkg install -y \
    git python nodejs ruby \
    nmap python-pip termux-api \
    wget curl clang make

# Instalar dependencias Python
print_status "Instalando dependencias Python..."
pip install --upgrade pip
pip install \
    requests beautifulsoup4 colorama \
    pyfiglet kivy pillow \
    qrcode phonenumbers

# Instalar herramientas de hacking comunes
print_status "Instalando herramientas comunes..."
pkg install -y \
    hydra sqlmap metasploit \
    wireshark tshark aircrack-ng \
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
