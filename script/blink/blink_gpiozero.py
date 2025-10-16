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