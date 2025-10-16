import RPi.GPIO as GPIO
import time

# Set up GPIO mode 
# Use GPIO.BCM to refer to pins by their Broadcom SOC channel number
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)  # Opcional: silenciar advertencias

# Set up GPIO pin 17 as an output pin
LED_PIN = 17 # Pin físico 11 (GPIO 17)
GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)

print("Blinking LED on BCM pin 17")
# Blink the LED indefinitely
try:
    while True:
        print("Turning on LED on BCM pin 17")
        GPIO.output(LED_PIN, True) # Turn the LED on
        time.sleep(1)
        print("Turning off LED on BCM pin 17")
        GPIO.output(LED_PIN, False) # Turn the LED off
        time.sleep(1)
except KeyboardInterrupt:
    print(" Exiting program...")
finally:
    GPIO.cleanup() # Clean up GPIO settings