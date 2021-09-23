from model.decisions.action_decision import ActionDecision


class DoNothingDecision(ActionDecision):

    def __init__(self) -> None:
        pass

    def engine_str(self) -> str:
        return "do_nothing "

    def __str__(self) -> str:
        return f"DoNothingDecision()"
