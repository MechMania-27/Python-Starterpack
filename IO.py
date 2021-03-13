import sys
import json


def receive_gamestate():
    gamestate_bytes = sys.stdin.readline()
    return json.loads(gamestate_bytes)


def send_decision(decision: str) -> None:
    print(decision)


def send_item(item: str) -> None:
    print(item)


def send_upgrade(upgrade: str) -> None:
    print(upgrade)


class Logger:
    def __init__(self) -> None:
        pass

    def info(self, message: str) -> None:
        print(f"info: {message}", file=sys.stderr, flush=True)

    def debug(self, message: str) -> None:
        print(f"debug: {message}", file=sys.stderr, flush=True)
