import RPi.GPIO as GPIO
import time

# Set up GPIO mode 
# Use GPIO.BOARD to refer to pins by their physical pin number
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)  # Opcional: silenciar advertencias

# Set up GPIO pin 11 as an output pin
LED_PIN = 11 # Pin físico 11 (GPIO 17)
GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)

print("Blinking LED on BOARD pin 11")
# Blink the LED indefinitely
try:
    while True:
        print("Turning on LED on BOARD pin 11")
        GPIO.output(LED_PIN, True) # Turn the LED on
        time.sleep(1)
        print("Turning off LED on BOARD pin 11")
        GPIO.output(LED_PIN, False) # Turn the LED off
        time.sleep(1)
except KeyboardInterrupt:
    print(" Exiting program...")
finally:
    GPIO.cleanup() # Clean up GPIO settings avoid GPIO allocated error (pin en uso)