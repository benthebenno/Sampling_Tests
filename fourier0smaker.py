#This code is mostly just partial construction turned into a funcion
import numpy as np
from scipy.fft import fftn 

def fourier0sMaker(sum_x, sum_y, im):
    fourier_matrix = np.zeros((len(sum_x), len(sum_y)))
    rows, cols = im.size
    matrix = [[0 for i in range(cols)] for j in range(rows)]


    count = 0
    y_max = len(matrix[0])
    for row in range(y_max):
        for x_row_sum in sum_x:
            fourier_matrix[row, 0] += (x_row_sum * (np.cos(2*(np.pi*(row*count)/y_max)))) - (x_row_sum *(np.sin(2*np.pi*(row*count)/y_max)*1j))
            count += 1
        count = 0

    # This stops the doubling issue, may not be nessecicary
    fourier_matrix[0, 0] = 0
    row_count = 0
    x_max = len(matrix)

    for collum in range(x_max):
        for y_row_sum in sum_y:
            fourier_matrix[0, collum] += (y_row_sum * (np.cos(2*(np.pi*(collum*row_count)/x_max)))) - (y_row_sum * (np.sin(2*np.pi*(collum*row_count)/x_max)*1j))
            row_count += 1
        row_count = 0
    
    return fourier_matrix