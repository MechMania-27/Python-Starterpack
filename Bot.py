import sys
import random
import time
from IO import receive_gamestate, send_decision, send_item, send_upgrade
from IO import Logger

logger = Logger()


def send_heartbeat() -> None:
    print("heartbeat")


def get_item() -> str:
    logger.info("Sending \"NONE\"")
    return "NONE"


def get_upgrade() -> str:
    logger.info("Sending \"NONE\"")
    return "NONE"


def get_move_decision(game_state) -> str:
    player_num = game_state['playerNum']

    try:
        logger.info(f"{game_state['feedback']=}")
    except KeyError as e:
        logger.info(f"no feedback in this game state: keys={game_state.keys()}")

    pos = game_state[f"p{player_num}"]["position"]
    logger.info(f"Currently at ({pos['x']},{pos['y']})")

    if random.random() < 0.5 and \
            (sum(game_state[f"p{player_num}"]["seedInventory"].values()) == 0 or
             len(game_state[f'p{player_num}']['harvestedInventory']) > 0):
        move = f"move {game_state['tileMap']['mapWidth'] // 2} {max(0, pos['y'] - 10)}"
    else:
        x = min(max(0, random.randint(pos['x'] - 7, pos['x'] + 7)), game_state["tileMap"]["mapWidth"] - 1)
        y = min(max(0, random.randint(pos['y'] - 7, pos['y'] + 7)), game_state["tileMap"]["mapHeight"] - 1)
        move = f"move {x} {y}"

    logger.info(f"Sending \"{move}\"")
    return move


def get_action_decision(game_state) -> str:
    player_num = game_state['playerNum']

    try:
        logger.info(f"{game_state['feedback']=}")
    except KeyError as e:
        logger.info(f"no feedback in this game state: keys={game_state.keys()}")

    logger.info(f"I am player {player_num}")

    pos = game_state[f"p{player_num}"]["position"]
    logger.info(f"Currently at ({pos['x']},{pos['y']}), Harvested: {game_state[f'p{player_num}']['harvestedInventory']}")

    crop = random.choice(["POTATO", "CORN", "GRAPE"])
    pos = game_state[f"p{player_num}"]["position"]
    if game_state[f"p{player_num}"]["seedInventory"][crop] > 0 and \
            game_state["tileMap"]["tiles"][pos["y"]][pos["x"]]["type"] != "GREEN_GROCER" and \
            game_state["tileMap"]["tiles"][pos["y"]][pos["x"]]["type"].startswith("F_BAND"):
        action = f"plant {crop} {pos['x']} {pos['y']}"
    elif game_state[f"p{player_num}"]["money"] >= 15 and \
            game_state["tileMap"]["tiles"][pos["y"]][pos["x"]]["type"] == "GREEN_GROCER":
        action = f"buy {crop} 1"
    else:
        harvest_radius = 1
        action = f"harvest"
        for x in range(max(0, pos['x'] - 1), min(pos['x'] + 1, game_state["tileMap"]["mapHeight"] - 1)):
            for y in range(max(0, pos['y'] - 1), min(pos['y'] + 1, game_state["tileMap"]["mapWidth"] - 1)):
                if abs(x - pos['x']) + abs(y - pos['y']) <= harvest_radius:
                    action += f" {x} {y}"
        if action == "harvest":
            action += f" {pos['x']} {pos['y']}"

    logger.info(f"Sending \"{action:.30s}\"")
    return action



if __name__ == "__main__":
    send_heartbeat()
    send_item(get_item())
    send_upgrade(get_upgrade())

    # all logging and errors should be redirected to sys.stderr
    # while all commands sent back to the game engine as decision should
    # be sent in stdout using print
    while True:
        start_time = time.perf_counter_ns()
        game_state = receive_gamestate()
        duration = time.perf_counter_ns() - start_time
        logger.info(f"Receiving game state 1 took {duration // 1e6} ms")

        start_time = time.perf_counter_ns()
        move_decision = get_move_decision(game_state)
        duration = time.perf_counter_ns() - start_time
        logger.info(f"Move decision took {duration // 1e6} ms")

        start_time = time.perf_counter_ns()
        send_decision(move_decision)
        duration = time.perf_counter_ns() - start_time
        logger.info(f"Send move decision took {duration // 1e6} ms")

        start_time = time.perf_counter_ns()
        game_state = receive_gamestate()
        duration = time.perf_counter_ns() - start_time
        logger.info(f"Receiving game state 2 took {duration // 1e6} ms")

        start_time = time.perf_counter_ns()
        action_decision = get_action_decision(game_state)
        duration = time.perf_counter_ns() - start_time
        logger.info(f"Action decision took {duration // 1e6} ms")

        start_time = time.perf_counter_ns()
        send_decision(action_decision)
        duration = time.perf_counter_ns() - start_time
        logger.info(f"Sending action decision took {duration // 1e6} ms")


