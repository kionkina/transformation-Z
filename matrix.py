import math

def make_translate( x, y, z ):
    pass


def make_scale_helper( x, y, z):
    arr = [x,y,z]
    ret = []
    len_row = 4
    len_col = 4
    for r in range(len_row):
        new_row = []
        for c in range(len_col):
            if (c<=2) and (c == r):
                new_row.append(arr[c])
            else:
                new_row.append(0)
        ret.append(new_row)
    return ret



def make_scale( x, y, z ):
    pass

def make_rotX( theta ):    
    pass

def make_rotY( theta ):
    pass

def make_rotZ( theta ):
    pass

def print_matrix( matrix ):
    s = ''
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            s+= str(matrix[c][r]) + ' '
        s+= '\n'
    print s


print_matrix(make_scale_helper(10, 12, 14));

def ident( matrix ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            if r == c:
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):

    point = 0
    for row in m2:
        #get a copy of the next point
        tmp = row[:]
        
        for r in range(4):
            m2[point][r] = (m1[0][r] * tmp[0] +
                            m1[1][r] * tmp[1] +
                            m1[2][r] * tmp[2] +
                            m1[3][r] * tmp[3])
        point+= 1


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
