import RPi.GPIO as GPIO
import time

# Set up GPIO mode 
# Use GPIO.BCM to refer to pins by their Broadcom SOC channel number
GPIO.setmode(GPIO.BCM)

# Set up GPIO pin 4 as an output pin
LED_PIN = 4 # Pin físico 7 (GPIO 4)
GPIO.setup(LED_PIN, GPIO.OUT)

print("Blinking LED on BCM pin 2")
# Blink the LED indefinitely
try:
    while True:
        print("Turning on LED on BCM pin 2")
        GPIO.output(LED_PIN, True) # Turn the LED on
        time.sleep(1)
        print("Turning off LED on BCM pin 2")
        GPIO.output(LED_PIN, False) # Turn the LED off
        time.sleep(1)
except KeyboardInterrupt:
    print(" Exiting program...")
finally:
    GPIO.cleanup() # Clean up GPIO settings