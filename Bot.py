import sys
import random
import time
from IO import receive_gamestate, send_decision, send_item, send_upgrade
from IO import Logger
import Game
import model.Position

logger = Logger()



def get_move_decision(game):
    return move_decision(model.Position.position(0, 1))

def get_action_decision(game):
    return action_decision()



# def crash_on_turn(curr_turn: int, turn: int) -> None:
#     if curr_turn == turn:
#         a = [1, 2, 3]
#         b = a[4]


if __name__ == "__main__":
    game = receive_gamestate
    
    while (True) :
        try :
            game.update_game()
        except IOError:
            exit(-1)
        game.sendMoveDecision(get_move_decision(game))
        game.sendActionDecision(get_move_decision(game))

