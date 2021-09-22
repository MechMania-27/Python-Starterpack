from enum import Enum

class ItemType(Enum):
    RAIN_TOTEM = 1
    FERTILITY_IDOL = 2
    PESTICIDE = 3
    SCARECROW = 4
    DELIVERY_DRONE = 5
    COFFEE_THERMOS = 6
    NONE = 7

    def __str__(self):
        return f"{self.name}"

    def engine_str(self):
        return f"{self.name}"
