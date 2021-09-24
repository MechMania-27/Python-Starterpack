from typing import List
from model.tile_type import TileType
from model.game_state import GameState
from model.player import Player
from model.position import Position
from api.constants import Constants

import sys

constants = Constants()


def valid_position(pos: Position) -> bool:
    """
    Returns if a location is valid (on the board)
    :param pos:
    :param game_state:
    :return:
    """
    return pos.x >= 0 and pos.x < constants.BOARD_WIDTH and pos.y >= 0 and pos.y < constants.BOARD_HEIGHT


def distance(pos1: Position, pos2: Position) -> int:
    """
    Returns the Manhattan distance between two Position objects
    :param pos1: position 1
    :param pos2: position 2
    :return: Manhattan distance
    """
    return abs(pos1.x - pos2.x) + abs(pos1.y - pos2.y)


def get_player_from_name(game_state: GameState, name: str) -> Player:
    """
    Get the player representing the name given a game state
    :param game_state: GameState containing information for the game
    :param name: name to check
    :return: Player object for that name
    """
    return game_state.player1 if game_state.player1.name == name else game_state.player2


def within_move_range(game_state: GameState, name: str) -> List[Position]:
    """
    Returns all tiles for which player of input name can go to
    :param game_state: GameState containing information for the game
    :param name: Name of player to get
    :return: List of positions that the player can move to
    """
    my_player = get_player_from_name(game_state, name)
    speed = my_player.max_movement
    res = []

    for i in range(my_player.position.y - speed, my_player.position.y + speed):
        leftover_travel = max(0, speed - abs(my_player.position.y - i));
        for j in range(my_player.position.x - leftover_travel, my_player.position.x + leftover_travel):
            pos = Position(j, i)
            if valid_position(pos):
                res.append(pos)
    return res


def within_harvest_range(game_state: GameState, name: str) -> List[Position]:
    """
    Returns all tiles for which player of input name can go to
    :param game_state: GameState containing information for the game
    :param name: Name of player to get
    :return: List of positions that the player can harvest
    """
    my_player = get_player_from_name(game_state, name)
    radius = my_player.harvest_radius
    res = []

    for i in range(my_player.position.y - radius, my_player.position.y + radius + 1):
        for j in range(my_player.position.x - radius, my_player.position.x + radius + 1):
            pos = Position(j, i)
            if distance(my_player.position, pos) <= my_player.harvest_radius and valid_position(pos):
                res.append(pos)
    return res


def tile_type_on_turn(turn: int, game_state: GameState, coord: Position) -> TileType:
    """
    Get the type of the tile on given turn. This is useful for figuring out whether
    you should plant a crop now or later.
    :param turn: Turn to check for
    :param game_state: GameState containing information for the game
    :param coord: Coordinate to check at
    :return: TileType corresponding to the tile type of the tile given by coord
    """
    shifts = (turn - 1 - constants.F_BAND_INIT_DELAY) / constants.F_BAND_MOVE_DELAY;
    shifts = max(0, shifts);

    row = coord.y
    newType = TileType.ARID

    # Offset records how far into the fertility zone a row is (negative indicates below)
    # Init position indicates the first row that will * become * part of a band after the first shift
    # e.g. 0 = > fertility band starts off the map while 1 = > fertility band starts with 1 row on the map int
    offset = shifts - row - 1 + constants.F_BAND_INIT_POSITION;
    if (offset < 0):
        # Below fertility band
        newType = TileType.SOIL
    elif offset < constants.F_BAND_OUTER_HEIGHT:
        # Within first outer band
        newType = TileType.F_BAND_OUTER
    elif offset < constants.F_BAND_OUTER_HEIGHT + constants.F_BAND_MID_HEIGHT:
        # Within first mid band
        newType = TileType.F_BAND_MID
    elif offset < constants.F_BAND_OUTER_HEIGHT + constants.F_BAND_MID_HEIGHT + constants.F_BAND_INNER_HEIGHT:
        # Within inner band
        newType = TileType.F_BAND_INNER
    elif offset < constants.F_BAND_OUTER_HEIGHT + 2 * constants.F_BAND_MID_HEIGHT + constants.F_BAND_INNER_HEIGHT:
        # Within second mid band
        newType = TileType.F_BAND_MID
    elif offset < 2 * constants.F_BAND_OUTER_HEIGHT + 2 * constants.F_BAND_MID_HEIGHT + constants.F_BAND_INNER_HEIGHT:
        # Within second outer band
        newType = TileType.F_BAND_OUTER
    else:
        # Above fertility bands
        newType = TileType.ARID

    return newType
