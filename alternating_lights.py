import RPi.GPIO as GPIO
import time

# --- Configuration ---
LED_PIN_1 = 17  # This pin now controls Transistor 1
LED_PIN_2 = 27  # This pin now controls Transistor 2
DELAY = 1       # Time (in seconds) to wait before swapping

# --- Setup ---
try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(LED_PIN_1, GPIO.OUT)
    GPIO.setup(LED_PIN_2, GPIO.OUT)

    print("Starting the 10-LED light show! Press Ctrl+C to stop.")

    # --- Main Loop ---
    while True:
        # Turn Set 1 ON (by activating Transistor 1)
        # Turn Set 2 OFF (by deactivating Transistor 2)
        print("SET 1 ON | SET 2 OFF")
        GPIO.output(LED_PIN_1, GPIO.HIGH)
        GPIO.output(LED_PIN_2, GPIO.LOW)
        
        time.sleep(DELAY)
        
        # Turn Set 1 OFF
        # Turn Set 2 ON
        print("SET 1 OFF | SET 2 ON")
        GPIO.output(LED_PIN_1, GPIO.LOW)
        GPIO.output(LED_PIN_2, GPIO.HIGH)
        
        time.sleep(DELAY)

except KeyboardInterrupt:
    print("\nStopping the script and cleaning up...")

finally:
    GPIO.cleanup()
    print("GPIO pins cleaned up. Exiting.")
