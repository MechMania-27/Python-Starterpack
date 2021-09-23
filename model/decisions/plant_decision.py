from model.decisions.action_decision import ActionDecision


class PlantDecision(ActionDecision):
    def __init__(self, crop_types: list, coords: list) -> None:
        self.crop_types = crop_types
        self.coords = coords
        assert(len(crop_types) == len(coords))

    def __str__(self) -> str:
        res = f"PlantDecision("
        for i in range(len(self.crop_types)):
            res += str(self.crop_types[i])
            res += ":"
            res += str(self.coords[i])
            res += ","
        res = res[:-1]
        res += ")"
        return res

    def engine_str(self) -> str:
        res = f"plant "
        for i in range(len(self.crop_types)):
            res += str(self.crop_types[i])
            res += " "
            res += self.coords[i].engine_str()
            res += " "
        res = res[:-1]
        return res
