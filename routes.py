from enum import Enum
from dataclasses import dataclass

class RouteNumber(Enum):
    BUS_9  = "9"  #  9 McCandless-Oakland
    BUS_54 = "54" # 54 North Side-Oakland-South Side
    BUS_64 = "64" # 64 Millvale-Homestead
    BUS_81 = "81" # 81 Mercy Hospital-Oakland-Lawrenceville
    BUS_86 = "86" # 86 Liberty
    BUS_87 = "87" # 87 Friendship
    BUS_88 = "88" # 88 Penn

@dataclass
class DirectionalRouteNumber:
    route: RouteNumber
    is_outbound: bool