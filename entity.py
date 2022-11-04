from collider import CollisionBox
from vector3d import Vector3D
class Entity:
    def __init__(self,game,pos,widths=(0,0,0)):
        self.game = game
        self.pos = pos
        self.widths = list(widths)
        self.collision_box = CollisionBox(self.pos,self.widths)

    def draw(self):
        pass