from PyQt5.QtWidgets import QMainWindow, QTableWidget, QComboBox, QFileDialog, QTableWidgetItem
from level_editor import LevelEditor

class MapEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.level_editor = LevelEditor()

        self.create_grid()
        self.create_tile_selector()

    def create_grid(self):
        self.grid = QTableWidget(10, 10, self)
        self.grid.cellClicked.connect(self.place_tile)

    def create_tile_selector(self):
        self.tile_selector = QComboBox(self)
        self.tile_selector.addItems(['Cube', 'Cat'])

    def place_tile(self, row, column):
        tile_type = self.tile_selector.currentText()
        self.level_editor.set_tile((row, column), tile_type)
        self.update_map()

    def save_map(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Map")
        if file_path:
            self.level_editor.save_map(file_path)

    def load_map(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Map")
        if file_path:
            self.level_editor.load_map(file_path)
            self.update_map()

    def update_map(self):
        for row in range(self.grid.rowCount()):
            for column in range(self.grid.columnCount()):
                tile_type = self.level_editor.get_tile((row, column))
                self.grid.setItem(row, column, QTableWidgetItem(tile_type))