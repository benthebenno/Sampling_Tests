from wFourierFI import wFourierF
from scipy.fft import fftn
from PIL import Image
import numpy as np

imagePath = input("Please give an image path: ")
im = Image.open(imagePath)

rows, cols = im.size
matrix = [[0 for i in range(cols)] for j in range(rows)]

np_matrix = np.zeros((len(matrix),len(matrix[0])))


np_matrix = np.zeros((len(matrix),len(matrix[0])))

#This seperates the image into a matrix, of points an non points, perhaps not the most elegant solution but it
for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        if im.getpixel((x,y))[0] > 130:
            np_matrix[x, y] = 0
        else: 
            np_matrix[x,y] = 1

first = fftn(np_matrix)

second = fftn(first)

for x in range(len(second)):
    for y in range(len(second[x])):
        if (np.iscomplex(second[x,y])):
            print("it has failed")
            print(second[x,y])
        