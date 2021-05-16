from PIL import Image
from contextlib import redirect_stdout
import re

#square size in px (2x2, 3x3, etc)
size = 5

def get_main_color(file):
    pixels = file.getcolors(size * size)
    sorted_pixels = sorted(pixels, key=lambda t: t[0])
    dominant_color = sorted_pixels[-1][1]
    if dominant_color != 0:
        return 0
    else :
        return 1

with open("data/output.txt", "r+") as f:
    data = f.read()
    f.seek(0)
    if data != "":
        f.write("")
    f.truncate()

width = size
height = size
im = Image.open("data/bat2rdc_colors.png")
imgwidth, imgheight = im.size
curArray = []
h = 0
for i in range(0, imgheight, height):
    for j in range(0, imgwidth, width):
        box = (j, i, j+width, i+height)
        a = im.crop(box)
        b = get_main_color(a)
        curArray.insert(j, b)
        if j >= (imgwidth - size) :
            with open("data/output.txt", "r+") as f:
                data = f.read()
                f.seek(0)
                with redirect_stdout(f):
                    print(data)
                    print(curArray , ",", sep="")
                f.truncate()
            h += 1
            curArray = []

#removing the line breaks from the output
with open("data/output.txt", "r+") as f:
    data = f.read()
    f.seek(0)
    data = re.sub("^\n", "", data, flags=re.M)
    with redirect_stdout(f):
        print(data)
    f.truncate()