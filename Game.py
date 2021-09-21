import json
from model.GameState import GameState
import IO
import configparser

class Game:

    def __init__(self, item, upgrade):
        self.send_item(str(item))
        self.send_upgrade(str(upgrade))
        with open(r'E:\uiuc\Mechmania\Python-Starterpack\resources\mm27.properties') as f:
            file_content = '[dummy_section]\n' + f.read()
        config_parser = configparser.RawConfigParser()
        config_parser.read_string(file_content)
        config = config_parser['dummy_section']


        

    def update_game(self):
        self.game_state = IO.receive_gamestate()
        logger = IO.Logger()
        # logger.debug(str(self.game_state.__dict__))
        # logger.debug(str(self.game_state.))
        # logger.debug(str(self.game_state.p1.position.x))

                
        

    def send_move_decision(self, decision: str) -> None:
        IO.send_string(decision)

    def send_action_decision(self, decision: str) -> None:
        IO.send_string(decision)


    def send_item(self, item: str) -> None:
        IO.send_string(item)


    def send_upgrade(self, upgrade: str) -> None:
        IO.send_string(upgrade)
