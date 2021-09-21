from ActionDecision import ActionDecision
class buy_action(ActionDecision):

    def __init__(self, crop_types: list, quantities: list) -> None:
        assert(len(crop_types) == len(quantities))
        self.crop_types = crop_types
        self.quantities = quantities

    def __str__(self) -> str:
        res = f"buy "
        for i in range(len(self.crop_types)):
            res += self.crop_types[i]
            res += " "
            res += str(self.quantities[i])
            res += " "
        res = res[:-1]
        return res
