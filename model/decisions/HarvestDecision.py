from Position import position
from ActionDecision import ActionDecision

class HarvestDecision(ActionDecision):
    def __init__(self, pos: position) -> None:
        self.position = position
    
    def __str__(self) -> str:
        return "HarvestDecision"

    def engine_str(self) -> str:
        return f"harvest {str(self.position)}"
