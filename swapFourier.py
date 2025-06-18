import numpy as np
import random 
from scipy.fft import fftn 
from fourier0smaker import fourier0sMaker
import matplotlib.pyplot as plt
from scipy.fft import ifftn 
import matplotlib.cm as cm
from PIL import Image
from initTest import matrixSum

def roundMatrix(matrix):
    print(matrix)
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix > .5:
                matrix[x, y] = 0
            else: 
                matrix[x,y] = 1

def fourSwap(x_sums, y_sums, iterations, im):


    partialMatrix = fourier0sMaker(x_sums, y_sums, im)
    # This part should do part 1 of the algorithm
    np_matrix = np.zeros((len(x_sums), len(y_sums)))

    for i in range(iterations):
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
        # print(np_matrix)

        fourMatrix = fftn(np_matrix)
        for x in range(len(fourMatrix)):
            fourMatrix[(x,0)] = partialMatrix[(x,0)]
        for y in range(len(fourMatrix[0])):
            fourMatrix[(0,y)] = partialMatrix[(0,y)]
        np_matrix = (ifftn(fourMatrix))

    return ifftn(fourMatrix)


        
def main():
    f, ((ax1), (ax2), (ax6), (ax3), (ax5)) = plt.subplots(5, 1, sharex='col', sharey='row')

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
    print(x_val,y_val)
    
    ax1.imshow(np_matrix, cmap=cm.gray)
    ax2.imshow(np.real(fftn(np_matrix)), cmap = cm.gray)
    ax6.imshow(np.real(ifftn(fftn(np_matrix))), cmap = cm.gray)
    ax3.imshow(np.real(fourier0sMaker(x_val, y_val, im)), cmap = cm.gray)
    ax5.imshow(np.real(fourSwap(x_val, y_val, iterations, im)), cmap=cm.gray)
    print(fourSwap(x_val, y_val, iterations, im))
    print("break")
    print(np.real(fourSwap(x_val, y_val, iterations, im)))
    
    plt.show()

main()