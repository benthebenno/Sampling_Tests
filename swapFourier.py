import numpy as np
import random 
from scipy.fft import fftn 
from fourier0smaker import fourier0sMaker
import matplotlib.pyplot as plt
from scipy.fft import ifftn 
import matplotlib.cm as cm
from PIL import Image
from initTest import matrixSum
from roundMatrix import round

def fourSwap(x_sums, y_sums, iterations, im):

    
    partialMatrix = fourier0sMaker(x_sums, y_sums, im)
    # This part should do part 1 of the algorithm
    np_matrix = np.zeros((len(x_sums), len(y_sums)))
    for sumNum in range(len(x_sums)):
                yIndex = sumNum
                count = 0
                while x_sums[sumNum] > 0:
                    if count == len(x_sums):
                        count = 0
                    if np_matrix[yIndex, count] == 0: 
                        if random.randrange(0,len(x_sums)) == 0:
                            np_matrix[yIndex, count ] = 1
                            x_sums[sumNum] -= 1
                    count += 1
    for i in range(iterations):
        fourMatrix = fftn(np_matrix)
        for x in range(len(fourMatrix)):
            fourMatrix[(x,0)] = partialMatrix[(x,0)]
        for y in range(len(fourMatrix[0])):
            fourMatrix[(0,y)] = partialMatrix[(0,y)]
        np_matrix = round(ifftn(fourMatrix))
    return (np_matrix, ifftn(fourMatrix) )


        
def main():
    f, ((ax1), (ax2), (ax6), (ax3), (ax5), (ax7)) = plt.subplots(6, 1, sharex='col', sharey='row')

    imagePath = input("Please give an image path: ")
    im = Image.open(imagePath)

    iterations = int(input("Please give a number of iterations you want this function to run: "))

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

    sawpTouple = fourSwap(x_val, y_val, iterations, im)

    #The original image
    ax1.imshow(np_matrix, cmap=cm.gray)

    #The fftn of the original matrix
    ax2.imshow(np.real(fftn(np_matrix)), cmap = cm.gray)

    #The correct reconstruction (should always be identical to the original image)
    ax6.imshow(np.real(ifftn(fftn(np_matrix))), cmap = cm.gray)

    #The edge fourier transform
    ax3.imshow(np.real(fourier0sMaker(x_val, y_val, im)), cmap = cm.gray)

    #rouned data
    ax5.imshow(np.real(sawpTouple[0]), cmap=cm.gray)

    #data before rounding
    ax7.imshow(np.real(sawpTouple[1]), cmap=cm.gray)

    
    plt.show()

main()