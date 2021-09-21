class Crop:
    def __init__(self, crop_dict) -> None:
        self.type = crop_dict['type']
        self.growth_timer = crop_dict['growthTimer']
        self.value = crop_dict['value']