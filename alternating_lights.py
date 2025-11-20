import RPi.GPIO as GPIO
import time

# --- Configuration ---
# We now have 4 pins, one for each transistor
LED_PIN_1 = 17  # Controls Set 1
LED_PIN_2 = 27  # Controls Set 2
LED_PIN_3 = 22  # Controls Set 3
LED_PIN_4 = 23  # Controls Set 4
DELAY = 1       # Time (in seconds) to wait before swapping

# --- Setup ---
try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    # Set up all 4 pins as outputs
    GPIO.setup(LED_PIN_1, GPIO.OUT)
    GPIO.setup(LED_PIN_2, GPIO.OUT)
    GPIO.setup(LED_PIN_3, GPIO.OUT)
    GPIO.setup(LED_PIN_4, GPIO.OUT)

    print("Starting the 4-set light show! Press Ctrl+C to stop.")

    # --- Main Loop ---
    while True:
        # Turn Sets 1 & 2 ON, and Sets 3 & 4 OFF
        print("SETS 1 & 2 ON | SETS 3 & 4 OFF")
        GPIO.output(LED_PIN_1, GPIO.HIGH)
        GPIO.output(LED_PIN_2, GPIO.HIGH)
        GPIO.output(LED_PIN_3, GPIO.LOW)
        GPIO.output(LED_PIN_4, GPIO.LOW)
        
        time.sleep(DELAY)
        
        # Turn Sets 1 & 2 OFF, and Sets 3 & 4 ON
        print("SETS 1 & 2 OFF | SETS 3 & 4 ON")
        GPIO.output(LED_PIN_1, GPIO.LOW)
        GPIO.output(LED_PIN_2, GPIO.LOW)
        GPIO.output(LED_PIN_3, GPIO.HIGH)
        GPIO.output(LED_PIN_4, GPIO.HIGH)
        
        time.sleep(DELAY)

except KeyboardInterrupt:
    print("\nStopping the script and cleaning up...")

finally:
    # Clean up all 4 pins
    GPIO.cleanup()
    print("GPIO pins cleaned up. Exiting.")
