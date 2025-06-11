from initTest import matrixSum
from PIL import Image
import numpy as np
#This is taken from imageBur.py just to find out the picture stuff
imagePath = input("Please give an image path: ")
im = Image.open(imagePath)
rows, cols = im.size
matrix = [[0 for i in range(cols)] for j in range(rows)]
np_matrix = np.zeros((len(matrix),len(matrix[0])))

for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        if im.getpixel((x,y))[0] > 130:
            np_matrix[x, y] = 0
        else: 
            np_matrix[x,y] = 1

(sum_x, sum_y) = matrixSum(np_matrix)
