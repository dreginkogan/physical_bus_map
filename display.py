from time import sleep

from state import State, StateManager

def update_display(state: State):
    # TODO
    pass

def display_loop(state_mgr: StateManager):
    while True:
        with state_mgr as state:
            update_display(state)

        sleep(0.05) # TODO: sleep this thread when nothing needs updating