from wFourierFI import wFourierF
from scipy.fft import fftn
from scipy.fft import ifftn
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from wFourierFI import wfft
from wFourierFI import iwfft

f, ((ax1), (ax4), (ax5)) = plt.subplots(3, 1, sharex='col', sharey='row')

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
# The first transformation
# first = wfft(np_matrix)
print("IT IS HERE")
first = iwfft(np_matrix)
second = ifftn(np_matrix)
third = wfft(first)
fourth = fftn(second)

# first = fftn(np_matrix)
# second = fftn(np_matrix)
# print("SPACE")
# print(second)
print("This is the start of the thing")
for x in range(len(second)):
    for y in range(len(second[x])):
        # print(second[x,y])
        # if first[x,y] != second[x,y]:
        #     print("it has failed")
        # print(first[x,y])
        # print(second[x,y])
        # # print(np.linalg.norm(first-second))
        # if np.iscomplex(third[x,y]):
        #     print("Third failed")
        #     print(third[x,y])
        # if np.iscomplex(fourth[x,y]):
        #     print("fourth failed")
        #     print(fourth[x,y])
        if np.abs(third[x,y]-fourth[x,y]) > 1.0e-10:
            print("third-fourth")
            print(np.abs(third[x,y]-fourth[x,y]))
        if np.abs(first[x,y]-second[x,y]) > 1.0e-10:
            print("first-second")
            print(np.abs(first[x,y]-second[x,y]))


ax1.imshow(np_matrix, cmap=cm.gray)
ax4.imshow(np.real(third), cmap=cm.gray)
ax5.imshow(np.real(fourth), cmap=cm.gray)
plt.show()
