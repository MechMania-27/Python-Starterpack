from model.tile import Tile

class TileMap:
    def __init__(self, tilemap_dict) -> None:
        self.map_height = tilemap_dict['mapHeight']
        self.map_width = tilemap_dict['mapWidth']
        self.tiles = [] 
        for row_list in tilemap_dict['tiles']:
            tile_row = []
            for tile in row_list:
                tile_row.append(Tile(tile))
            self.tiles.append(tile_row)
        
    def get_tile(self, x: int, y: int) -> Tile:
        return self.tiles[y][x]