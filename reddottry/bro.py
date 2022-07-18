import random
import turtle
from tkinter import *
from turtle import *
from PIL import Image
import os
import time

# let's start a loop


x = (random.randint(-142, 142))
y = (random.randint(-42, 42))
xy = (str(x) + "," + str(y))

turtle.setup(360, 360)
turtle.bgpic('NewBackground.png')
turtle.hideturtle
wn = turtle.Screen()

# draw the random dot

turtle.up()
turtle.setpos(x, y)
turtle.down()
turtle.dot(10, 'red')

print(x, y)


eps_file = "temp.eps"

# generating eps file
ts = turtle.getscreen()
turtle.hideturtle()
ts.getcanvas().postscript(file=eps_file)

fname = os.path.basename(__file__)
Prefilename = fname.replace('.py', '.png')
# change the name to x,y values
filename = Prefilename.replace('bro', xy)

# Converting eps file to jpg | with filename
#im.save(str(filename)+".jpg", "JPEG")

# Convert eps to transparent png using ghost script
os.popen("gswin64c -dSAFER -dBATCH -dNOPAUSE -r300 -sDEVICE=pngalpha -dTextAlphaBits=4 -dGraphicsAlphaBits=4 -sOutputFile=" +
         filename+" -dEPSCrop temp.eps")

# Merge transparent png on top of given background png
time.sleep(2)


print("Done")
