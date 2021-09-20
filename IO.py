from model.GameState import game_state
from types import SimpleNamespace as Namespace
import sys
import json




def receive_gamestate():
    gamestate_bytes = sys.stdin.readline()
    a = json.loads(gamestate_bytes, object_hook=lambda d: Namespace(**d))
    return a


def readline() -> str:
    return sys.stdin.readline()

def send_string(str : str):
    print(str)


class Logger:
    def __init__(self) -> None:
        pass

    def info(self, message: str) -> None:
        print(f"info: {message}", file=sys.stderr, flush=True)

    def debug(self, message: str) -> None:
        print(f"debug: {message}", file=sys.stderr, flush=True)
