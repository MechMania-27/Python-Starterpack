from model.game_state import GameState
from networking import io
from model.item_type import ItemType
from model import upgrade_type
from model.decisions.move_decision import MoveDecision
from model.decisions.action_decision import ActionDecision


class Game:

    def __init__(self, item: ItemType, upgrade: upgrade_type):
        io.send_heartbeat()
        self.send_item(item)
        self.send_upgrade(upgrade)

    def update_game(self) -> None:
        self.game_state = io.receive_gamestate()

    def get_game_state(self) -> GameState:
        return self.game_state

    def send_move_decision(self, decision: MoveDecision) -> None:
        io.send_string(decision.engine_str())

    def send_action_decision(self, decision: ActionDecision) -> None:
        io.send_string(decision.engine_str())

    def send_item(self, item: ItemType) -> None:
        io.send_string(item.engine_str())

    def send_upgrade(self, upgrade: upgrade_type) -> None:
        io.send_string(upgrade.engine_str())
