from PIL import Image
from matrixPrint import matrixPrint
from scipy.fft import ifftn 
from scipy.fft import fftn
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from roundComplexMatrix import roundCM

imagePath = input("Please give an image path: ")
im = Image.open(imagePath)
rows, cols = im.size
matrix = [[0 for i in range(cols)] for j in range(rows)]

f, ((ax1), (blur5), (blur8), (blur11), (blur29)) = plt.subplots(5, 1, sharex='col', sharey='row')

np_matrix = np.zeros((len(matrix),len(matrix[0])))

#This seperates the image into a matrix, of points an non points, perhaps not the most elegant solution but it
for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        if im.getpixel((x,y))[0] > 130:
            np_matrix[x, y] = 0
        else: 
            np_matrix[x,y] = 1


f5 = fftn(np_matrix)
f8 = fftn(np_matrix)
f11 = fftn(np_matrix)
f29 = fftn(np_matrix)

for x in range(len(f5)):
    for y in range(len(f5[0])):
        if (x > 5 and x< (len(f5) - 5) or (y > 5 and y <(len(f5) - 5))):
            f5[x,y] = 0 

for x in range(len(f8)):
    for y in range(len(f8[0])):
        if (x > 8 and x< (len(f8) - 8) or (y > 8 and y <(len(f8) - 8))):
            f8[x,y] = 0 

for x in range(len(f11)):
    for y in range(len(f11[0])):
        if (x > 11 and x< (len(f11) - 11) or (y > 11 and y <(len(f11) - 11))):
            f11[x,y] = 0 


f5 = roundCM(f5, 100000)
print(f5)


reversedImage5 = ifftn(f5)
reversedImage8 = ifftn(f8)
reversedImage11 = ifftn(f11)
reversedImage29 = ifftn(f29)

ax1.imshow(np_matrix, cmap=cm.gray)
blur5.imshow(np.real(reversedImage5), cmap=cm.gray)
blur8.imshow(np.real(reversedImage8), cmap=cm.gray)
blur11.imshow(np.real(reversedImage11), cmap=cm.gray)
blur29.imshow(np.real(reversedImage29), cmap=cm.gray)
plt.show()
