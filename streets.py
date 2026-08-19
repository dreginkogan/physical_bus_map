from dataclasses import dataclass

from coords import Map2DCoords

@dataclass
class StreetNode:
    pass

@dataclass
class StreetSeg:
    street_name: str

    # node indices
    nodes: tuple[int, int]

    # LED IDs, in order from nodes[0] to nodes[1]
    leds: list[int]

    # in order from nodes[0] to nodes[1]
    curve: list[Map2DCoords]

@dataclass
class DirectionalSegRef:
    seg_index: int
    is_reverse: bool

@dataclass
class CodedStreetSeg:
    street_name: str

    # node names
    nodes: tuple[str, str]

    # LED IDs, in order from nodes[0] to nodes[1]
    leds: list[int]

    # in order from nodes[0] to nodes[1]
    curve: list[Map2DCoords]

class StreetsGraph:
    nodes: list[StreetNode]
    segs: list[StreetSeg]

    adj_matrix: list[list[DirectionalSegRef]]

    def __init__(self, segs: list[CodedStreetSeg]):
        node_names: list[str] = []

        for seg in segs:
            node_0_index = node_names.index(seg.nodes[0])
            node_1_index = node_names.index(seg.nodes[1])

            if node_0_index == -1:
                node_0_index = len(node_names)
                node_names.append(seg.nodes[0])
            if node_1_index == -1:
                node_1_index = len(node_names)
                node_names.append(seg.nodes[1])

            self.segs.append(CodedStreetSeg(
                seg.street_name,
                (node_0_index, node_1_index),
                seg.leds,
                seg.curve,
            ))

        for _ in node_names:
            self.nodes.append(StreetNode())
            self.adj_matrix.append([None for _ in node_names])

        for i, seg in enumerate(self.segs):
            self.adj_matrix[seg.nodes[0]][seg.nodes[1]] = DirectionalSegRef(i, False)
            self.adj_matrix[seg.nodes[1]][seg.nodes[0]] = DirectionalSegRef(i, True)