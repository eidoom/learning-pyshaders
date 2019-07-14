#!/usr/bin/env python3

import pyglet
import pyshaders
from pyglet.gl import GL_POLYGON
from pyglet.window import key

frag = """
#version 330 core

out vec4 color_frag;

uniform vec3 color = vec3(1.0, 1.0, 1.0);

void main()
{
  color_frag = vec4(color, 1.0);
}
"""

vert = """
#version 330 core

layout(location = 0)in vec2 vert;

void main()
{
  gl_Position = vec4(vert, 1, 1);
}
"""

window = pyglet.window.Window(width=512, height=512, resizable=True)

shader = pyshaders.from_string(vert, frag)
shader.use()

a = 0.9

vertex_list = pyglet.graphics.vertex_list(4,
                                          ('v2f', (-a, 0,
                                                   0, a,
                                                   a, 0,
                                                   0, -a)),
                                          )

color_map = {
    key._1: (1, 0, 0),
    key._2: (0, 1, 0),
    key._3: (0, 0, 1),
}


@window.event
def on_draw():
    window.clear()
    vertex_list.draw(GL_POLYGON)


@window.event
def on_key_press(symbol, modifiers):
    try:
        shader.uniforms.color = color_map[symbol]
    except KeyError:
        pass


if __name__ == '__main__':
    pyglet.app.run()
