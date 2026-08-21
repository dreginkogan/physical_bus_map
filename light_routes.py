import json
import board
import neopixel
import random
import time

# --- CONFIGURATION ---
LED_PIN = board.D18          # Uses GPIO 18 (PWM standard pin)
LED_COUNT = 362            # Change this to the number of LEDs on your strip
BRIGHTNESS = 0.6             # Set brightness level (0.0 to 1.0)

# Initialize the NeoPixel strip
# auto_write=False means changes won't show until we call pixels.show()
pixels = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=BRIGHTNESS, auto_write=False)

with open('routes.json') as route_segment_file:
    route_data = json.load(route_segment_file)

with open('segments.json') as segments:
    segment_data = json.load(segments)

def hex_to_rgb(hex_str: str) -> tuple[int, int, int]:
  hex_str = hex_str.lstrip("#")
  return tuple(int(hex_str[i : i + 2], 16) for i in (0, 2, 4))

try:

    while True:

        for route_name, route_segs in route_data["ROUTES"].items():

            route_color = route_segs['COLOR']
            inbound_segs = route_segs['INBOUND']
            outbound_segs = route_segs['OUTBOUND']

            print(f"Displaying route {route_name}")

            i = 30

            while i>0:
            
                for seg in inbound_segs:
                    for led_id in segment_data[seg]["led_ids"]:
                        pixels[int(led_id)] = hex_to_rgb(route_color)

                time.sleep(0.05)
                pixels.show()
                pixels.fill((0, 0, 0))

                for seg in outbound_segs:
                            for led_id in segment_data[seg]["led_ids"]:
                                pixels[int(led_id)] = hex_to_rgb(route_color)

                time.sleep(0.05)
                pixels.show()
                pixels.fill((0, 0, 0))
                i-=1
                

except KeyboardInterrupt:
    # Clear the strip cleanly when exiting
    pixels.fill((0, 0, 0))
    pixels.show()
    print("\nLEDs turned off.")

