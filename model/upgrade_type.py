from enum import Enum

class UpgradeType(Enum):
    SCYTHE = 0
    LOYALTY_CARD = 1
    LONGER_LEGS = 2
    RABBITS_FOOT = 3
    SEED_A_PULT = 4
    SPYGLASS = 5
    BACKPACK = 6
    NONE = 7

    def __str__(self):
        return f"{self.name}"

    def engine_str(self):
        return f"{self.name}"

