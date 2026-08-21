import json
import board
import neopixel
import random

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

try:

    for route_name, route_segs in route_data["ROUTES"].items():

        route_color = route_segs['COLOR']
        inbound_segs = route_segs['INBOUND']
        outbound_segs = route_segs['OUTBOUND']

        print(inbound_segs)
        
        for seg in inbound_segs:
            print(f"seg {seg}")
            for led_id in segment_data[seg]:
                pixels[int(led_id)] = (256, 200, 200)


    # for seg_id, segment in data.items():
    #     r = random.randrange(0, 256)
    #     g = random.randrange(0, 256)
    #     b = random.randrange(0, 256)


    #     for led_id in segment["led_ids"]:
    #         pixels[int(led_id)] = (r, g, b)

    # pixels.show()
                

except KeyboardInterrupt:
    # Clear the strip cleanly when exiting
    pixels.fill((0, 0, 0))
    pixels.show()
    print("\nLEDs turned off.")

