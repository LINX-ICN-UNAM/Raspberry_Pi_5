#  Samba en Raspberry Pi (systemd)

Esta guía explica:

* Qué es Samba y para qué se usa
* Cómo se instala en Raspberry Pi OS / Debian
* Cómo funcionan los servicios (daemons) de Samba bajo systemd
* Explicación detallada del archivo `samba.service` / `samba-ad-dc.service`
* Cómo habilitar, iniciar y administrar Samba
* Uso básico (compartir carpetas)

---

## 1. ¿Qué es Samba?

Samba es una implementación libre del protocolo **SMB/CIFS**, utilizado principalmente por Windows para compartir:

* Archivos
* Carpetas
* Impresoras
* Servicios de red

Con Samba puedes hacer que una Raspberry Pi actúe como:

* Servidor de archivos compatible con Windows
* Cliente SMB
* Controlador de dominio (Active Directory)

En sistemas modernos, Samba se gestiona con **systemd**.

---

## 2. Instalación de Samba en Raspberry Pi

Actualizar sistema:

```bash
sudo apt update
sudo apt upgrade
```

Instalar Samba:

```bash
sudo apt install samba samba-common samba-common-bin
```

Verificar instalación:

```bash
samba --version
```

---

## 3. Servicios systemd de Samba

En tu sistema aparecen principalmente:

```
/lib/systemd/system/samba.service
/lib/systemd/system/samba-ad-dc.service
```

### Samba clásico (servidor de archivos)

➡ `samba.service`

### Samba como controlador de dominio (AD)

➡ `samba-ad-dc.service`

Normalmente en una Raspberry Pi doméstica o de laboratorio se usa `samba.service`. El `samba-ad-dc.service` se usa solo si montas Active Directory.

---

## 4. Explicación detallada del archivo systemd

Archivo:

```ini
[Unit]
Description=Samba AD Daemon
Documentation=man:samba(8) man:samba(7) man:smb.conf(5)
Wants=network-online.target
After=network.target network-online.target

[Service]
Type=notify
PIDFile=/run/samba/samba.pid
LimitNOFILE=16384
EnvironmentFile=-/etc/default/samba
ExecStart=/usr/sbin/samba --foreground --no-process-group $SAMBAOPTIONS
ExecReload=/bin/kill -HUP $MAINPID
ExecCondition=/usr/share/samba/is-configured samba

[Install]
WantedBy=multi-user.target
```

### [Unit]

```ini
Description=Samba AD Daemon
```

Nombre descriptivo del servicio.

```ini
Documentation=man:samba(8)
```

Referencia a manuales.

```ini
Wants=network-online.target
After=network.target network-online.target
```

Samba se inicia solo cuando la red está lista.

### [Service]

```ini
Type=notify
```

Samba notifica a systemd cuando ya está listo.

```ini
PIDFile=/run/samba/samba.pid
```

Archivo donde se guarda el PID del proceso.

```ini
LimitNOFILE=16384
```

Límite de archivos abiertos (muchas conexiones simultáneas).

```ini
EnvironmentFile=-/etc/default/samba
```

Carga variables opcionales de configuración.

```ini
ExecStart=/usr/sbin/samba --foreground --no-process-group $SAMBAOPTIONS
```

Comando principal que lanza el daemon Samba.

* `--foreground` → corre en primer plano (systemd lo gestiona)
* `--no-process-group` → evita conflictos con señales

```ini
ExecReload=/bin/kill -HUP $MAINPID
```

Recarga configuración sin detener servicio.

```ini
ExecCondition=/usr/share/samba/is-configured samba
```

Solo inicia si Samba está correctamente configurado.

### [Install]

```ini
WantedBy=multi-user.target
```

Permite que Samba se inicie automáticamente al arrancar el sistema.

---

## 5. Habilitar e iniciar Samba

Habilitar al arranque:

```bash
sudo systemctl enable samba
```

Iniciar ahora:

```bash
sudo systemctl start samba
```

Ver estado:

```bash
sudo systemctl status samba
```

Reiniciar:

```bash
sudo systemctl restart samba
```

Recargar configuración:

```bash
sudo systemctl reload samba
```

---

## 6. Archivo de configuración principal

📁 `/etc/samba/smb.conf`

Verlo:

```bash
sudo nano /etc/samba/smb.conf
```

Estructura básica:

```ini
[global]
   workgroup = WORKGROUP
   security = user

[Compartido]
   path = /home/pi/compartido
   writable = yes
   browseable = yes
   guest ok = no
```

---

## 7. Crear carpeta compartida

```bash
mkdir /home/pi/compartido
chmod 777 /home/pi/compartido
```

---

## 8. Crear usuario Samba

Debe existir como usuario Linux:

```bash
sudo adduser alfredo
```

Agregar a Samba:

```bash
sudo smbpasswd -a alfredo
```

Activar:

```bash
sudo smbpasswd -e alfredo
```

---

## 9. Acceder desde Windows o Linux

### Desde Windows

En el explorador de archivos:

```
\\IP_DE_LA_RASPBERRY
```

Ejemplo:

```
\\192.168.1.50
```

---

### Desde Linux

```bash
smbclient //IP/Compartido -U alfredo
```

O montar:

```bash
sudo mount -t cifs //IP/Compartido /mnt/samba -o user=alfredo
```

---

## 10. Diferencia entre samba.service y samba-ad-dc.service

| Servicio            | Uso                                     |
| ------------------- | --------------------------------------- |
| samba.service       | Servidor de archivos SMB normal         |
| samba-ad-dc.service | Controlador de dominio Active Directory |

👉 Para compartir archivos: usa `samba.service`

👉 Para redes empresariales: `samba-ad-dc.service`

---

## 11. Diagnóstico básico

Ver puertos abiertos:

```bash
sudo ss -tulnp | grep samba
```

Probar configuración:

```bash
testparm
```

Ver logs:

```bash
journalctl -u samba
```

Para revisar el estado del Daemon:

```bash
sudo systemctl status samba
```

# Run Program on Boot
copiar lo siguiente en:

```
/etc/systemd/system/rover.service
```

```txt
[Unit]
Description=Rover Control Web Server
After=network.target

[Service]
WorkingDirectory=/home/LINX_ROBOTS/Colmena_2_Rover/raspberry_ws
ExecStart=python3 /home/LINX_ROBOTS/Colmena_2_Rover/raspberry_ws/app.py
Restart=always
StandardOutput=syslog
StandardError=syslog
SyslogIdentifier=rover
User=LINX_ROBOTS
Group=LINX_ROBOTS
Environment=NODE_ENV=production

[Install]
WantedBy=multi-user.target
```

# Ejecutar un script automáticamente al arranque usando systemd (Raspberry Pi / Linux)

Esta guía explica cómo configurar y habilitar un servicio `systemd` para que tu aplicación Python se ejecute automáticamente al iniciar el sistema.

Usaremos como ejemplo el archivo:

```
/etc/systemd/system/rover.service
```

con el siguiente contenido:

```ini
[Unit]
Description=Rover Control Web Server
After=network.target

[Service]
WorkingDirectory=/home/LINX_ROBOTS/Colmena_2_Rover/raspberry_ws
ExecStart=python3 /home/LINX_ROBOTS/Colmena_2_Rover/raspberry_ws/app.py
Restart=always
StandardOutput=syslog
StandardError=syslog
SyslogIdentifier=rover
User=LINX_ROBOTS
Group=LINX_ROBOTS
Environment=NODE_ENV=production

[Install]
WantedBy=multi-user.target
```

---

## 1. Crear el archivo de servicio

Ejecuta:

```bash
sudo nano /etc/systemd/system/rover.service
```

Pega el contenido del servicio y guarda.

---

## 2. Explicación rápida de cada sección

### [Unit]

Define dependencias y descripción:

* `After=network.target` → Espera a que la red esté activa

---

### [Service]

| Directiva            | Función                            |
| -------------------- | ---------------------------------- |
| WorkingDirectory     | Carpeta donde se ejecuta el script |
| ExecStart            | Comando que inicia la app          |
| Restart=always       | Reinicia si falla                  |
| StandardOutput/Error | Envía logs a syslog                |
| SyslogIdentifier     | Nombre del proceso en logs         |
| User/Group           | Usuario que ejecuta el proceso     |
| Environment          | Variables de entorno               |

---

### [Install]

* `WantedBy=multi-user.target` → Se ejecuta en modo normal del sistema

---

## 3. Recargar systemd

Cada vez que creas o modificas un servicio:

```bash
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
```

---

## 4. Habilitar el servicio al arranque

```bash
sudo systemctl enable rover.service
```

Esto crea el enlace automático para el boot.

---

## 5. Iniciar el servicio manualmente (prueba)

```bash
sudo systemctl start rover.service
```

---

## 6. Ver estado del servicio

```bash
sudo systemctl status rover.service
```

Deberías ver algo como:

```
Active: active (running)
```

---

## 7. Ver logs del servicio

En tiempo real:

```bash
journalctl -u rover.service -f
```

Historial completo:

```bash
journalctl -u rover.service
```

---

## 8. Detener o reiniciar

```bash
sudo systemctl stop rover.service
sudo systemctl restart rover.service
```

---

## 9. Verificar que arranca en reboot

Reinicia:

```bash
sudo reboot
```

Luego:

```bash
systemctl status rover.service
```

---

## 10. Errores comunes

### ❌ Python no encontrado

Usa ruta absoluta:

```ini
ExecStart=/usr/bin/python3 /ruta/app.py
```

Ver ruta con:

```bash
which python3
```

---

### ❌ Permisos

Asegura que el usuario tiene acceso:

```bash
sudo chown -R LINX_ROBOTS:LINX_ROBOTS /home/LINX_ROBOTS/Colmena_2_Rover
```

---

### ❌ Script no ejecuta

Prueba manual:

```bash
sudo -u LINX_ROBOTS python3 /home/LINX_ROBOTS/Colmena_2_Rover/raspberry_ws/app.py
```

---

## 11. Deshabilitar del arranque (si quieres)

```bash
sudo systemctl disable rover.service
```

---

## Flujo típico de trabajo

```bash
sudo nano /etc/systemd/system/rover.service
sudo systemctl daemon-reload
sudo systemctl enable rover.service
sudo systemctl start rover.service
systemctl status rover.service
```

---

✅ Con esto tu aplicación Python se ejecutará automáticamente en cada arranque del sistema.
