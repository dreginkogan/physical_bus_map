from dataclasses import dataclass

# WGS 84
@dataclass
class LatLonCoords:
    lat: float
    lon: float

    def to_map_2d(self) -> 'Map2DCoords':
        return Map2DCoords(0.0, 0.0) # TODO

@dataclass
class Map2DCoords:
    x: float
    y: float

    def to_lat_lon(self) -> LatLonCoords:
        return LatLonCoords(0.0, 0.0) # TODO

@dataclass
class StreetCoords:
    ss_id: int # street segment ID
    z: float