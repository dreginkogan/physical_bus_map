from time import sleep
import board
import neopixel

from state import State, StateManager

from coord_to_led import coords_to_led

LED_PIN = board.D18 # fyi this has to run on rpi, will throw errors if just ran on laptop 
LED_COUNT = 362
BRIGHTNESS = 0.6

# auto_write = False means that changes won't show until pixels.show() is called
pixels = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=BRIGHTNESS, auto_write=False)

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def update_display(state: State):
    pixels.fill((0, 0, 0))

    vehicles_list = state.busses

    for bus in vehicles_list:
        bus_rt = bus["rt"]
        bus_dir = bus["rtdir"]

        bus_lat = float(bus["lat"])
        bus_lon = float(bus["lon"])

        leds_to_light, color = coords_to_led(bus_rt, bus_dir, bus_lat, bus_lon)

        print(f"Lighting {leds_to_light} the color {color}")

        for led in leds_to_light:
            pixels[led] = hex_to_rgb(color)

    print()
    pixels.show()

    pass

def display_loop(state_mgr: StateManager):
    while True:
        with state_mgr as state:
            update_display(state)

        sleep(60)