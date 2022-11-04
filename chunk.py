from pyglet.gl import *
from pyglet.window import key
from entity import Entity
import math

from vector3d import Vector3D

class Chunk:
    def __init__(self,game,pos):
        self.game = game
        self.pos = pos
        self.blocks = []
        self.batch = pyglet.graphics.Batch()

    def add_block(self,block):
        self.blocks.append(block)

    def fits_pos(self,pos):
        return ((pos.x >= self.pos.x and pos.x < self.pos.x + self.game.chunk_size) and 
                (pos.y >= self.pos.y and pos.y < self.pos.y + self.game.chunk_size) and 
                (pos.z >= self.pos.z and pos.z < self.pos.z + self.game.chunk_size))

    def in_render_distance(self,pos):
        # distance to chunk is within render distance
        to_pos = pos - self.pos 
        return (to_pos.magnitude() / self.game.chunk_size) <= self.game.render_distance

    def draw(self):
        self.batch.draw()