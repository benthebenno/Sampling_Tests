from wFourierFI import wFourierF
from scipy.fft import fftn
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from wFourierFI import wfft


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
first = fftn(np_matrix)


second = fftn(first)
# print("SPACE")
# print(second)
for x in range(len(second)):
    for y in range(len(second[x])):
        print(second[x,y])
        if (np.iscomplex(second[x,y])):
            print("it has failed")
            print(second[x,y])


ax1.imshow(np_matrix, cmap=cm.gray)
ax4.imshow(np.real(first), cmap=cm.gray)
ax5.imshow(np.real(second), cmap=cm.gray)
plt.show()
