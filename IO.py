from model.GameState import GameState
from types import SimpleNamespace as Namespace
import sys
import json



# def oh(d):
#     Logger().debug("**entris:" + str(**d))
#     return GameState(**d)

def receive_gamestate():
    gamestate_bytes = sys.stdin.readline()
    gamestate_dict = json.loads(gamestate_bytes)
    a = GameState(gamestate_dict)
    Logger().debug(str((a.tile_map.tiles[10][10].type)))
    return a


def readline() -> str:
    return sys.stdin.readline()

def send_string(str : str):
    print(str)

def send_heartbeat():
    print("heartbeat")
class Logger:
    def __init__(self) -> None:
        pass

    def info(self, message: str) -> None:
        print(f"info: {message}", file=sys.stderr, flush=True)

    def debug(self, message: str) -> None:
        print(f"debug: {message}", file=sys.stderr, flush=True)
