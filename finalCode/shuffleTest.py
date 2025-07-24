import numpy as np
from testFourier import wfft
from testFourier import iwfft
from scipy.fft import ifftn
from scipy.fft import fftn
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from testFourier import unshuffle
from roundMatrix import roundMat

#This file creates one run though of the encryption then graphs each matrix along the way

#This part takes in an image, then turns it into a binary matrix
imagePath = input("Please give an image path: ")
im = Image.open(imagePath)

rows, cols = im.size
matrix = [[0 for i in range(cols)] for j in range(rows)]

f, ((ax1), (ax2), (ax3), (ax4), (ax5)) = plt.subplots(5, 1, sharex='col', sharey='row')
    

np_matrix = np.zeros((len(matrix),len(matrix[0])))

for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        if im.getpixel((x,y))[0] > 130:
            np_matrix[x, y] = 0
        else: 
            np_matrix[x,y] = 1

#This is the run through of the encryption 
first = wfft(np_matrix)
second = roundMat(np.real(wfft(first[1])[0]), 8, True)[0]
third = iwfft(second)
fourth = roundMat(np.real(iwfft(unshuffle(third, first[2]))), 2, False)[0]

#This part graphs the original and four matrices
ax1.imshow(np_matrix, cmap=cm.gray)
ax2.imshow(np.real(first[1]), cmap=cm.gray)
ax3.imshow(np.real(second), cmap=cm.gray)
ax4.imshow(np.real(third), cmap=cm.gray)
ax5.imshow(np.real(fourth), cmap=cm.gray)
plt.show()

