from model.Position import Position
from model.CropType import CropType
from model.ItemType import ItemType
from model.UpgradeType import UpgradeType
from api.Constants import Constants


class Player:
    constants = Constants()

    def __init__(self, player_dict) -> None:
        self.name = player_dict['name']
        self.position = Position(0, 0).from_dict(player_dict['position'])
        self.upgrade = UpgradeType[player_dict['upgrade']]
        self.item = ItemType[player_dict['item']]
        self.money = player_dict['money']
        self.seed_inventory = {CropType[k]:v for k,v in player_dict['seedInventory'].items()}
        
        self.harvested_inventory = player_dict['harvestedInventory']

        self.discount = player_dict['discount']
        self.protection_radius = player_dict['protectionRadius']
        self.harvest_radius = player_dict['harvestRadius']
        self.plant_radius = player_dict['plantRadius']
        self.carring_capacity = player_dict['carryingCapacity']
        self.max_movement = player_dict['maxMovement']
        self.double_drop_chance = player_dict['doubleDropChance']
        self.used_item = player_dict['usedItem']
        self.has_delivery_drone = player_dict['hasDeliveryDrone']
        self.has_coffee_thermos = player_dict['hasCoffeeThermos']
        self.item_time_expired = player_dict['itemTimeExpired']

        self.max_movement = constants.LONGER_LEGS_MAX_MOVEMENT if self.upgrade is UpgradeType.LONGER_LEGS \
            else Player.constants.MAX_MOVEMENT
        self.harvest_radius = constants.LONGER_SCYTHE_HARVEST_RADIUS if self.upgrade is UpgradeType.LONGER_SCYTHE \
            else Player.constants.HARVEST_RADIUS
