import sys
import random
import time
from IO import receive_gamestate
from IO import Logger
from Game import Game
import model.Position
from model.decisions.MoveDecision import move_decision
from model.decisions.ActionDecision import action_decision

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
    print("heartbeat")
    game = Game("NONE", "NONE")
    
    while (True) :
        try :
            game.update_game()
        except IOError:
            exit(-1)
        game.send_move_decision(get_move_decision(game))
        game.send_action_decision(get_move_decision(game))

