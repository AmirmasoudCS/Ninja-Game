class Tilemap:
    def __init__(self, tile_size=16):
        self.tile_size = tile_size
        self.tilemap = {}
        self.offgrid_tiles = []