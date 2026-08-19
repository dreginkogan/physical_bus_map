from threading import Thread

from state import State
from prt import prt_loop
from display import display_loop

if __name__ == "__main__":
    state = State()

    prt_thread = Thread(target=prt_loop, args=(state,))
    display_thread = Thread(target=display_loop, args=(state,))