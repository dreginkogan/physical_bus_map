import os
import dotenv

dotenv.load_dotenv()

# for some reason, dotenv wont load when main.py is run with sudo (needs to be run with sudo for neopixels)

PRT_API_KEY = os.getenv("PRT_API_KEY")