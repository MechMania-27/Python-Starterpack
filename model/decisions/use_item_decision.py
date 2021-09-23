from model.decisions.action_decision import ActionDecision
from model.position import Position

class UseItemDecision(ActionDecision):
    def __init__(self, pos: Position) -> None:
        self.pos = pos

    def __str__(self) -> str:
        return "UseItemDecision()"

    def engine_str(self) -> str:
        return f"use_item"
