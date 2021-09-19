from model.decisions.ActionDecision import action_decision


import ActionDecision
from Position import position
class use_item_decision(ActionDecision.action_decision):
    def __init__(self, item: str, pos: position) -> None:
        self.pos = pos

    def __str__(self) -> str:
        return f"use_item"