from routes import DirectionalRouteNumber
from streets import StreetGraph

def parse_data_files() -> tuple[StreetGraph, dict[DirectionalRouteNumber, list[int]]]:
    return (StreetGraph(), dict()) # TODO