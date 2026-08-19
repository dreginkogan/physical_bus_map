from time import time, sleep

from state import State, StateManager

def update_state_from_prt(state: State):
    # TODO
    pass

def prt_loop(state_mgr: StateManager):
    while True:
        with state_mgr as state:
            update_state_from_prt(state)

            update_interval = 60 # TODO: modify interval depending on situational factors

            state.last_state_update = time()
            state.state_update_interval = update_interval

        sleep(update_interval)