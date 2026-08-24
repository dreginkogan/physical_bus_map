from time import time, sleep
import requests
import xmltodict

from routes import ROUTES

from state import State, StateManager

def update_state_from_prt(state: State):
    # TODO
    routes_list = ",".join([route.value for route in ROUTES])

    vehicle_data = xmltodict.parse(
                   requests.get(
                   f"http://realtime.portauthority.org/bustime/api/v3/getvehicles?key={api_key}&rt={routes_list}&rtpidatafeed=Port Authority Bus"
                   ).text)

    # TODO make it so this doesnt use xmltodict
    print(vehicle_data)

    pass

def prt_loop(state_mgr: StateManager):
    while True:
        with state_mgr as state:
            update_state_from_prt(state)

            update_interval = 60 # TODO: modify interval depending on situational factors

            state.last_state_update = time()
            state.state_update_interval = update_interval

        sleep(update_interval)