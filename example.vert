#version 460 core

in layout(location = 0) vec2 pos;

uniform float offset_x;

out vec2 col;

void main()
{
  gl_Position = vec4(pos.x + offset_x, pos.y, 0, 1);
  col = (pos + 1)/2;
}
