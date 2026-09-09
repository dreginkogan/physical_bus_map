import json

with open('nodes.json') as f:
    nodes_dict = json.load(f)

with open('segments.json') as f:
    segments_dict = json.load(f)

with open('routes.json') as f:
    routes_dict = json.load(f)

def distance(a_coord, b_coord):
    return (a_coord[0] - b_coord[0])**2 + (a_coord[1] - b_coord[1])**2

def coords_to_led(rt: str, dir: str, lat: float, lon: float):
    #TODO: make it so something like 3 or 5 or whatever adjacent leds can be returned,
    # that amount of leds will make the bus location more readable

    segments_list = routes_dict["ROUTES"][rt][dir]
    color = routes_dict["ROUTES"][rt]["COLOR"]

    coord_led_pairs = []
    leds_to_light = []

    for segment in segments_list:
        segment_leds = segments_dict[segment]["led_ids"]
        segment_length = len(segment_leds)

        start_coords = tuple(nodes_dict[segments_dict[segment]["start_node"]]["coordinates"])
        end_coords = tuple(nodes_dict[segments_dict[segment]["end_node"]]["coordinates"])

        segment_coords = [start_coords]

        lat_interval = (end_coords[0] - start_coords[0]) / segment_length
        lon_interval = (end_coords[1] - start_coords[1]) / segment_length

        for i in range(1, segment_length - 1):
            segment_coords.append((start_coords[0] + lat_interval * i,
                                    start_coords[1] + lon_interval * i))

        segment_coords.append(end_coords)

        # zip coords to their LED ids together, then dedupe the pairs as a unit
        segment_pairs = list(zip(segment_coords, segment_leds))
        coord_led_pairs = list(dict.fromkeys(coord_led_pairs + segment_pairs))

    min_diff, nearest_led = float('inf'), None
    for coord, led_id in coord_led_pairs:
        d = distance((lat, lon), coord)
        if d < min_diff:
            min_diff = d
            nearest_led = led_id

    leds_to_light.append(nearest_led)

    return leds_to_light, color