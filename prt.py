from time import time, sleep
import requests
import xmltodict
import os
import json

from state import State, StateManager

from load_api_key import PRT_API_KEY

with open('routes.json') as f:
    routes_dict = json.load(f)["ROUTES"]

map_corners = [(40.467143, -79.955775), (40.456565, -79.938941)]

def purge_outside_busses(vehicles, corners):
    """Returns a dict with busses that are only within the physical bounds of the map

    Parameters
    ----------
    vehicles : list
        list returned from api, e.g. vehicle_data["bustime-response"]["vehicle"]
    corners : list
        A list of two tuples demarcating the NW and SE corners of the map

    Returns
    -------
    dict
        vehicle dict with busses only within the defined bounds
    """

    for vehicle in vehicles:
        lat = float(vehicle["lat"])
        lon = float(vehicle["lon"])

        if lat>corners[0][0] or lat<corners[1][0] or lon>corners[0][1] or lat<corners[1][1]:
            vehicles.remove(vehicle)

    return vehicles

def update_state_from_prt(state: State):
    routes_list = ",".join([route for route in routes_dict])

    try:

        # is it fine to just have this all be one blob? might be easier to break it up for debugging purposes.
        vehicle_data = xmltodict.parse(
                    requests.get(
                    f"http://realtime.portauthority.org/bustime/api/v3/getvehicles?key={PRT_API_KEY}&rt={routes_list}&rtpidatafeed=Port Authority Bus"
                    ).text, force_list=('vehicle',))

        # TODO make it so this ^ doesnt rely on xmltodict
        # TODO write json for bus stops to get estimates
        # or maybe make it its own file?

        # remove vehicles outside of geographic bounds from dict
        vehicles_list = purge_outside_busses(vehicle_data["bustime-response"]["vehicle"], map_corners)
        # vehicles_list = vehicle_data["bustime-response"]["vehicle"]

        # DEBUG
        print("the vehicles that are in the map irl arn are:")
        print()
        for vehicle in vehicles_list:
            print(f"The Humble {vehicle["rt"]} heading {vehicle["rtdir"]}")
        print()

        state.busses = vehicles_list
        #state.estimates = blablabla blebleble

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