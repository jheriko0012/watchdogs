#!/usr/bin/env python3
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
        self.text = f"{tool_data['icon']} {tool_data['name']}\n[tiny]{tool_data['description']}[/tiny]"
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
            text='[b]₩₳₮₵Ⱨ ĐØ₲₴[/b]\nHACKING SUITE',
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
            text=f"🚀 Ejecutando: {tool['command']} {params}\n\n[Simulando ejecución...]\n\n✅ Completado!",
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
