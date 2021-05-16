import numpy as np
import re
import ast
from PIL import Image

#creating the array
data = np.zeros((432, 810, 3), dtype=np.uint8)

#parsing the Javascript
pixels = open("data_2px.js", "r").read()
pixels = pixels.split("var TwoPxBats = ", 2)
pixels = pixels[1]
pixels = pixels.split("//End of the bat colors", 2)
pixels = pixels[0].replace(";", "")
pixels = ast.literal_eval(pixels)

#stores the bats and their corresponding color
colors = [[0, 0, 0], [255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 255, 255], [255, 0, 255], [255, 255, 0], [0, 255, 255]]
colorsValues = [0, 1, 2, 3, 4, 5, 6, 7]

curRow = 0
curRowBis = 0

for row in pixels:

    #reset the cells index
    curCell = 0
    curCellBis = 0

    for cell in row:
        #insert the colors in a 2x2 pixels square, since the array is twice as small as the original image
        data[curRow, curCell] = colors[colorsValues.index(cell)]
        data[curRow + 1, curCell] = colors[colorsValues.index(cell)]
        data[curRow, curCell + 1] = colors[colorsValues.index(cell)]
        data[curRow + 1, curCell + 1] = colors[colorsValues.index(cell)]

        #increments the cell counter (+ 1 because we go forward one pixel then * 2 because we use 2px squares)
        curCellBis += 1
        curCell = curCellBis * 2

    #same for the rows
    curRowBis += 1
    curRow = curRowBis * 2

#transforms the array to an image and show it
image = Image.fromarray(data)
image.save("colors_toimage_output.png", "PNG")