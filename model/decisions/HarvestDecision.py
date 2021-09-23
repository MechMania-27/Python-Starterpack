from model.Position import Position
from model.decisions.ActionDecision import ActionDecision

class HarvestDecision(ActionDecision):
    def __init__(self, pos: Position) -> None:
        self.position = pos
    
    def __str__(self) -> str:
        return "HarvestDecision"

    def engine_str(self) -> str:
        return f"harvest {str(self.position)}"
