'''
Script para hacer parpadear un LED conectado al GPIO de una Raspberry Pi usando la biblioteca gpiozero.
try, except KeyboardInterrupt para manejar la interrupción del usuario con Ctrl+C.
'''

from gpiozero import LED
from time import sleep

# Usar GPIO 17 (pin físico 11)
led = LED(17)

print("Iniciando blink...")
print("Presiona Ctrl+C para detener")

try:
    while True:
        led.on()
        print("LED encendido")
        sleep(1)
        led.off()
        print("LED apagado")
        sleep(1)
except KeyboardInterrupt:
    print("\nPrograma detenido")
    led.off()