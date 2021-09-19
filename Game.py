import json
import IO
import api.Config


class Game:

    def __init__(self, item, upgrade):
        self.send_item(str(item))
        self.send_upgrade(str(upgrade))
        

    def update_game(self):
        self.game_state = IO.receive_gamestate()
        

    def send_move_decision(self, decision: str) -> None:
        IO.send_string(decision)

    def send_action_decision(self, decision: str) -> None:
        IO.send_string(decision)


    def send_item(self, item: str) -> None:
        IO.send_string(item)


    def send_upgrade(self, upgrade: str) -> None:
        IO.send_string(upgrade)



        

    # def get_player_num(self) -> str:
    #     return self.game_state['playerNum']

    # def get_player_pos(self, player_num) -> tuple(int, int):
    #     pos = self.game_state[f"p{player_num}"]["position"]
    #     return pos['x'], pos['y']

    # def get_board_size(self) -> tuple(int, int):
    #     return self.game_state["tileMap"]["mapWidth"], self.game_state["tileMap"]["mapHeight"]

    # def get_tile(self, x, y) -> dict:
    #     return self.game_state["tileMap"]["tiles"][f"{y}"][f"{x}"]

    # def get_tile_crops(self, x, y) -> dict:
    #     return self.game_state["tileMap"]["tiles"][f"{y}"][f"{x}"]["crops"]

    # api functions
    def possible_positions(self):
        pass

    def get_tile_type_after_z_turns(self, x, y, z):
        pass
