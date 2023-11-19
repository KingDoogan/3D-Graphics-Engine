from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

class LevelEditor:
    def __init__(self):
        self.grid = {}

    def get_tile(self, position):
        return self.grid.get(position, '')

    def set_tile(self, position, tile_type):
        self.grid[position] = tile_type

    def save_map(self, file_path):
        with open(file_path, 'w') as file:
            for position, tile_type in self.grid.items():
                file.write(f'{position[0]} {position[1]} {tile_type}\n')

    def load_map(self, file_path):
        with open(file_path, 'r') as file:
            self.grid = {}
            for line in file:
                x, y, tile_type = line.strip().split()
                self.grid[int(x), int(y)] = tile_type