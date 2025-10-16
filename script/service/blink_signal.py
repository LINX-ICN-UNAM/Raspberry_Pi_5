import RPi.GPIO as GPIO
import time
import signal
import sys
import os
import logging

# Configurar logging para systemd
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger()

def signal_handler(signum, frame):
    """Manejador de señales para terminación graceful"""
    
    # Mapear números de señal a nombres
    signal_names = {
        signal.SIGTERM: 'SIGTERM',  # systemd stop
        signal.SIGINT: 'SIGINT',    # Ctrl+C
        signal.SIGHUP: 'SIGHUP',    # Recarga
        signal.SIGUSR1: 'SIGUSR1'   # Señal personalizada
    }
        
    signal_name = signal_names.get(signum, f'Señal {signum}')
    logger.info(f"📡 Recibida {signal_name}. Iniciando shutdown graceful...")
    
    # Acciones específicas por tipo de señal
    if signum == signal.SIGTERM:
        logger.info("Deteniendo servicio por systemd...")
    elif signum == signal.SIGINT:
        logger.info("Deteniendo servicio por Ctrl+C...")
    elif signum == signal.SIGHUP:
        logger.info("Recargando configuración...")
        # Aquí podrías recargar configuraciones sin detener
        return
    
    # Limpieza del GPIO
    cleanup_gpio()
    
    # Salir del programa
    sys.exit(0 if signum in [signal.SIGTERM, signal.SIGINT] else 1)

def cleanup_gpio():
    """Función dedicada para limpiar GPIO"""
    logger.info("🧹 Limpiando recursos GPIO...")
    try:
        GPIO.cleanup()
        logger.info("✅ GPIO limpiado correctamente")
    except Exception as e:
        logger.error(f"❌ Error limpiando GPIO: {e}")

def custom_actions(signum):
    """Acciones personalizadas basadas en la señal"""
    if signum == signal.SIGUSR1:
        logger.info("🔧 Acción personalizada: Cambiando patrón de blink")
        return "change_pattern"
    return None

# Registrar manejadores para múltiples señales
signal.signal(signal.SIGTERM, signal_handler)  # systemd stop
signal.signal(signal.SIGINT, signal_handler)   # Ctrl+C
signal.signal(signal.SIGHUP, signal_handler)   # Recarga
signal.signal(signal.SIGUSR1, signal_handler)  # Señal personalizada

# Información del servicio
logger.info(f"🚀 Servicio iniciado - PID: {os.getpid()}, Directorio: {os.getcwd()}")

# Configuración GPIO
try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    LED_PIN = 17  # GPIO 17 (pin físico 11)
    GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)
    
    logger.info(f"✅ GPIO {LED_PIN} configurado como OUTPUT")

except Exception as e:
    logger.error(f"❌ Error configurando GPIO: {e}")
    sys.exit(1)

# Bucle principal con manejo de estado
logger.info("🔴 Iniciando patrón de blink...")

try:
    blink_state = True
    while True:
        # Controlar el LED
        GPIO.output(LED_PIN, blink_state)
        current_state = "ON" if blink_state else "OFF"
        
        # Log cada 10 ciclos para no saturar
        if int(time.time()) % 10 == 0:
            logger.info(f"💡 LED {current_state} - Servicio activo")
        
        # Cambiar estado
        blink_state = not blink_state
        time.sleep(1)
        
except Exception as e:
    logger.error(f"💥 Error en el bucle principal: {e}")
    
finally:
    # Garantizar limpieza incluso si hay excepciones
    cleanup_gpio()
    logger.info("👋 Servicio terminado")