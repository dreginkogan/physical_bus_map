from dataclasses import dataclass
from typing import Optional

from coords import Map2DCoords

@dataclass
class StreetNode:
    point: Map2DCoords

@dataclass
class StreetSeg:
    street_name: str

    # node indices
    nodes: tuple[int, int]

    # LED IDs, in order from nodes[0] to nodes[1]
    leds: list[int]

    # in order from nodes[0] to nodes[1], omitting nodes[0].point and nodes[1].point
    curve: list[Map2DCoords]

@dataclass
class DirectionalSegRef:
    seg_index: int
    is_reverse: bool

class StreetGraph:
    nodes: list[StreetNode]
    segs: list[StreetSeg]

    adj_matrix: list[list[Optional[DirectionalSegRef]]]

    def __init__(self, nodes: list[StreetNode], segs: list[StreetSeg]):
        self.nodes = nodes
        self.segs = segs

        self.adj_matrix = [[None for _ in self.nodes] for _ in self.nodes]

        for i, seg in enumerate(self.segs):
            self.adj_matrix[seg.nodes[0]][seg.nodes[1]] = DirectionalSegRef(i, False)
            self.adj_matrix[seg.nodes[1]][seg.nodes[0]] = DirectionalSegRef(i, True)