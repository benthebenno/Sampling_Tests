import numpy as np
from testFourier import wfft
from wFourierFI import iwfftnoshuff
from scipy.fft import ifftn
from scipy.fft import fftn
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.cm as cm


#This test assumes the number in 0,0 is 1
imagePath = input("Please give an image path: ")
im = Image.open(imagePath)

rows, cols = im.size
matrix = [[0 for i in range(cols)] for j in range(rows)]

f, ((ax1), (ax4), (ax9), (ax5)) = plt.subplots(4, 1, sharex='col', sharey='row')
    

np_matrix = np.zeros((len(matrix),len(matrix[0])))

#This seperates the image into a matrix, of points an non points, perhaps not the most elegant solution but it
for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        if im.getpixel((x,y))[0] > 130:
            np_matrix[x, y] = 0
        else: 
            np_matrix[x,y] = 1

first = wfft(np_matrix)
second = ifftn(first)

ax1.imshow(np_matrix, cmap=cm.gray)
ax4.imshow(np.real(first[0]), cmap=cm.gray)
ax9.imshow(np.real(fftn(np_matrix)), cmap=cm.gray)
ax5.imshow(np.real(second[0]), cmap=cm.gray)
# print(second[0])
plt.show()

