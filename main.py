from display import *
from draw import *
from parsing import *
from matrix import *
import math
import random

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

f = open ("newscript", "w")
f.write ("ident\n")
y = 0
while (y < 150):
    f.write ("torus\n250 " + str (y + 2) + " 0 20 50\n")
    y += 5

while (y < 170):
    f.write ("torus\n250 " + str (y + 2) + " 0 30 100\n")
    y += 5

while (y < 190):
    f.write ("torus\n250 " + str (y + 2) + " 0 25 90\n")
    y += 5

while (y < 200):
    f.write ("torus\n250 " + str (y + 2) + " 0 20 80\n")
    y += 5

while (y < 210):
    f.write ("torus\n250 " + str (y + 2) + " 0 15 70\n")
    y += 5

while (y < 220):
    f.write ("torus\n250 " + str (y + 2) + " 0 10 60\n")
    y += 5

while (y < 230):
    f.write ("torus\n250 " + str (y + 2) + " 0 5 50\n")
    y += 5

f.write ("sphere\n250 220 0 45\n")
# for i in range (100):
#     x = random.randint (0, 500)
#     y = random.randint (0,500)
#     if (pow (x - 250, 2) + pow (y - 250, 2)) > 10000:
#         f.write ("sphere\n")
#         f.write (str (x) + " " + str (y) + " 0 10\n")

f.write ("apply\ndisplay\nsave\npic.png")
f.close ()
parse_file( 'newscript', edges, transform, screen, color )
