from PIL import Image
import numpy

size = 2

def get_main_color(file):
    img = file
    colors = img.getcolors(256) #put a higher value if there are many colors in your image
    max_occurence, most_present = 0, 0
    try:
        for c in colors:
            if c[0] > max_occurence:
                (max_occurence, most_present) = c
        if most_present == (255, 255, 255) :
            return 0
        else :
            return 1
    except TypeError:
        raise Exception("Too many colors in the image")

width = size
height = size
im = Image.open("ta.png")
imgwidth, imgheight = im.size
curArray = []
h = 0
for i in range(0, imgheight, height):
    for j in range(0, imgwidth, width):
        box = (j, i, j+width, i+height)
        a = im.crop(box)
        b = get_main_color(a)
        curArray.insert(j, b)
        if j >= 808 :
            print(curArray , ",", sep="")
            h += 1
            curArray = []
            if h%100 == 0 :
                a = input("Waiting")