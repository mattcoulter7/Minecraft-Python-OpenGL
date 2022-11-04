from pyglet.gl import *
from pyglet.window import key
import math
import numpy

from entity import Entity
from collider import Collider,CollisionBox

class Player(Entity):
    def __init__(self, game, pos=(0, 0, 0), rot=(0, 0)):
        super().__init__(game, pos,(1,2,1))
        self.rot = list(rot)
        self.force = list

    def mouse_motion(self, dx, dy):
        dx /= 8
        dy /= 8
        self.rot[0] += dy
        self.rot[1] -= dx
        if self.rot[0] > 90:
            self.rot[0] = 90
        elif self.rot[0] < -90:
            self.rot[0] = -90

    def get_collision_objects(self):
        current_chunk = self.game.get_chunk_from_pos(self.pos)
        return list(filter(lambda b: Collider.intersect(self.collision_box,b.collision_box),current_chunk.blocks))
        if len(colliding_blocks) > 0:
            print(colliding_blocks)

    def update(self, dt, keys):
        colliding = self.get_collision_objects()
        s = dt*10
        rotY = -self.rot[1]/180*math.pi
        dx, dz = s*math.sin(rotY), s*math.cos(rotY)

        if keys[key.W]:
            self.pos.x += dx
            self.pos.z -= dz
        if keys[key.S]:
            self.pos.x -= dx
            self.pos.z += dz
        if keys[key.A]:
            self.pos.x -= dz
            self.pos.z -= dx
        if keys[key.D]:
            self.pos.x += dz
            self.pos.z += dx
        if keys[key.SPACE]:
            self.pos.y += s
        if keys[key.LSHIFT]:
            if (len(list(filter(lambda b: b.pos.y + 1 <= self.pos.y,colliding))) == 0):
                self.pos.y -= s
