import numpy as np
from finalCode.testFourier import wfft
from finalCode.testFourier import iwfft
from scipy.fft import ifftn
from scipy.fft import fftn
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from finalCode.testFourier import unshuffle
from finalCode.roundMatrix import roundMat

#This test assumes the number in 0,0 is 1
imagePath = input("Please give an image path: ")
im = Image.open(imagePath)

rows, cols = im.size
matrix = [[0 for i in range(cols)] for j in range(rows)]

f, ((ax1), (ax2), (ax3), (ax4), (ax5)) = plt.subplots(5, 1, sharex='col', sharey='row')
    

np_matrix = np.zeros((len(matrix),len(matrix[0])))

#This seperates the image into a matrix, of points an non points, perhaps not the most elegant solution but it
for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        if im.getpixel((x,y))[0] > 130:
            np_matrix[x, y] = 0
        else: 
            np_matrix[x,y] = 1

first = wfft(np_matrix)
second = roundMat(np.real(wfft(first[1])[0]), 10)
third = iwfft(second)
fourth = roundMat(np.real(iwfft(unshuffle(third, first[2]))), 2)

ax1.imshow(np_matrix, cmap=cm.gray)
ax2.imshow(np.real(first[1]), cmap=cm.gray)
ax3.imshow(np.real(second), cmap=cm.gray)
ax4.imshow(np.real(third), cmap=cm.gray)
ax5.imshow(np.real(fourth), cmap=cm.gray)
plt.show()

