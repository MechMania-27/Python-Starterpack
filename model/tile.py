from model.item_type import ItemType
from model.tile_type import TileType
from model.crop import Crop
class Tile:
    def __init__(self, tile_dict) -> None:
        self.type = TileType[tile_dict['type']]
        self.crop = Crop(tile_dict['crop'])
        self.p1_item = ItemType[tile_dict['p1_item']]
        self.p1_item = ItemType[tile_dict['p2_item']]
        self.turns_left_to_grow = tile_dict['turnsLeftToGrow']
        self.rain_totem_effect = tile_dict['rainTotemEffect']
        self.fertility_idol_effect = tile_dict['fertilityIdolEffect']
        self.scarecrow_effect = tile_dict['scarecrowEffect']