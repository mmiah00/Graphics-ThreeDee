from display import *
from draw import *
from parsing import *
from matrix import *
import math
import random

screen = new_screen()
color = [ 255, 255, 255 ]
edges = []
transform = new_matrix()

f = open ("newscript", "w")
f.write ("ident\n")
f.write ("sphere\n250 100 0 100\n")
f.write ("sphere\n250 200 0 70\n")
f.write ("sphere\n250 270 0 40\n")
f.write ("box\n200 290 10 100 10 10\n")
f.write ("torus\n250 290 0 10 75\n")

f.write ("torus\n250 300 0 10 50\n")
f.write ("torus\n250 310 0 10 50\n")
f.write ("torus\n250 320 0 10 50\n")
f.write ("torus\n250 330 0 10 50\n")
f.write ("torus\n250 340 0 10 50\n")
f.write ("torus\n250 350 0 10 50\n")
f.write ("torus\n250 360 0 10 50\n")
f.write ("torus\n250 370 0 10 50\n")

f.write ("apply\ndisplay\nsave\npic.png")
f.close ()
parse_file ('script', edges, transform, screen, color)
#parse_file( 'newscript', edges, transform, screen, color )
