from model.Position import Position
class Player:
    def __init__(self, player_dict) -> None:
        self.position = Position(pos_dict=player_dict['position'])
        self.upgrade = player_dict['upgrade']
        self.money = player_dict['money']
        self.seed_inventory = player_dict['seedInventory']
        self.harvested_inventory = player_dict['harvestedInventory']
        self.discount = player_dict['discount']
        self.protection_radius = player_dict['protectionRadius']
        self.harvest_radius = player_dict['harvestRadius']
        self.plant_radius = player_dict['plantRadius']
        self.carring_capacity = player_dict['carryingCapacity']
        self.max_movement = player_dict['maxMovement']
        self.double_drop_chance = player_dict['doubleDropChance']
        self.used_item = player_dict['doubleDropChance']
        self.used_item = player_dict['usedItem']
        self.has_delivery_drone = player_dict['hasDeliveryDrone']
        self.has_coffee_thermos = player_dict['hasCoffeeThermos']
        self.item_time_expired = player_dict['itemTimeExpired']
