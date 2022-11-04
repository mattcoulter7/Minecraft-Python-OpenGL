from pyglet.gl import *
from pyglet.window import key
import math

from player import Player
from block import Block
from chunk import Chunk
from vector3d import Vector3D

class Game:
    def __init__(self):
        self.player = Player(self,Vector3D(0.5,1.5,1.5),(-30,0))
        self.chunks = []
        self.batch = pyglet.graphics.Batch()
        self.chunk_size = 16
        self.render_distance = 3
        self.gravity = -9.8

    def get_chunk_from_pos(self,pos):
        chunk = list(filter(lambda c: c.fits_pos(pos),self.chunks))
        if (len(chunk) == 0):
            chunk = self.add_chunk(pos)
        else:
            chunk = chunk[0]
        return chunk

    def add_chunk(self,pos):
        chunk_pos = pos.round_to(self.chunk_size)
        chunk = Chunk(self,chunk_pos)
        self.chunks.append(chunk)
        return chunk

    def add_block(self,type,pos):
        chunk = self.get_chunk_from_pos(pos)
        chunk.blocks.append(Block(self,chunk,pos,type))

    def update(self,dt,keys):
        self.player.update(dt,keys)

    def draw(self):
        self.batch.draw()
        for chunk in self.chunks:
            if chunk.in_render_distance(self.player.pos):
                chunk.draw()