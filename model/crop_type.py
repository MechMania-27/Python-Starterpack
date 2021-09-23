from enum import Enum
from pathlib import Path
import os
import configparser

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

    def __init__(self, *args, **kwargs):
        with open(Path(os.path.dirname(os.path.dirname(__file__))) / "resources" / "mm27.properties") as f:
            file_content = '[dummy_section]\n' + f.read()
        config_parser = configparser.RawConfigParser()
        config_parser.read_string(file_content)
        self.config = config_parser['dummy_section']

    def __str__(self):
        return f"{self.name}"

    def engine_str(self):
        return f"{self.name}"

    def get_seed_price(self) -> float:
        return float(self.config[f"croptype.{self.name.lower()}.seedprice"])

    def get_growth_time(self) -> int:
        return int(self.config[f"croptype.{self.name.lower()}.growthtime"])

    def get_fertility_sensitivity(self) -> float:
        return float(self.config[f"croptype.{self.name.lower()}.fertilitysens"])

    def get_growth_value(self) -> float:
        return float(self.config[f"croptype.{self.name.lower()}.growthvalue"])

