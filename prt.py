from time import time, sleep

from state import State

def update_state_from_prt(state: State):
    assert state.mutex.locked()

    # TODO

def prt_loop(state: State):
    while True:
        state.mutex.acquire()

        update_state_from_prt(state)

        update_interval = 60 # TODO: modify interval depending on situational factors

        state.last_state_update = time()
        state.state_update_interval = update_interval

        state.mutex.release()

        sleep(update_interval)