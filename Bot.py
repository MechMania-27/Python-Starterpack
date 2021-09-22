import sys
import random
import time
import configparser
from IO import receive_gamestate
from IO import Logger
from IO import send_heartbeat
from Game import Game
from model.Position import Position
from model.decisions.MoveDecision import MoveDecision
from model.decisions.ActionDecision import ActionDecision
from model.ItemType import ItemType
from model.UpgradeType import UpgradeType
from model.GameState import GameState
import api.Constants

logger = Logger()


def get_move_decision(game: Game) -> MoveDecision:
    """
    Returns a move decision for the turn given the current game state.
    This is part 1 of 2 of the turn.

    Remember, you can only sell crops once you get to a Green Grocer tile,
    and you can only harvest or plant within your harvest or plant radius.

    After moving (and submitting the move decision), you will be given a new
    game state with both players in their updated positions.

    @param game The object that contains the game state and other related information
    @return MoveDecision A location for the bot to move to this turn
    """
    game_state: GameState = game.get_game_state()
    logger.debug(f"[Turn {game_state.turn}] Feedback received from engine: [{game_state.feedback}]")

    decision = MoveDecision(Position(0, 0))
    logger.debug(f"[Turn {game_state.turn}] Sending MoveDecision: {decision}")
    return decision


def get_action_decision(game: Game) -> ActionDecision:
    """
    Returns an action decision for the turn given the current game state.
    This is part 2 of 2 of the turn.

    There are multiple action decisions that you can return here: BuyDecision,
    HarvestDecision, PlantDecision, or UseItemDecision.

    After this action, the next turn will begin.

    @param game The object that contains the game state and other related information
    @return ActionDecision A decision for the bot to make this turn
    """
    game_state: GameState = game.get_game_state()
    logger.debug(f"[Turn {game_state.turn}] Feedback received from engine: [{game_state.feedback}]")

    decision = DoNothingDecision()
    logger.debug(f"[Turn {game_state.turn}] Sending ActionDecision: {decision}")
    return decision


def main():
    """
    Competitor TODO: choose an item and upgrade for your bot
    """
    game = Game(ItemType.NONE, UpgradeType.NONE)

    while (True) :
        try :
            game.update_game()
        except IOError:
            exit(-1)
        game.send_move_decision(get_move_decision(game))
        game.send_action_decision(get_move_decision(game))


if __name__ == "__main__":
    main()
