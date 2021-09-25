from model.position import Position
from model.crop_type import CropType
from model.item_type import ItemType
from model.upgrade_type import UpgradeType
from api.constants import Constants


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
