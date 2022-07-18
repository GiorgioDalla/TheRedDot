import random
import turtle
from tkinter import *
from turtle import *
from PIL import Image
import os
import time



turtle.setup(350, 350)

x = (random.randint(-133, 133))
y = (random.randint(-45, 45))

# put xy values into a string so that it can be seen in the name
xy = (str(x) + "," + str(y))


turtle.bgpic('NewBackground.png')
turtle.hideturtle
wn = turtle.Screen()

# draw the random dot

turtle.up()
turtle.setpos(x, y)
turtle.down()
turtle.dot(5, 'red')


print(x, y)

# keeping eps file name as image
eps_file = "temp.eps"

# generating eps file
ts = turtle.getscreen()
turtle.hideturtle()
ts.getcanvas().postscript(file=eps_file)

# get current python file name as string without ".py"
fname = os.path.basename(__file__)
Prefilename = fname.replace('.py', '.png')
# change the name to x,y values
filename = Prefilename.replace('seeifitworks', xy)


# Convert eps to transparent png using ghost script
os.popen("gswin64c -dSAFER -dBATCH -dNOPAUSE -r300 -sDEVICE=pngalpha -dTextAlphaBits=4 -dGraphicsAlphaBits=4 -sOutputFile=" +
         filename+" -dEPSCrop temp.eps")





print("Done")
