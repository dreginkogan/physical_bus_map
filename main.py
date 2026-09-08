from dotenv import load_dotenv
import os
from threading import Thread

from display import display_loop
from prt import prt_loop
from state import State, StateManager

if __name__ == "__main__":
    # (streets, bus_routes) = parse_data_files()

    state_mgr = StateManager(State())

    prt_thread = Thread(target=prt_loop, args=(state_mgr,)) #TODO, add time estimates
    display_thread = Thread(target=display_loop, args=(state_mgr,))

    prt_thread.start()
    display_thread.start()