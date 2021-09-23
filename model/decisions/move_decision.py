from model.position import Position


class MoveDecision:
    def __init__(self, pos: Position) -> None:
        self.pos = pos

    def __str__(self) -> str:
        return f"MoveDecision({self.pos})"

    def engine_str(self) -> str:
        return f"move {self.pos.engine_str()}"
