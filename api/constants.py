from pathlib import Path
import configparser
import os


class Constants:
    def __init__(self) -> None:
        with open(Path(os.path.dirname(os.path.dirname(__file__))) / "resources" / "mm27.properties") as f:
            file_content = '[dummy_section]\n' + f.read()
        config_parser = configparser.RawConfigParser()
        config_parser.read_string(file_content)
        config = config_parser['dummy_section']
        
        self.BOARD_WIDTH                            = int(config['board.width'])
        self.BOARD_HEIGHT                           = int(config['board.height'])
        self.GRASS_ROWS                             = int(config['board.grass.rows'])
        self.GREENGROCER_LENGTH                     = int(config['board.greengrocer.length'])
        self.FBAND_INNER_HEIGHT                     = int(config['fertilityband.inner.height'])
        self.FBAND_MID_HEIGHT                       = int(config['fertilityband.mid.height'])
        self.FBAND_OUTER_HEIGHT                     = int(config['fertilityband.outer.height'])
        self.FBAND_MOVE_DELAY                       = int(config['fertilityband.speed'])
        self.FBAND_INIT_DELAY                       = int(config['fertilityband.delay'])
        self.FBAND_INIT_POSITION                    = int(config['fertilityband.start'])

        self.CARRYING_CAPACITY                      = int(config['player.carrycapacity'])
        self.MAX_MOVEMENT                           = int(config['player.maxmovement'])
        self.PLANT_RADIUS                           = int(config['player.plantradius'])
        self.HARVEST_RADIUS                         = int(config['player.harvestradius'])
        self.PROTECTION_RADIUS                      = int(config['player.protectionradius'])
        self.STARTING_MONEY                         = int(config['player.startingmoney'])
        
        self.PLAYER_TIMEOUT                         = int(config['networking.timeout.player'])
        
        self.RAIN_TOTEM_GROWTH_MULTIPLIER           = int(config['item.rain_totem.growth_multiplier'])
        self.RAIN_TOTEM_EFFECT_RADIUS               = int(config['item.rain_totem.effect_radius'])
        self.FERTILITY_IDOL_FERTILITY_MULTIPLIER    = int(config['item.fertility_idol.fertility_multiplier'])
        self.FERTILITY_IDOL_EFFECT_RADIUS           = int(config['item.fertility_idol.effect_radius'])
        self.PESTICIDE_CROP_VALUE_DECREASE          = float(config['item.pesticide.crop_value_decrease'])
        self.PESTICIDE_EFFECT_RADIUS                = int(config['item.pesticide.effect_radius'])
        self.SCARECROW_EFFECT_RADIUS                = int(config['item.scarecrow.effect_radius'])
        self.COFFEE_THERMOS_MOVEMENT_MULTIPLIER     = int(config['items.coffee_thermos.movement_multiplier'])

        self.GREEN_GROCER_LOYALTY_CARD_DISCOUNT     = float(config['upgrades.green_grocer_loyalty_card_discount'])
        self.GREEN_GROCER_LOYALTY_CARD_MINIMUM      = float(config['upgrades.green_grocer_loyalty_card_minimum'])
        self.RABBITS_FOOT_DOUBLE_DROP_CHANCE        = float(config['upgrades.rabbits_foot_double_drop_chance'])
        self.LONGER_LEGS_MAX_MOVEMENT               = int(config['upgrades.longer_legs_max_movement'])
        self.SEED_A_PULT_PLANT_RADIUS               = int(config['upgrades.seed_a_pult_plant_radius'])
        self.SCYTHE_HARVEST_RADIUS                  = int(config['upgrades.scythe_harvest_radius'])
        self.BACKPACK_CARRYING_CAPACITY             = int(config['upgrades.backpack_carrying_capacity'])
        self.SPYGLASS_PROTECTION_RADIUS             = int(config['upgrades.spyglass_protection_radius'])
