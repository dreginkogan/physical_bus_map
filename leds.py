from dataclasses import dataclass
from typing import NewType

from coords import Map2DCoords

@dataclass
class LED:
    coords: Map2DCoords

LEDID = NewType('LEDID', int)