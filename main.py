from threading import Thread

from display import display_loop
from parse import parse_data_files
from prt import prt_loop
from state import State, StateManager

if __name__ == "__main__":
    (streets, bus_routes) = parse_data_files()

    state_mgr = StateManager(State(streets, bus_routes))

    prt_thread = Thread(target=prt_loop, args=(state_mgr,))
    display_thread = Thread(target=display_loop, args=(state_mgr,))