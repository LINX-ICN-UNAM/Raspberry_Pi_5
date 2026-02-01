# Samba
copiar lo siguiente en:

```
/lib/systemd/system/samba-ad-dc.service
/lib/systemd/system/samba.service
```


```txt
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
