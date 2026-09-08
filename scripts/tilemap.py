class Tilemap:
    def __init__(self, tile_size=16):
        self.tile_size = tile_size
        self.tilemap = {}
        self.offgrid_tiles = []

        for i in range(10):
            self.tilemap[str(3+i)+";10"] = {'type': 'grass', 'variant':1, 'pis': (3+i, 10)}
            self.tilemap["10;"+str(5+i)] = {'type': 'stone', 'variant':1, 'pis': (10, 5+i)}