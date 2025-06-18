##This is identiacal to swap fouier but uses the initalizer instead of random rows
# I think this will be more accurate

import numpy as np
import random 
from scipy.fft import fftn 
from fourier0smaker import fourier0sMaker
import matplotlib.pyplot as plt
from scipy.fft import ifftn 
import matplotlib.cm as cm
from PIL import Image
from initTest import matrixSum
from initMaker import initMaker
def fourSwap(x_sums, y_sums, iterations, im):


    partialMatrix = fourier0sMaker(x_sums, y_sums, im)
    # This part should do part 1 of the algorithm
    np_matrix = initMaker(x_sums,y_sums)
  
    # print(np_matrix)

    fourMatrix = fftn(np_matrix)
    for x in range(len(fourMatrix)):
        fourMatrix[(x,0)] = partialMatrix[(x,0)]
    for y in range(len(fourMatrix[0])):
        fourMatrix[(0,y)] = partialMatrix[(0,y)]

    return ifftn(fourMatrix)


        
def main():
    f, ((ax1), (ax2),(ax3), (ax5)) = plt.subplots(4, 1, sharex='col', sharey='row')

    imagePath = input("Please give an image path: ")
    im = Image.open(imagePath)

    rows, cols = im.size
    matrix = [[0 for i in range(cols)] for j in range(rows)]
    
    np_matrix = np.zeros((len(matrix),len(matrix[0])))

    #This seperates the image into a matrix, of points an non points, perhaps not the most elegant solution but it
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if im.getpixel((x,y))[0] > 130:
                np_matrix[x, y] = 0
            else: 
                np_matrix[x,y] = 1

    (x_val, y_val) = matrixSum(np_matrix)
    print(x_val,y_val)
    
    ax1.imshow(np_matrix, cmap=cm.gray)
    ax2.imshow(np.real(fftn(np_matrix)), cmap = cm.gray)
    ax3.imshow(np.real(fourier0sMaker(x_val, y_val, im)), cmap = cm.gray)
    ax5.imshow(np.real(fourSwap(x_val, y_val, 3, im)), cmap=cm.gray)
    plt.show()

main()