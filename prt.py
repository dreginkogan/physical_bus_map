from time import time, sleep
import requests
import xmltodict
from main import PRT_API_KEY

from routes import ROUTES

from state import State, StateManager

def update_state_from_prt(state: State):
    # TODO
    routes_list = ",".join([route.value for route in ROUTES])

    # is it fine to just have this all be one blob? might be easier to break it up for debugging purposes.
    vehicle_data = xmltodict.parse(
                   requests.get(
                   f"http://realtime.portauthority.org/bustime/api/v3/getvehicles?key={PRT_API_KEY}&rt={routes_list}&rtpidatafeed=Port Authority Bus"
                   ).text, force_list=('vehicle',))

    # TODO make it so this ^ doesnt rely on xmltodict
    # TODO write json for bus stops to get estimates

    # TODO make dict that will be sent to state
    # Dict should encode: vid, timestamp, route, heading, latitude, longitude
    vehicles_dict = vehicle_data["bustime-response"]["vehicle"]

    state.busses = vehicles_dict
    #state.estimates = blablabla blebleble

    try:
        print()

    except Exception as e:
        print(f"Error: {e}")


    # state.busses

def prt_loop(state_mgr: StateManager):
    while True:
        with state_mgr as state:
            update_state_from_prt(state)

            update_interval = 60 # TODO: modify interval depending on situational factors

            state.last_state_update = time()
            state.state_update_interval = update_interval

        sleep(update_interval)