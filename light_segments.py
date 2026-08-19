import json

import board
import neopixel

# --- CONFIGURATION ---
LED_PIN = board.D18          # Uses GPIO 18 (PWM standard pin)
LED_COUNT = 362            # Change this to the number of LEDs on your strip
BRIGHTNESS = 0.6             # Set brightness level (0.0 to 1.0)

# Initialize the NeoPixel strip
# auto_write=False means changes won't show until we call pixels.show()
pixels = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=BRIGHTNESS, auto_write=False)

with open('segments.json') as file:
    data = json.load(file)

for segment in data:
    print(segment)