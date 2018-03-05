from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix - 
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix - 
	 scale: create a scale matrix, 
	    then multiply the transform matrix by the scale matrix - 
	    takes 3 arguments (sx, sy, sz)
	 move: create a translation matrix, 
	    then multiply the transform matrix by the translation matrix - 
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 apply: apply the current transformation matrix to the 
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    f = open(fname, 'ru')
    lines = f.readlines()
    point_matrix = new_matrix(4,4)
    for i in range(len(lines)):
        line = lines[i]
#        print line
        # took me a while to realize I was missing the \n
        #print line == "line\n"
        if line == "line\n":
#            print "adding line . . ."
            arr = lines[i+1].split(" ")
            add_edge(point_matrix, int(arr[0]), int(arr[1]), int(arr[2]), int(arr[3]), int(arr[4]), int(arr[5]))
#            print "after adding a line . . ."
#            print_matrix(point_matrix)
        elif line == "ident\n":
            ident(transform)
        elif line == "scale\n":
            arr = lines[i+1].split(" ")
            matrix_mult(make_scale(float(arr[0]), float(arr[1]), float(arr[2])), transform)
        elif line == "move\n":
            arr = lines[i+1].split(" ")
            matrix_mult(make_translate(float(arr[0]), float(arr[1]), float(arr[2])), transform)
        elif line == "rotate\n":
            arr = lines[i+1].split(" ")
            if arr[0] == "x":
                matrix_mult(make_rotX(arr[1]), transform)
            elif arr[0] == "y":
                matrix_mult(make_rotY(arr[1]), transform)
            else:
                matrix_mult(make_rotZ(arr[1]), transform)
        elif line == "apply\n":
            matrix_mult(transform, point_matrix)
        elif line == "display":
            clear_screen(screen)
            for r in range(len(point_matrix)):
                for c in range(len(point_matrix[r])):
                    point_matrix[r][c] = int(point_matrix[r][c])
            draw_lines(point_matrix, screen, color)
            display(screen)
        elif line == "save\n":
            arr = lines[i + 1].split("\n")         
            for r in range(len(point_matrix)):
                for c in range(len(point_matrix[r])):
                    point_matrix[r][c] = int(point_matrix[r][c])
            draw_lines(point_matrix, screen, color)
            save_extension( screen, arr[0])
        else:
            pass
