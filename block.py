from pyglet.gl import *
from pyglet.window import key
from entity import Entity
import math

from entity import Entity
from collider import Collider,CollisionBox

BLOCK_BASE_DIR = "entities\\blocks\\"
LOADED_TEXTURES = dict()


class Block(Entity):
    def __init__(self, game, chunk, pos, type):
        super().__init__(game, pos,(1,1,1))
        self.chunk = chunk
        self.type = type
        self.textures = BlockTextures(type)
        self.init_textures()

    def init_textures(self):
        tex_coords = ('t2f', (0, 0, 1, 0, 1, 1, 0, 1, ))
        textures = self.textures.get_textures()
        for side, tex in textures.items():
            self.chunk.batch.add(4, GL_QUADS, tex, ('v3f', self.textures.get_texture_pos(
                self.pos, side)
            ), tex_coords)

    def draw(self):
        pass


class BlockTextures:
    def __init__(self, type):
        dirs = BLOCKS.get(type)
        for key, val in dirs.items():
            setattr(self, key, val)

    @property
    def front(self):
        try:
            return self._front
        except AttributeError:
            return self.side

    @front.setter
    def front(self, val):
        self._front = val

    @property
    def right(self):
        try:
            return self._right
        except AttributeError:
            return self.side

    @right.setter
    def right(self, val):
        self._right = val

    @property
    def left(self):
        try:
            return self._left
        except AttributeError:
            return self.side

    @left.setter
    def left(self, val):
        self._left = val

    @property
    def top(self):
        try:
            return self._top
        except AttributeError:
            return self.side

    @top.setter
    def top(self, val):
        self._top = val

    @property
    def bottom(self):
        try:
            return self._bottom
        except AttributeError:
            return self.side

    @bottom.setter
    def bottom(self, val):
        self._bottom = val

    @property
    def back(self):
        try:
            return self._back
        except AttributeError:
            return self.side

    @back.setter
    def back(self, val):
        self._back = val

    def get_textures(self):
        return {
            "front": self.get_texture(self.front),
            "right": self.get_texture(self.right),
            "left": self.get_texture(self.left),
            "top": self.get_texture(self.top),
            "bottom": self.get_texture(self.bottom),
            "back": self.get_texture(self.back),
        }

    def get_texture(self, file):
        if file in LOADED_TEXTURES:
            # no need to reload the same texture
            return LOADED_TEXTURES.get(file)
        pyg_file = pyglet.image.load(BLOCK_BASE_DIR + file)
        tex = pyg_file.get_texture()
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        texture_group = pyglet.graphics.TextureGroup(tex)
        LOADED_TEXTURES[file] = texture_group
        return texture_group

    def get_texture_pos(self, pos, side):
        x, y, z = pos.list
        X, Y, Z = x+1, y+1, z+1
        if side == "front":
            return (x, y, z, x, y, Z, x, Y, Z, x, Y, z)
        if side == "right":
            return (X, y, Z, X, y, z, X, Y, z, X, Y, Z)
        if side == "top":
            return (x, Y, Z, X, Y, Z, X, Y, z, x, Y, z)
        if side == "bottom":
            return (x, y, z, X, y, z, X, y, Z, x, y, Z)
        if side == "left":
            return (X, y, z, x, y, z, x, Y, z, X, Y, z)
        if side == "back":
            return (x, y, Z, X, y, Z, X, Y, Z, x, Y, Z)


BLOCKS = {
    "dirt": {
        "side": "grass_block_side.png",
        "top": "grass_block_top.png",
        "bottom": "dirt.png"
    },
    "test": {
        "side": "test.png"
    }
}
