from api.Constants import Constants
import json
from model.GameState import GameState
import IO
from model.ItemType import ItemType
from model.UpgradeType import UpgradeType
from model.decisions.MoveDecision import MoveDecision
from model.decisions.ActionDecision import ActionDecision


class Game:
    logger = IO.Logger()

    def __init__(self, item: ItemType, upgrade: UpgradeType):
        IO.send_heartbeat()
        self.send_item(item)
        self.send_upgrade(upgrade)
 
        self.constants = Constants()

    def update_game(self) -> None:
        self.game_state = IO.receive_gamestate()

    def get_game_state(self) -> GameState:
        return self.game_state

    def send_move_decision(self, decision: MoveDecision) -> None:
        IO.send_string(decision.engine_str())

    def send_action_decision(self, decision: ActionDecision) -> None:
        IO.send_string(decision.engine_str())

    def send_item(self, item: ItemType) -> None:
        IO.send_string(item.engine_str())

    def send_upgrade(self, upgrade: UpgradeType) -> None:
        IO.send_string(upgrade.engine_str())
