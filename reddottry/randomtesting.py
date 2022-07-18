import random
import turtle
from tkinter import *
from turtle import *
from PIL import Image
import os
import time


# setting the coordonotes for my random dot

x = (random.randint(-146, 146))
y = (random.randint(-46, 46))


turtle.setup(360, 360)

turtle.bgpic('NewBackground.png')
turtle.hideturtle
wn = turtle.Screen()

# draw the random dot
turtle.up()
turtle.setpos(x, y)
turtle.down()
turtle.dot(10, 'red')

#xyName = x
#filename = f"{name}.ps"

fname = os.path.basename(__file__)
filename = fname.replace('.py', '.png')

os.popen("gswin64c -dSAFER -dBATCH -dNOPAUSE -r300 -sDEVICE=pngalpha -dTextAlphaBits=4 -dGraphicsAlphaBits=4 -sOutputFile=" +
         filename+" -dEPSCrop temp.eps")

time.sleep(2)

print(filename)
print(x, y)
