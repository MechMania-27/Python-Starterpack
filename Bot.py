from os import add_dll_directory
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

logger = Logger()



def get_move_decision(game):
    return MoveDecision(Position(0, 0))

def get_action_decision(game):
    return ActionDecision()





if __name__ == "__main__":
    send_heartbeat()
    game = Game("NONE", "NONE")


    
    while (True) :
        try :
            game.update_game()
        except IOError:
            exit(-1)
        game.send_move_decision(get_move_decision(game))
        game.send_action_decision(get_move_decision(game))

