from model.Position import position
class move_decision:
    def __init__(self, pos: position) -> None:
        self.pos = pos

    def __str__(self) -> str:
        return f"move {str(self.pos)}"