from IO import Logger
from Game import Game
from model.Position import Position
from model.decisions.MoveDecision import MoveDecision
from model.decisions.ActionDecision import ActionDecision
from model.decisions.BuyDecision import BuyDecision
from model.decisions.HarvestDecision import HarvestDecision
from model.decisions.PlantDecision import PlantDecision
from model.decisions.UseItemDecision import UseItemDecision
from model.decisions.DoNothingDecision import DoNothingDecision
from model.TileType import TileType
from model.ItemType import ItemType
from model.CropType import CropType
from model.UpgradeType import UpgradeType
from model.GameState import GameState
from api.Constants import Constants

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

    if random.random() < 0.5 and \
            (sum(my_player.seed_inventory.values()) == 0 or
             len(my_player.harvested_inventory)):
        decision = MoveDecision(Position(constants.BOARD_WIDTH // 2, max(0, pos.y - constants.MAX_MOVEMENT)))
    else:
        x = min(max(0, random.randint(pos.x - 7, pos.x + 7)), constants.BOARD_WIDTH - 1)
        y = min(max(0, random.randint(pos.y - 7, pos.y + 7)), constants.BOARD_HEIGHT - 1)
        decision = MoveDecision(Position(x, y))

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
    crop = random.choice(list(CropType))
    if my_player.seed_inventory[crop] > 0 and \
        game_state.tile_map.get_tile(pos.x, pos.y).type != TileType.GREEN_GROCER and \
        game_state.tile_map.get_tile(pos.x, pos.y).type.value >= TileType.F_BAND_OUTER.value:
        decision = PlantDecision([crop], [pos])
    elif my_player.money >= crop.get_seed_price() and \
        game_state.tile_map.get_tile(pos.x, pos.y).type == TileType.GREEN_GROCER:
        decision = BuyDecision([crop], [1])
    else:
        harvest_radius = 1
        locations = []
        for x in range(max(0, pos.x - 1), min(pos.x + 1, constants.BOARD_WIDTH - 1)):
            for y in range(max(0, pos.y - 1), min(pos.y + 1, constants.BOARD_HEIGHT - 1)):
                if abs(x - pos.x) + abs(y - pos.y) <= harvest_radius:
                    locations.append(Position(x, y))
        decision = HarvestDecision(locations)
    logger.debug(f"[Turn {game_state.turn}] Sending ActionDecision: {decision}")
    return decision


def main():
    """
    Competitor TODO: choose an item and upgrade for your bot
    """
    game = Game(ItemType.NONE, UpgradeType.NONE)

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
