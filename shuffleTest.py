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
# unshuffled = unshuffle(first[1].copy(), first[2])
# second = iwfft(unshuffled)

# for x in range(len(second)):
#     for y in range(len(second[0])):
#         if np.abs(np.imag(second[x,y])) > 1.0e-10:
#             print("IT HAS FAILED AT MAKING REAL NUMBERS")
#             print(second[x,y])

# print(second)

# print(first[0][0,0])
# print(second[0,0])
# print(second)
print("THIS IS THE FIRST FTTN")
# print(fftn(first[1]))
# print(iwfft(first[1]))
# print(np.real(wfft(first[1])[0]))
ax1.imshow(np_matrix, cmap=cm.gray)
ax2.imshow(np.real(first[1]), cmap=cm.gray)
ax3.imshow(np.real(second), cmap=cm.gray)
ax4.imshow(np.real(third), cmap=cm.gray)
ax5.imshow(np.real(fourth), cmap=cm.gray)
# print(second[0])
plt.show()

