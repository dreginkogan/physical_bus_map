# Coordinate Systems

This file documents the coordinate systems used for the physical bus map, and the procedures to convert from one to another.

## Coordinate Systems Reference

Currently, the map uses three coordinate systems:

### `lat_lon`: Latitude-Longitude Coordinates

This is the latitude-longitude coordinate system used by the PRT API, which is [WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System).

### `map_2d`: Physical Bus Map 2D Coordinates

This is a 2D coordinate pair representing a position on the physical map. The `x` axis is left/right (west/east) on the map, ranging from `0.0` (the furthest left) to `1.0` (the furthest right). The `y` axis is down/up (south/north) on the map, ranging from `0.0` (the furthest down) to `1.0` (the furthest up).

A `map_2d` coordinate pair can be converted to a `lat_lon` coordinate pair, and vice versa.

### `street`: Street Coordinates

This is a coordinate system abstractly describing a point on one of the illuminated streets on the physical map. It consists of a street segment ID and a one-dimensional coordinate, `z`, ranging from `0.0` to `1.0` on that segment. Which side is `0` and which is `1` is determined by the order of the node IDs in the street segment's representation; `0.0` corresponds to the position of `nodes[0]` and `1.0` corresponds to the position of `nodes[1]`.

## Conversion

A `lat_lon` coordinate pair can be converted to a `map_2d` coordinate pair, and vice versa.

A `map_2d` coordinate pair does not always map cleanly to `street` coordinates -- consider a coordinate pair lying far from any of the illuminated streets. A `street` coordinate pair may be converted injectively to a `map_2d` coordinate pair, but to convert in the other direction, the best that can be done is returning the coordinates of the closest `street` position(s), of which there may be multiple with the same distance, and the distance from that street.

A `street` coordinate may be lossily converted to an LED ID by rounding it to the nearest LED.