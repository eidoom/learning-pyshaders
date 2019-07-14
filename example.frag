#version 460 core

uniform float colour;

in vec2 col;

out vec4 colour_frag;

void main()
{
  colour_frag = vec4(col, colour, 1);
}
