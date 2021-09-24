from networking.io import Logger
from game import Game
from api import game_util
from model.position import Position
from model.decisions.move_decision import MoveDecision
from model.decisions.action_decision import ActionDecision
from model.decisions.buy_decision import BuyDecision
from model.decisions.harvest_decision import HarvestDecision
from model.decisions.plant_decision import PlantDecision
from model.decisions.do_nothing_decision import DoNothingDecision
from model.tile_type import TileType
from model.item_type import ItemType
from model.crop_type import CropType
from model.upgrade_type import UpgradeType
from model.game_state import GameState
from model.player import Player
from api.constants import Constants

import random

logger = Logger()
constants = Constants()


def get_move_decision(game: Game) -> MoveDecision:
    """
    Returns a move decision for the turn given the current game state.
    This is part 1 of 2 of the turn.

    Remember, you can only sell crops once you get to a Green Grocer tile,
    and you can only harvest or plant within your harvest or plant radius.

    After moving (and submitting the move decision), you will be given a new
    game state with both players in their updated positions.

    :param: game The object that contains the game state and other related information
    :returns: MoveDecision A location for the bot to move to this turn
    """
    game_state: GameState = game.get_game_state()
    logger.debug(f"[Turn {game_state.turn}] Feedback received from engine: {game_state.feedback}")

    # Select your decision here!
    my_player: Player = game_state.get_my_player()
    pos: Position = my_player.position
    logger.info(f"Currently at {my_player.position}")

    # If we have something to sell that we harvested, then try to move towards the green grocer tiles
    if random.random() < 0.5 and \
            (sum(my_player.seed_inventory.values()) == 0 or
             len(my_player.harvested_inventory)):
        logger.debug("Moving towards green grocer")
        decision = MoveDecision(Position(constants.BOARD_WIDTH // 2, max(0, pos.y - constants.MAX_MOVEMENT)))
    # If not, then move randomly within the range of locations we can move to
    else:
        pos = random.choice(game_util.within_move_range(game_state, my_player.name))
        logger.debug("Moving randomly")
        decision = MoveDecision(pos)

    logger.debug(f"[Turn {game_state.turn}] Sending MoveDecision: {decision}")
    return decision


def get_action_decision(game: Game) -> ActionDecision:
    """
    Returns an action decision for the turn given the current game state.
    This is part 2 of 2 of the turn.

    There are multiple action decisions that you can return here: BuyDecision,
    HarvestDecision, PlantDecision, or UseItemDecision.

    After this action, the next turn will begin.

    :param: game The object that contains the game state and other related information
    :returns: ActionDecision A decision for the bot to make this turn
    """
    game_state: GameState = game.get_game_state()
    logger.debug(f"[Turn {game_state.turn}] Feedback received from engine: {game_state.feedback}")

    # Select your decision here!
    my_player: Player = game_state.get_my_player()
    pos: Position = my_player.position
    # Let the crop of focus be the one we have a seed for, if not just choose a random crop
    crop = max(my_player.seed_inventory, key=my_player.seed_inventory.get) \
        if sum(my_player.seed_inventory.values()) > 0 else random.choice(list(CropType))

    # Get a list of possible harvest locations for our harvest radius
    possible_harvest_locations = []
    harvest_radius = my_player.harvest_radius
    for harvest_pos in game_util.within_harvest_range(game_state, my_player.name):
        if game_state.tile_map.get_tile(harvest_pos.x, harvest_pos.y).crop.value > 0:
            possible_harvest_locations.append(harvest_pos)

    logger.debug(f"Possible harvest locations={possible_harvest_locations}")

    # If we can harvest something, try to harvest it
    if len(possible_harvest_locations) > 0:
        decision = HarvestDecision(possible_harvest_locations)
    # If not but we have that seed, then try to plant it in a fertility band
    elif my_player.seed_inventory[crop] > 0 and \
            game_state.tile_map.get_tile(pos.x, pos.y).type != TileType.GREEN_GROCER and \
            game_state.tile_map.get_tile(pos.x, pos.y).type.value >= TileType.F_BAND_OUTER.value:
        logger.debug(f"Deciding to try to plant at position {pos}")
        decision = PlantDecision([crop], [pos])
    # If we don't have that seed, but we have the money to buy it, then move towards the
    # green grocer to buy it
    elif my_player.money >= crop.get_seed_price() and \
        game_state.tile_map.get_tile(pos.x, pos.y).type == TileType.GREEN_GROCER:
        logger.debug(f"Buy 1 of {crop}")
        decision = BuyDecision([crop], [1])
    # If we can't do any of that, then just do nothing (move around some more)
    else:
        logger.debug(f"Couldn't find anything to do, waiting for move step")
        decision = DoNothingDecision()

    logger.debug(f"[Turn {game_state.turn}] Sending ActionDecision: {decision}")
    return decision


def main():
    """
    Competitor TODO: choose an item and upgrade for your bot
    """
    game = Game(ItemType.COFFEE_THERMOS, UpgradeType.SCYTHE)

    while (True):
        try:
            game.update_game()
        except IOError:
            exit(-1)
        game.send_move_decision(get_move_decision(game))

        try:
            game.update_game()
        except IOError:
            exit(-1)
        game.send_action_decision(get_action_decision(game))


if __name__ == "__main__":
    main()
