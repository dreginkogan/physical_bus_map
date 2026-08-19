from enum import Enum
from dataclasses import dataclass

from coords import Map2DCoords

class StreetNode(Enum):
    pass

@dataclass
class StreetSeg:
    street_name: str
    nodes: tuple[StreetNode, StreetNode]
    leds: dict[int, Map2DCoords] # maps LED IDs to their coordinates

street_segs: list[StreetSeg] = [
    
]