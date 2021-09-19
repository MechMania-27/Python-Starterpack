from Position import position
import ActionDecision
class harvest_decision(ActionDecision.action_decision):
    def __init__(self, pos: position) -> None:
        self.position = position
    
    def __str__(self) -> str:
        return f"harvest {str(self.position)}"