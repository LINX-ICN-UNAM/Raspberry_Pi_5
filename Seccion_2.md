# 📂 Sección 2: Configuración Intermedia

- [📂 Sección 2: Configuración Intermedia](#-sección-2-configuración-intermedia)
  - [🌐 Redes y Conexiones](#-redes-y-conexiones)
    - [🔢 IP Fija](#-ip-fija)
    - [🔌 Conexión con cable Ethernet](#-conexión-con-cable-ethernet)
    - [💻 Conexión por VSCode](#-conexión-por-vscode)
  - [📜 Scripts](#-scripts)
    - [📚 Librerias de python](#-librerias-de-python)
    - [🐍 Virtual Enviroments en Python](#-virtual-enviroments-en-python)
    - [⚙️ Cargar Script](#️-cargar-script)
  - [🔧 Sensores y Hardware](#-sensores-y-hardware)
    - [🔌 Biblioteca GPIO](#-biblioteca-gpio)
    - [Script al arrancar Raspberry Pi](#script-al-arrancar-raspberry-pi)

## 🌐 Redes y Conexiones

### 🔢 IP Fija

Para asignar una **IP fija** a tu Raspberry Pi usando `nmtui` (Network Manager Text User Interface), sigue estos pasos:

1. Abre la terminal en tu Raspberry Pi (localmente o por SSH).
2. Instala *Network Manager*:

   ```bash
   sudo apt install network-manager
   ```

3. Ejecuta el siguiente comando para abrir el asistente de configuración de red:

   ```bash
   sudo nmtui
   ```

4. Selecciona la opción **"Edit a connection"** y elige la interfaz de red que deseas configurar (por ejemplo, `wlan0` para WiFi o `eth0` para Ethernet).
5. En el campo **"IPv4 CONFIGURATION"**, cambia el método de `Automatic (DHCP)` a `Manual`.
6. Añade la dirección IP deseada, la máscara de red y la puerta de enlace (gateway). Ejemplo:
   - **Address**: `192.168.1.50/24`
   - **Gateway**: `192.168.1.1`
7. (Opcional) Agrega los servidores DNS si lo requieres.
8. Guarda los cambios y selecciona **"Back"**.
9. Reinicia la interfaz de red o la Raspberry Pi para aplicar los cambios:

   ```bash
   sudo systemctl restart NetworkManager
   ```

   o simplemente reinicia con:

   ```bash
   sudo reboot
   ```

Algunas opciones para IPs:

- WIFI:  `192.168.10.50/24`
- Ethernet: `192.168.1.50/24`
- Hostpot: `192.168.4.1/24`
- Colmena: `192.168.10.1/24`

📷 *Espacio para imagen de menú principal de nmtui*  
📷 *Espacio para imagen de edición de conexión y configuración manual de IP*  

---

### 🔌 Conexión con cable Ethernet

Para conectar tu Raspberry Pi a internet mediante un cable Ethernet, sigue estos pasos:

1. Conecta un extremo del cable Ethernet al puerto Ethernet de tu Raspberry Pi y el otro extremo a un puerto libre de tu router o switch de red.
2. La Raspberry Pi debería detectar automáticamente la conexión. Para verificar, puedes usar el comando:

   ```bash
   ip a
   ```

   Busca una interfaz llamada `eth0` y verifica que tenga una dirección IP asignada.

📷 *Espacio para imagen de conexión por cable Ethernet*  

### 💻 Conexión por VSCode

Para quitar una llave asociada a algun Host SSH, en `powershell`:

```powershell
ssh-keygen -R <hostname/ip>
```

---

## 📜 Scripts

### 📚 Librerias de python

### 🐍 Virtual Enviroments en Python

Para crear ambientes que puedan acceder a las librerias del sistema

```bash
python3 -m venv --system-site-packages .venv
```

Donde `.venv` es el nombre del ambiente, puede ser cambiado pero no se recomienda por simplicidad, a menos que necesites varios ambientes. el flag `--system-site-packages` permite que el ambiente virtual pueda usar las bibliotecas globales, osea las instaladas con `sudo apt`.

 Para activar un virtual enviroment:

```bash
source .venv/bin/activate
```

Para desactivar un virtual enviroment:

```bash
deactivate
```

Una buena practica para poder compartir el codigo es dar las librerias instaladas y su respectiva versión. Dentro de un ambiente solo se cargarán aquellas a las que pueda acceder `pip`:

```bash
pip freeze > requirements.txt
```

Esto crea un archivo `requirements.txt` en el directorio de trabajo actual.

### ⚙️ Cargar Script

Para cargar un script en tu Raspberry Pi, sigue estos pasos:

1. Transfiere el archivo del script a tu Raspberry Pi usando SCP, SFTP o un dispositivo USB.
2. Navega hasta el directorio donde se encuentra el script.
3. Asegúrate de que el script tenga permisos de ejecución. Si no, otórgale permisos con el comando:

   ```bash
   chmod +x nombre_del_script.sh
   ```

4. Ejecuta el script con el comando:

   ```bash
   ./nombre_del_script.sh
   ```

   Si es de python:

📷 *Espacio para imagen de transferencia y ejecución de script*  

---

## 🔧 Sensores y Hardware

Para conectar y configurar sensores u otro hardware en tu Raspberry Pi, sigue estos pasos generales:

1. Apaga tu Raspberry Pi y desconéctala de la corriente.
2. Conecta el sensor o hardware en los pines GPIO correspondientes. Consulta la documentación del sensor y de la Raspberry Pi para conocer los pines correctos.
3. Vuelve a conectar y encender tu Raspberry Pi.
4. Instala las bibliotecas o controladores necesarios para el sensor o hardware que estás utilizando.
5. Escribe un script o programa para interactuar con el sensor o hardware. Consulta la documentación específica para conocer los comandos y funciones disponibles.

### 🔌 Biblioteca GPIO

Un usuario se puede conectar a los pines de la Raspberri Pi mediante su número fisico o su número BCM (*Broadcom SOC channel number*)

<img src="img/GPIO-Pinout.png" alt="GPRIO Pintout" />

Para viejas versiones de Raspberry Pi se utilizaba por defecto la biblioteca `RPi.GPIO` que es una *Biblioteca de Backend* que accede a los registros de hardware para controlar los pines por ejemplo.

Pero estos dependen bastante del hardware en el que esta implementado y en Raspberry Pi 5 el hardware es diferente, con el GPIO gestionado por el chip RPI1, que no es compatible con las Pi anteriores. Por lo que se recomienda que se acceda a los pines mediante el kernel de Linux.

Se recomienda en **Raspberry Pi 5** remover la libreria `RPi.GPIO` para evitar conflictos:

```bash
sudo apt unistall RPi.GPIO
```

Para poder acceder al GPIO se pueden utilizar las siguientes bibliotecas en todo el sistema, es decir, no pueden ser compiladas dentro de un [virtual enviroment](#-virtual-enviroments-en-python):

- `rpi-lgpio`: debe instalarse en toda la Raspberry Pi utilizando

   ```bash
   sudo apt install python3-rpi-lgpio
   ```

  y **NO** debe estar instalada la biblioteca RPi.GPIO

- `gpiozero`: contiene *RPi.GPIO* y *rpi-lgpio*, se recomienda esta opcion por compatibilidad con `lgpio` de backend
  
  ```bash
   sudo apt install gpiozero
   ```

Con esto la libreria GPIO queda configurada para usar el kernel de Linux como intermediario. Aunque es mas rapido utilizar `RPi.GPIO` ya que es mucho más rápido trabajar directamente con el Hardware que pedirle al controlador del dispositivo del kernel que lo haga. Sin embargo, no ofrecen protección contra el acceso concurrente y pueden entrar en conflicto entre sí, entre sí mismas y con las bibliotecas que usan el kernel.

### Script al arrancar Raspberry Pi

Para ello necesitamos tener un script de python. Adicionalmente se puede tener un viertual enviroment asociado.

Primero se deben conceder los permisos:

```bash
chmod +x <nombre-del-archivo>
```

📷 *Espacio para imagen*  

Luego, se cambia al directorio del Sistema donde estan los servicios:

```bash
cd /lib/systemd/system
```

Ahí habrán muchos archivos tipo `.service`. Para iniciar un script durante el arranque vamos a crear un nuevo servicio:

```bash
sudo touch nombre-del-servicio.service
```

Se recomienda el uso de Nano para poder editar el archivo con permisos de administrador:

```bash
sudo nano nombre-del-servicio.service
```

Dentro se debe colocar lo siguiente

```text
[Unit]
Description=Descripcion del servicio
After=multi-user.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 /directorio/de/archivo.py
WorkingDirectory=/directorio/del/proyecto
User=linx-robot
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```

Donde:

- **Unit**
  - **Description**
  - **After**
- **Service**
  - **ExecStart**
  - **User**
- **Install**
  - **WantedBy**

Comandos utiles en nano

- `ctrl + s` Guardar archivo
- `ctrl + x` Salir del archivo

Ahora, en el directorio local `~` se debe reiniciar el *daemon*, que es como se llama a un programa que se corre en segundo plano:

```bash
sudo systemctl daemon-reload
```

Probar el servicio:

```bash
sudo systemctl start nombre-del-servicio.service
```

Ver estado del servicio:

```bash
sudo systemctl status nombre-del-servicio.service
```

Y habilitar el servicio:

```bash
sudo systemctl enable nombre-del-servicio.service
```

O habilitar e iniciar el servicio:

```bash
sudo systemctl enable --now blink_BCM.service
```

Para detener el servicio:

```bash
sudo systemctl stop nombre-del-servicio.service
```

Para desactivar el servicio:

```bash
sudo systemctl disable nombre-del-servicio.service
```

Forzar terminación (en caso de emergencia):

```bash
sudo systemctl kill nombre-del-servicio.service
```
