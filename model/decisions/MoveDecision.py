from model.Position import Position


class MoveDecision:
    def __init__(self, pos: Position) -> None:
        self.pos = pos

    def __str__(self) -> str:
        return f"MoveDecision {str(self.pos)}"

    def engine_str(self) -> str:
        return f"move {str(self.pos)}"
