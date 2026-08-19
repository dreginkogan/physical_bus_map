from threading import Thread

from state import State, StateManager
from prt import prt_loop
from display import display_loop

if __name__ == "__main__":
    state_mgr = StateManager(State())

    prt_thread = Thread(target=prt_loop, args=(state_mgr,))
    display_thread = Thread(target=display_loop, args=(state_mgr,))