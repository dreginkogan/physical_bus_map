from threading import Lock

from routes import Route

class RouteState:
    pass

class State:
    mutex: Lock

    last_state_update: float # seconds since epoch
    state_update_interval: float # seconds from last state update to start of next state update (sleep duration)

    bus_routes: dict[Route, RouteState]

    def __init__(self, routes: list[Route]):
        self.mutex = Lock()

        for route in routes:
            self.bus_routes[route] = RouteState()