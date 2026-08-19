from time import sleep

from state import State

def update_display(state: State):
    assert state.mutex.locked()

    # TODO

def display_loop(state: State):
    while True:
        state.mutex.acquire()

        update_display(state)

        state.mutex.release()

        sleep(0.05) # TODO: sleep this thread when nothing needs updating