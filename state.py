from threading import Lock

from routes import Route

class RouteState:
    pass

class State:
    mutex: Lock

    bus_routes: dict[Route, RouteState]

    def __init__(self, routes: list[Route]):
        self.mutex = Lock()

        for route in routes:
            self.bus_routes[route] = RouteState()