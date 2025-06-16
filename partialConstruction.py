from initTest import matrixSum
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import ifftn 
from scipy.fft import fftn
import matplotlib.cm as cm
from initTest import matrixSum

#This is taken from imageBur.py just to find out the picture stuff

#This takes the image 
imagePath = input("Please give an image path: ")
im = Image.open(imagePath)

#This makes a matrix the same size as the image, then creates a second matrix which uses the np form
rows, cols = im.size
matrix = [[0 for i in range(cols)] for j in range(rows)]
np_matrix = np.zeros((len(matrix),len(matrix[0])))

#this line constructs the graphs
f, ((ax1), (ax4), (axtest), (ax5)) = plt.subplots(4, 1, sharex='col', sharey='row')

fourier_matrix = np.zeros((len(matrix),len(matrix[0])), dtype=complex)

#This takes the pixels from the images and translates them into either 1s or 0s in the np_matrix
for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        if im.getpixel((x,y))[0] > 130:
            np_matrix[x, y] = 0
        else: 
            np_matrix[x,y] = 1

TESTFouier = fftn(np_matrix)

# This tests if sum was working correctly, I belive it is
# print(f"The matrix:: {np_matrix}")
(sum_x, sum_y) = matrixSum(np_matrix)

# print(f"x_sum= {sum_x}")
# print(f"y_sum= {sum_y}")


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

reversedImage = ifftn(fourier_matrix)
 
# print(x)
# print(y)

ax1.imshow(np_matrix, cmap=cm.gray)
ax4.imshow(np.real(fourier_matrix), cmap=cm.gray)
ax5.imshow(np.real(reversedImage), cmap=cm.gray)
axtest.imshow(np.real(TESTFouier), cmap=cm.gray)
plt.show()

print(f"This is the fourier at 0,0 {fourier_matrix[0,0]}")
print(f"This is the Test at 0,0 {TESTFouier[0,0]}")
print("")
print(f"This is the fourier at 0,1 {fourier_matrix[0,1]}")
print(f"This is the Test at 0,1 {TESTFouier[0,1]}")
print("")
print(f"This is the fourier at 1,0 {fourier_matrix[1,0]}")
print(f"This is the Test at 1,0 {TESTFouier[1,0]}")
