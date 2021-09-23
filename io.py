from model.game_state import GameState
import sys
import json


def receive_gamestate():
    gamestate_bytes = sys.stdin.readline()
    gamestate_dict = json.loads(gamestate_bytes)
    a = GameState(gamestate_dict)
    return a

def readline() -> str:
    return sys.stdin.readline()

def send_string(s: str):
    print(s)

def send_heartbeat():
    print("heartbeat")


class Logger:
    def __init__(self) -> None:
        pass

    def info(self, message) -> None:
        print(f"info: {str(message)}", file=sys.stderr, flush=True)

    def debug(self, message: str) -> None:
        print(f"debug: {str(message)}", file=sys.stderr, flush=True)
