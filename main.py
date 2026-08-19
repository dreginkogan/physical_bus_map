from threading import Thread

from state import State

if __name__ == "__main__":
    state = State()

    prt_thread = Thread(args=(state,))
    display_thread = Thread(args=(state,))