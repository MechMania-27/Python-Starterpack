import sys
import json


def receive_gamestate():
    gamestate_bytes = sys.stdin.readline()
    return json.loads(gamestate_bytes)


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
