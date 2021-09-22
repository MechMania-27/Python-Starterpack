from ActionDecision import ActionDecision


class BuyDecision(ActionDecision):

    def __init__(self, crop_types: list, quantities: list) -> None:
        assert(len(crop_types) == len(quantities))
        self.crop_types = crop_types
        self.quantities = quantities

    def engine_str(self) -> str:
        return "do_nothing "

    def __str__(self) -> str:
        return f"DoNothingDecision"
