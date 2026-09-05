from dotenv import load_dotenv
import os
from threading import Thread

from display import display_loop
from prt import prt_loop
from state import State, StateManager

load_dotenv()

PRT_API_KEY = os.getenv("PRT_API_KEY")

print(PRT_API_KEY)

if __name__ == "__main__":
    # (streets, bus_routes) = parse_data_files()

    state_mgr = StateManager(State())

    prt_thread = Thread(target=prt_loop, args=(state_mgr,))
    display_thread = Thread(target=display_loop, args=(state_mgr,))