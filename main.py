from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()


#parser file uses move,rotate about all 3 axes and scale to create cube
parse_file('instructions.txt', edges, transform, screen, color)

print('make_translate...')
print_matrix(make_translate(1, 2, 3))

print('make_scale...')
print_matrix(make_scale(4, 5, 6))

print('rotations:')
print('x...')
print(make_rotX(180))
print('y...')
print(make_rotY(180))
print('z...')
print(make_rotZ(180))


