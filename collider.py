class Collider:
    def intersect(cubeA, cubeB):
        # Determining overlap in the x plane
        # Determining overlap in the y plane
        # Determining overlap in the z plane
        return cubeA.maxX > cubeB.minX and cubeA.minX < cubeB.maxX and cubeA.maxY > cubeB.minY and cubeA.minY < cubeB.maxY and cubeA.maxZ > cubeB.minZ and cubeA.minZ < cubeB.maxZ


class CollisionBox:
    def __init__(self, pos, widths):
        self.pos = pos
        self.widths = widths

    @property
    def minX(self):
        return self.pos.x

    @property
    def maxX(self):
        return self.pos.x + self.widths[0]

    @property
    def minY(self):
        return self.pos.y

    @property
    def maxY(self):
        return self.pos.y + self.widths[1]

    @property
    def minZ(self):
        return self.pos.z

    @property
    def maxZ(self):
        return self.pos.z + self.widths[2]
