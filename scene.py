from model import *
import glm
from level_editor import LevelEditor
from map_editor import MapEditor


class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.level_editor = LevelEditor()
        self.load()
        # skybox
        self.skybox = AdvancedSkyBox(app)

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object

        # Load level from .map file
        self.level_editor.load_map('/path/to/your/map/file.map')
        for position, asset_name in self.level_editor.grid.items():
            if asset_name == 'Cube':
                add(Cube(app, pos=position))
            elif asset_name == 'Cat':
                add(Cat(app, pos=position))

        # floor
        n, s = 20, 2
        for x in range(-n, n, s):
            for z in range(-n, n, s):
                add(Cube(app, pos=(x, -s, z)))

        # columns
        for i in range(9):
            add(Cube(app, pos=(15, i * s, -9 + i), tex_id=2))
            add(Cube(app, pos=(15, i * s, 5 - i), tex_id=2))

        # cat
        add(Cat(app, pos=(0, -1, -10)))

        # moving cube
        self.moving_cube = MovingCube(app, pos=(0, 6, 8), scale=(3, 3, 3), tex_id=1)
        add(self.moving_cube)

    def update(self):
        self.moving_cube.rot.xyz = self.app.time