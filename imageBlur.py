from PIL import Image
from matrixPrint import matrixPrint
from scipy.fft import ifftn 
from scipy.fft import fftn
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np



imagePath = input("Please give an image path: ")
im = Image.open(imagePath)

blur = (((int(input("How much would you like the image blurred, as a percent: "))/100) * (im.size[0]/2))) 
print(f"This is the size {im.size[0]/2}")
print(f"This is the blur {blur}")
rows, cols = im.size
matrix = [[0 for i in range(cols)] for j in range(rows)]

f, ((ax1), (ax4), (ax5)) = plt.subplots(3, 1, sharex='col', sharey='row')

np_matrix = np.zeros((len(matrix),len(matrix[0])))

#This seperates the image into a matrix, of points an non points, perhaps not the most elegant solution but it
for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        if im.getpixel((x,y))[0] > 130:
            np_matrix[x, y] = 0
        else: 
            np_matrix[x,y] = 1


Z = ifftn(np_matrix)

for x in range(len(Z)):
    for y in range(len(Z[0])):
        if not((x > blur and x < (im.size[0] - blur)) and (y > blur and y < (im.size[0]-blur))): 
            Z[x,y] = 0 
reversedImage = fftn(Z)

ax1.imshow(np_matrix, cmap=cm.gray)
ax4.imshow(np.real(Z), cmap=cm.gray)
ax5.imshow(np.real(reversedImage), cmap=cm.gray)
plt.show()

