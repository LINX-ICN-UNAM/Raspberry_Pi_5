# 🚀 Guía de Configuración y Uso de Raspberry Pi

Este repositorio contiene una guía paso a paso para configurar y trabajar con una **Raspberry Pi**, desde la preparación del sistema operativo hasta la conexión remota y el uso de hardware adicional.  

---

## 📑 Tabla de Contenido

- [📂 Sección 1: Configuración básica](#-sección-1-configuración-básica)  
  - [1️⃣ Cargar Sistema Operativo en microSD](#1-cargar-sistema-operativo-en-microsd)  
  - [2️⃣ Conexión Remota a Raspberry Pi](#2-conexión-remota-a-raspberry-pi)  
  - [3️⃣ Habilitar Protocolos de Comunicación](#3-habilitar-protocolos-de-comunicación)
---

## 📂 Sección 1: Configuración básica

### 1. Cargar Sistema Operativo en microSD

#### 📌 Requerimientos de Hardware
- 💻 Laptop  
- 💾 microSD con su adaptador  

⚠️ Estas instrucciones funcionan en **Windows** y **Linux**. Para **MacOS** aún está pendiente de probarse.  
Asegúrate de tener la microSD conectada a la computadora antes de iniciar.  

---

#### 🛠️ Instalación del Sistema Operativo
Para cargar el sistema operativo se utilizará **Raspberry Pi Imager**, que puede descargarse desde la [página oficial](https://www.raspberrypi.com/software/).  

Este software se encargará de **formatear y grabar el Sistema Operativo (SO)** en la microSD.  

<img src="img/Raspberry%20Pi%20Imager%20v1.gif" alt="Raspberry Pi Imager"/>


En la ventana principal se deben seleccionar las siguientes opciones (con la microSD ya conectada):  

- **Dispositivo**: Raspberry Pi 5  
- **Sistema Operativo**: Raspberry Pi OS (64-Bit)  
- **Almacenamiento**: Ruta de la microSD *(se detecta automáticamente)*  

✅ Luego dar clic en **Siguiente**  
Se desplegará una ventana preguntando por la configuración personalizada del Sistema Operativo (SO). Para editarlos se selecciona *EDITAR AJUSTES* 

<img src="img/Raspberry%20Pi%20Imager%205.jpg" alt="Raspberry Pi Imager Set-Up Servicio" />

---

#### ⚙️ Ajustes de Personalización del SO
Al seleccionar esta opción se abrirá una ventana con **tres menús de configuración**:  

**1. General**
- Nombre de anfitrión: `LINX-ROBOT`  
- Usuario: `linx-robot`  
- Contraseña: `***********`  
- Configuración LAN inalámbrica:  
  - **SSID**: `NombreDeRed`  
  - **Contraseña**: `***********`  
  - Conexión automática al arrancar  
- Ajustes Regionales:  
  - Zona Horaria: `America/Mex_City`  
  - Distribución del teclado: `us` *(opcional)*  

<img src="img/Raspberry%20Pi%20Imager%206.jpg" alt="Raspberry Pi Imager Set-Up General2" width="490" height="420"/>
<img src="img/Raspberry%20Pi%20Imager%207.jpg" alt="Raspberry Pi Imager Set-Up General2" width="490" height="420"/>

**2. Servicio**
- Activar SSH  
- Usar autenticación por contraseña  

**3. Opciones**
- Reproducir sonido *(opcional)*  

<img src="img/Raspberry%20Pi%20Imager%208.jpg" alt="Raspberry Pi Imager Set-Up Servicio" width="490" height="420"/>
<img src="img/Raspberry%20Pi%20Imager%209.jpg" alt="Raspberry Pi Imager Set-Up Opciones" width="490" height="420"/>

---

🔧 Con esto la microSD queda lista para insertarse en la **Raspberry Pi** y arrancar el sistema operativo.  

<img src="img/Raspberry%20Pi%20Imager%20v2.gif" alt="Raspberry Pi Imager"/>

---

### 2. Conexión Remota a Raspberry Pi

#### 📌 Requerimientos de Hardware
- 💻 Laptop  
- 🍓 Raspberry Pi con Sistema Operativo cargado en microSD  
- 🔌 Cargador Raspberry Pi  
- 🖱️ Periféricos (opcional, recomendado para la primera configuración):  
  - Cable micro HDMI → HDMI  
  - Ratón USB Tipo A  
  - Teclado USB Tipo A  

---

#### 🌐 Métodos de conexión remota
Existen dos formas principales de conectarse a la Raspberry Pi:  

1. **PuTTY** → Permite conectarse remotamente a la **consola** de Raspberry Pi.  
2. **RealVNC** → Permite ver y controlar el **entorno gráfico** de Raspberry Pi, desplegando una ventana que funciona como monitor virtual.  

📷 *Espacio para imagen de PuTTY y RealVNC*  

---

#### 📡 Obtención de la dirección IP
Para poder conectarse de manera remota es necesario conocer la **dirección IP** de la Raspberry Pi.  

1. Conectar la Raspberry Pi a un monitor usando el cable **micro HDMI – HDMI**.  
2. Abrir la terminal local y ejecutar:  

```bash
ifconfig
```
La IP estará en la sección **wlan0**, ejemplo:  

```bash
wlan0: inet 10.200.1.227
```
⚠️ **Nota**:  
- Esta IP puede cambiar en cada reinicio, aunque es posible configurar una **IP fija**.  
- Si deseas conocer la IP de manera remota, deberás estar en la misma red WiFi, lo cual puede ser difícil si hay varios dispositivos conectados.  

📷 *Espacio para captura de pantalla de ifconfig*  

---

#### 🔑 Conexión con PuTTY
1. Abrir **PuTTY**.  
2. En el campo **Hostname (IP address)** ingresar la dirección IP de la Raspberry Pi.  
3. En **Connection type**, seleccionar **SSH**.  
4. Dejar las demás configuraciones por defecto y hacer clic en **Open**.  
5. En la consola que aparece:  
   - **Login as**: `linx-robot`  
   - **Password**: `***********`  

✅ Ahora se tiene acceso a la **Terminal de Raspberry Pi** desde la PC.  

📷 *Espacio para imagen de conexión con PuTTY*  

---

#### 🖥️ Conexión con RealVNC
Para poder conectarse con **RealVNC**, primero es necesario habilitar el servidor VNC en la Raspberry Pi.  

1. Acceder a la terminal localmente o mediante PuTTY.  
2. Ejecutar:  

```bash
sudo raspi-config
```
3. Entrar al menú de configuración y seleccionar:  
   - **Interface Options → VNC → Enable**  

📷 *Espacio para imagen de habilitación de VNC en raspi-config*  

4. Abrir **RealVNC Viewer** en la PC:  
   - En la barra de búsqueda ingresar la **IP de la Raspberry Pi**.  
   - Ingresar **usuario** y **contraseña**.  

📷 *Espacio para imagen de conexión en RealVNC Viewer*  

---

⚡ Con esta configuración básica ya es posible conectarse de manera **remota** a la Raspberry Pi usando:  
- **Terminal (SSH con PuTTY)**  
- **Entorno gráfico (VNC con RealVNC)**  

### 3. Habilitar Protocolos de Comunicación

#### 📌 Requerimientos de Hardware
- 💻 Laptop  
- 🍓 Raspberry Pi conectada a la corriente  

**Periféricos opcionales** (para conexión local):  
- Cable micro HDMI → HDMI  
- Ratón USB Tipo A  
- Teclado USB Tipo A  

---

#### ⚙️ Activación de protocolos
Por defecto, la Raspberry Pi tiene inhabilitados algunos protocolos de comunicación.  
Para activarlos, ingresar a la terminal (local o remota) y ejecutar:  

```bash
sudo raspi-config
```
Se mostrará la interfaz de configuración. Debemos:  

1. Seleccionar **Interface Options**  
2. Aparecerá una lista de protocolos de telecomunicaciones disponibles:  
   - SPI  
   - VNC  
   - I2C  
   - Serial Port  
   - 1-Wire  
   - Remote GPIO  

3. Ingresar a cada protocolo que se quiera habilitar y seleccionar **Enable**.  

---

#### ✅ Finalización
- Una vez configurados todos los protocolos deseados, seleccionar **Finish**.  
- Si se solicita, realizar un **Reboot** para aplicar los cambios.  

📷 *Espacio para imagen de habilitación de protocolos en raspi-config*  

---

Con esto, la Raspberry Pi queda lista para utilizar todos los **protocolos de comunicación habilitados**.

