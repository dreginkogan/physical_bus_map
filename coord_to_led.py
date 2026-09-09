import json

with open('nodes.json') as f:
    nodes_dict = json.load(f)

with open('segments.json') as f:
    segments_dict = json.load(f)

with open('routes.json') as f:
    routes_dict = json.load(f)

def distance(a_coord, b_coord):
    #technically returns dist squared but oh well
    return (a_coord[0] - b_coord[0])**2 + (a_coord[1] - b_coord[1])

def coords_to_led(rt: str, dir: str, lat: float, lon: float):
    #TODO: make it so something like 3 or 5 or whatever adjacent leds can be returned,
    # that amount of leds will make the bus location more readable

    segments_list = routes_dict["ROUTES"][rt][dir]
    color = routes_dict["ROUTES"][rt]["COLOR"]

    led_list = []
    coords_list = [] #interpolate values based on node coords
    leds_to_light = []

    for segment in segments_list:
        segment_leds = segments_dict[segment]["led_ids"]
        segment_length = len(segment_leds)

        segment_coords = []

        start_coords = (nodes_dict[segments_dict[segment]["start_node"]]["coordinates"][0],
                         nodes_dict[segments_dict[segment]["start_node"]]["coordinates"][1])

        end_coords = (nodes_dict[segments_dict[segment]["end_node"]]["coordinates"][0],
                         nodes_dict[segments_dict[segment]["end_node"]]["coordinates"][1])

        

        # can do this with much fewer lines and better and more efficient practices, will deal with later

        #TODO: make this inefficient mess better
        segment_coords.append(start_coords)

        lat_interval = (end_coords[0] - start_coords[0])/segment_length
        lon_interval = (end_coords[1] - start_coords[1])/segment_length

        for i in range(1, segment_length-1):
            segment_coords.append((start_coords[0] + lat_interval*i, start_coords[1] + lon_interval*i))

        segment_coords.append(end_coords)
        coords_list = list(set(coords_list + segment_coords))
        led_list = list(set(led_list + segment_leds))

    min_diff, res = float('inf'), None
    for idx, coord in enumerate(coords_list):
        if distance((lat, lon), coord) < min_diff:
            min_diff = distance((lat, lon), coord)
            res = idx

    nearest_led = led_list[res]

    leds_to_light.append(nearest_led) # so i can expand the number of leds i return

    return leds_to_light, color