from model.decisions.action_decision import ActionDecision
from model.decisions.move_decision import MoveDecision

class BuyDecision(ActionDecision):

    def __init__(self, crop_types: list, quantities: list) -> None:
        assert(len(crop_types) == len(quantities))
        self.crop_types = crop_types
        self.quantities = quantities

    def engine_str(self) -> str:
        res = f"buy "
        for i in range(len(self.crop_types)):
            res += str(self.crop_types[i])
            res += " "
            res += str(self.quantities[i])
            res += " "
        if len(self.crop_types) > 0:
            res = res[:-1]
        return res

    def __str__(self) -> str:
        res = "BuyDecision("
        for i in range(len(self.crop_types)):
            res += str(self.crop_types[i])
            res += ":"
            res += str(self.quantities[i])
            res += ","
        if len(self.crop_types) > 0:
            res = res[:-1]
        res += ")"
        return res
