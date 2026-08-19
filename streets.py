from dataclasses import dataclass
from typing import NewType

from leds import LEDID

@dataclass
class StreetNode:
    pass

NodeID = NewType('NodeID', int)

@dataclass
class StreetSeg:
    street_name: str
    nodes: tuple[NodeID, NodeID]
    leds: list[LEDID] # in order from nodes[0] to nodes[1]

SegID = NewType('StreetSegID', int)