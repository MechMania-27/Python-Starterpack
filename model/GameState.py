from model.Player import Player
from model.TileMap import TileMap
from types import GetSetDescriptorType


class GameState:
    def __init__(self, gamestate_dict) -> None:
        self.turn = gamestate_dict['turn']
        self.player1 = Player(gamestate_dict['p1'])
        self.player2 = Player(gamestate_dict['p2'])
        self.tile_map = TileMap(gamestate_dict['tileMap'])
