from pyglet.gl import *
from pyglet.window import key
import math

from game import Game
from vector3d import Vector3D


class Window(pyglet.window.Window):
    def push(self, pos, rot): glPushMatrix(
    ); glRotatef(-rot[0], 1, 0, 0); glRotatef(-rot[1], 0, 1, 0); glTranslatef(-pos.x, -pos.y, -pos.z,)
    def Projection(self): glMatrixMode(GL_PROJECTION); glLoadIdentity()
    def Model(self): glMatrixMode(GL_MODELVIEW); glLoadIdentity()

    def set2d(self): self.Projection(); gluOrtho2D(
        0, self.width, 0, self.height); self.Model()
    def set3d(self): self.Projection(); gluPerspective(
        70, self.width/self.height, 0.05, 1000); self.Model()

    def setLock(self, state): self.lock = state; self.set_exclusive_mouse(state)
    lock = False
    mouse_lock = property(lambda self: self.lock, setLock)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_minimum_size(300, 200)
        self.keys = key.KeyStateHandler()
        self.push_handlers(self.keys)
        pyglet.clock.schedule(self.update)

    def on_mouse_motion(self, x, y, dx, dy):
        if self.mouse_lock:
            game.player.mouse_motion(dx, dy)

    def on_key_press(self, KEY, MOD):
        if KEY == key.ESCAPE:
            self.close()
        elif KEY == key.E:
            self.mouse_lock = not self.mouse_lock

    def update(self, dt):
        game.update(dt, self.keys)

    def on_draw(self):
        self.clear()
        self.set3d()
        self.push(game.player.pos, game.player.rot)
        game.draw()
        glPopMatrix()


if __name__ == '__main__':
    game = Game()
    for x in range(20):
        for y in range(20):
            for z in range(20):
                game.add_block('dirt', Vector3D(x, y, z))
    window = Window(width=854, height=480, caption='Minecraft', resizable=True)
    glClearColor(0.5, 0.7, 1, 1)
    glEnable(GL_BLEND);
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_CULL_FACE)
    pyglet.app.run()
