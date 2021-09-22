from enum import Enum

class CropType(Enum):
    GRAPE = 1
    CORN = 2
    POTATO = 3
    JOGAN_FRUIT = 4
    PEANUT = 5
    QUADROTRITICALE = 6
    DUCHAM_FRUIT = 7
    GOLDEN_CORN = 8
    NONE = 9

    def __str__(self):
        return f"{self.name}"

    def engine_str(self):
        return f"{self.name}"
