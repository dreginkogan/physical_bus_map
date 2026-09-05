from threading import Lock
from typing import Optional

class State:
    last_state_update: Optional[float] # seconds since epoch
    state_update_interval: float # seconds from last state update to start of next state update (sleep duration)

    busses = dict()
    estimates = dict() # values are seconds since epoch

    def __init__(self):
        self.last_state_update = None
        self.state_update_interval = 0.0

        # self.streets = streets
        # self.bus_routes = routes


class StateManager:
    lock: Lock

    _state: State

    def __init__(self, state: State):
        self.lock = Lock()

        self._state = state

    def __enter__(self) -> State:
        self.lock.acquire()

        return self._state

    def __exit__(self, exc_type, exc, tb):
        self.lock.release()