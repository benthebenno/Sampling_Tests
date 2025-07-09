from finalCode.testFourier import wfft
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import ifftn 
from scipy.fft import fftn
import matplotlib.cm as cm
from finalCode.testFourier import iwfft


    
imagePath = input("Please give an image path: ")
im = Image.open(imagePath)

rows, cols = im.size
matrix = [[0 for i in range(cols)] for j in range(rows)]

f, ((ax1), (ax4), (ax5), (ax6), (ax7)) = plt.subplots(5, 1, sharex='col', sharey='row')
    

np_matrix = np.zeros((len(matrix),len(matrix[0])))

#This seperates the image into a matrix, of points an non points, perhaps not the most elegant solution but it
for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        if im.getpixel((x,y))[0] > 130:
            np_matrix[x, y] = 0
        else: 
            np_matrix[x,y] = 1

print("Made it to first ffft")
Z = fftn(np_matrix)

realEncypted = np.real(ifftn(Z))

secondIm = fftn(realEncypted)

print("MAde it to reverse")
reversedImage = ifftn(secondIm)


ax1.imshow(np_matrix, cmap=cm.gray)
ax4.imshow(np.real(Z), cmap=cm.gray)
ax5.imshow(np.real(realEncypted), cmap=cm.gray)
ax6.imshow(np.real(secondIm),cmap=cm.gray)
ax7.imshow(np.real(reversedImage),cmap=cm.gray)
plt.show()
