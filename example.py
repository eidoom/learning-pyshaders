#!/usr/bin/env python3

import pyglet
from pyglet.window import key

import pyshaders


class Shape:
    def __init__(self, a):
        self.a = a
        self.indices = (0, 1, 2)
        self.vertices = ('v2f', (0, self.a,
                                 self.a, -self.a,
                                 -self.a, -self.a))
        # self.colours = ('c3f', (1, 0, 0,
        #                         0, 1, 0,
        #                         0, 0, 1))

        self.vertex_list = pyglet.graphics.vertex_list_indexed(3,
                                                               self.indices,
                                                               self.vertices
                                                               )

    def render(self):
        self.vertex_list.draw(pyglet.gl.GL_TRIANGLES)


class MyWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.shape_1 = Shape(0.8)
        # self.shape_2 = Shape(0.2)

    def on_draw(self):
        self.clear()
        self.shape_1.render()
        # self.shape_2.render()

    # def on_resize(self, width, height):
    #     pyglet.gl.glViewport(0, 0, width, height)

    def on_key_press(self, symbol, modifiers):
        if symbol in colour_map.keys():
            shader.uniforms.colour = colour_map[symbol]


pyglet.gl.glClearColor(0, 0, 0, 0)

w = 512
h = w
window = MyWindow(visible=True, width=w, height=h, resizable=True)

shader = pyshaders.from_files_names("example.vert", "example.frag")
shader.use()

shader.uniforms.offset_x = 0.1
shader.uniforms.colour = 1

colour_map = {getattr(key, f"_{i}"): (i + 1) / 10 for i in range(10)}

if __name__ == '__main__':
    pyglet.app.run()
