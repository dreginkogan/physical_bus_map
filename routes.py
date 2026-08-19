from enum import Enum

class Route(Enum):
    BUS_9  = "9"  #  9 McCandless-Oakland
    BUS_54 = "54" # 54 North Side-Oakland-South Side
    BUS_64 = "64" # 64 Millvale-Homestead
    BUS_81 = "81" # 81 Mercy Hospital-Oakland-Lawrenceville
    BUS_86 = "86" # 86 Liberty
    BUS_87 = "87" # 87 Friendship
    BUS_88 = "88" # 88 Penn

routes = [
    Route.BUS_54,
    Route.BUS_64,
    Route.BUS_86,
    Route.BUS_87,
    Route.BUS_88,
]