from initTest import matrixSum
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import ifftn 
from scipy.fft import fftn
import matplotlib.cm as cm

#This is taken from imageBur.py just to find out the picture stuff
imagePath = input("Please give an image path: ")
im = Image.open(imagePath)
rows, cols = im.size
matrix = [[0 for i in range(cols)] for j in range(rows)]
np_matrix = np.zeros((len(matrix),len(matrix[0])))


f, ((ax1), (ax4), (ax5)) = plt.subplots(3, 1, sharex='col', sharey='row')

fourier_matrix = np.zeros((len(matrix),len(matrix[0])), dtype=complex)
for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        if im.getpixel((x,y))[0] > 130:
            np_matrix[x, y] = 0
        else: 
            np_matrix[x,y] = 1

(sum_x, sum_y) = matrixSum(np_matrix)

count = 0
y_max = len(matrix[0])
for row in range(y_max):
    for x_row_sum in sum_x:
        fourier_matrix[0, count] = np.array([(x_row_sum * (np.cos(2*(np.pi*(row*count)/y_max)))),(x_row_sum *(np.sin(2*(np.pi*(2*np.pi*(row*count)/y_max)))*1j))])

row_count = 0
x_max = len(matrix)

for collum in range(x_max):
    for y_row_sum in sum_y:
        if collum == 0:
            fourier_matrix[row_count, 0] += np.array[(y_row_sum * (np.cos(2*(np.pi*(collum*row_count)/x_max)))),(np.sin(2*np.pi*(2*(np.pi*(collum*row_count)/x_max)))*1j)]
        else:
            fourier_matrix[row_count, 0] = np.array[(y_row_sum * (np.cos(2*(np.pi*(collum*row_count)/x_max)))),(np.sin(2*np.pi*(2*(np.pi*(collum*row_count)/x_max)))*1j)]

Z = ifftn(np_matrix)
reversedImage = fftn(Z)

ax1.imshow(np_matrix, cmap=cm.gray)
ax4.imshow(np.real(Z), cmap=cm.gray)
ax5.imshow(np.real(reversedImage), cmap=cm.gray)
plt.show()
