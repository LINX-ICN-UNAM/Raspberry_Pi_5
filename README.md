# **🚀 Raspberry Pi 5**

# 🧭 Propósito del Repositorio

Este repositorio tiene como objetivo proporcionar una **guía completa y modular** para el uso educativo y profesional de la **Raspberry Pi**, enfocándose en:

- La configuración inicial del sistema operativo y red.
- La creación de entornos Python para ejecución de scripts.
- El control de hardware mediante GPIO.
- La automatización de procesos con `systemd`.

Cada sección puede consultarse de forma independiente según las necesidades del usuario.

# 🗂️ Estructura del Repositorio

- [📂 Sección 1: Configuración básica](Seccion_1.md#-sección-1-configuración-básica)
  - [💾 Cargar Sistema Operativo en microSD](Seccion_1.md#-cargar-sistema-operativo-en-microsd)
    - [📌 Requerimientos de Hardware](Seccion_1.md#-requerimientos-de-hardware)
    - [🛠️ Instalación del Sistema Operativo](Seccion_1.md#️-instalación-del-sistema-operativo)
    - [⚙️ Ajustes de Personalización del SO](Seccion_1.md#️-ajustes-de-personalización-del-so)
  - [🔗 Conexión remota a Raspberry Pi](Seccion_1.md#-conexión-remota-a-raspberry-pi)
    - [📌 Requerimientos de Hardware](Seccion_1.md#-requerimientos-de-hardware-1)
    - [🌐 Métodos de conexión](Seccion_1.md#-métodos-de-conexión)
    - [📡 Dirección IP](Seccion_1.md#-dirección-ip)
    - [🔑 Conexión con PuTTY](Seccion_1.md#-conexión-con-putty)
    - [🖥️ Conexión con RealVNC](Seccion_1.md#️-conexión-con-realvnc)
  - [📡 Habilitar Protocolos de Comunicación](Seccion_1.md#-habilitar-protocolos-de-comunicación)
    - [📌 Requerimientos de Hardware](Seccion_1.md#-requerimientos-de-hardware-2)
    - [⚙️ Activación de protocolos](Seccion_1.md#️-activación-de-protocolos)
    - [✅ Finalización](Seccion_1.md#-finalización)
- [📂 Sección 2: Configuración Intermedia](Seccion_2.md#-sección-2-configuración-intermedia)
  - [🌐 Redes y Conexiones](Seccion_2.md#-redes-y-conexiones)
    - [🔢 IP Fija](Seccion_2.md#-ip-fija)
    - [🔌 Conexión con cable Ethernet](Seccion_2.md#-conexión-con-cable-ethernet)
    - [💻 Conexión por VSCode](Seccion_2.md#-conexión-por-vscode)
    - [📶 Hotspot](Seccion_2.md#-hotspot)
  - [📜 Scripts](Seccion_2.md#-scripts)
    - [📚 Librerías de python](Seccion_2.md#-librerías-de-python)
    - [⚙️ apt vs pip](Seccion_2.md#️-apt-vs-pip)
      - [🔧 `apt` → nivel del sistema operativo](Seccion_2.md#-apt--nivel-del-sistema-operativo)
      - [🐍 `pip` → nivel de Python](Seccion_2.md#-pip--nivel-de-python)
      - [⚠️ Recomendaciones prácticas (especialmente en Raspberry Pi)](Seccion_2.md#️-recomendaciones-prácticas-especialmente-en-raspberry-pi)
      - [🧠 En resumen](Seccion_2.md#-en-resumen)
    - [🐍 Virtual Enviroments en Python](Seccion_2.md#-virtual-enviroments-en-python)
    - [⚙️ Cargar Script](Seccion_2.md#️-cargar-script)
  - [🔧 Sensores y Hardware](Seccion_2.md#-sensores-y-hardware)
    - [🔌 Biblioteca GPIO](Seccion_2.md#-biblioteca-gpio)
    - [🌅 Script al arrancar Raspberry Pi](Seccion_2.md#-script-al-arrancar-raspberry-pi)
- [📚 Tutoriales](Tutoriales.md#-tutoriales)
  - [✋ `HelloWorld.py`](Tutoriales.md#-helloworldpy)
    - [🧰 Requerimientos del Sistema](Tutoriales.md#-requerimientos-del-sistema)
    - [📦 Dependencias Necesarias](Tutoriales.md#-dependencias-necesarias)
    - [🧪 Crear y Activar un Entorno Virtual (*Opcional*)](Tutoriales.md#-crear-y-activar-un-entorno-virtual-opcional)
    - [📁 Crear el Script `HelloWorld.py`](Tutoriales.md#-crear-el-script-helloworldpy)
    - [▶️ Ejecución del Script](Tutoriales.md#️-ejecución-del-script)
    - [🧾 Referencias](Tutoriales.md#-referencias)
  - [💡 `blink.py`](Tutoriales.md#-blinkpy)
    - [🧰 Requerimientos del Sistema](Tutoriales.md#-requerimientos-del-sistema-1)
    - [📦 Dependencias Necesarias](Tutoriales.md#-dependencias-necesarias-1)
    - [🧪 Crear y Activar un Entorno Virtual (*Opcional*)](Tutoriales.md#-crear-y-activar-un-entorno-virtual-opcional-1)
    - [📁 Crear el Script `blink.py`](Tutoriales.md#-crear-el-script-blinkpy)
    - [🛠 Conectar el Circuito](Tutoriales.md#-conectar-el-circuito)
    - [▶️ Ejecución del Script](Tutoriales.md#️-ejecución-del-script-1)
    - [🧾 Referencias](Tutoriales.md#-referencias-1)

## 🧰 Requisitos Generales

| Tipo | Elemento | Descripción |
| ------ | ----------- | ------------- |
| 💻 Hardware | Raspberry Pi 5 | Con conectividad WiFi o Ethernet |
| 🔋 Alimentación | Fuente de 5V / 3A (USB-C o microUSB según modelo) | Estable y de buena calidad |
| 💾 Almacenamiento | microSD ≥ 16 GB | Con sistema Raspberry Pi OS (Bookworm recomendado) |
| 🧠 Software base | **Sistema Operativo:** Raspberry Pi OS (64-bit) <br> **Base:** Debian GNU/Linux 12 (Bookworm) <br> **Kernel:** Linux 6.12.62+rpt-rpi-2712 <br> **Arquitectura:** ARM64 (aarch64) | Obtenido del **Raspberry Pi Imager** en *Legacy* y actualizado mediante `sudo apt update && sudo apt upgrade` |
| 🔧 Acceso remoto | SSH y/o VNC habilitados | Para control sin monitor |

> 💡 *Todos los ejemplos y scripts fueron probados en Raspberry Pi OS (Bookworm, 64-bit).*

## 🧾 Contribución

Las contribuciones son bienvenidas mediante *pull requests* o sugerencias en *issues*.

- **Responsable del proyecto**: Gustavo Medina Tanco  
- **Colaboradores**: Alfredo Rodríguez
- **Institución**: Laboratorio de Instrumentación Espacial (LINX-ICN-UNAM)

> ⚙️ Si deseas adaptar esta guía adelante.
