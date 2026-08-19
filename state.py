from threading import Lock
from typing import Optional

from routes import DirectionalRouteNumber
from streets import StreetGraph

class State:
    mutex: Lock

    last_state_update: Optional[float] # seconds since epoch
    state_update_interval: float # seconds from last state update to start of next state update (sleep duration)

    streets: StreetGraph
    bus_routes: dict[DirectionalRouteNumber, list[int]]

    def __init__(self, streets: StreetGraph, routes: dict[DirectionalRouteNumber, list[int]]):
        self.mutex = Lock()

        self.last_state_update = None
        self.state_update_interval = 0.0

        self.streets = streets
        self.bus_routes = routes