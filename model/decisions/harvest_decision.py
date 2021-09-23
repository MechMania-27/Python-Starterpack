from model.position import Position
from model.decisions.action_decision import ActionDecision
from typing import List


class HarvestDecision(ActionDecision):
    def __init__(self, positions: List[Position]) -> None:
        self.positions = positions
    
    def __str__(self) -> str:
        res = "HarvestDecision("
        for i in range(len(self.positions)):
            res += f"({self.positions[i].x},{self.positions[i].y})"
            res += ","
        if len(self.positions) > 0:
            res = res[:-1]
        res += ")"
        return res

    def engine_str(self) -> str:
        res = "harvest "
        for i in range(len(self.positions)):
            res += self.positions[i].engine_str()
            res += " "
        if len(self.positions) > 0:
            res = res[:-1]
        return res
