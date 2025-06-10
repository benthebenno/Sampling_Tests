from PIL import Image
from matrixPrint import matrixPrint
from scipy.fft import ifftn 
from scipy.fft import fftn
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np



# imagePath = input("Please give an image path: ")
imagePath = r"C:\Users\user\Sampling_Tests\testImage.png"
im = Image.open(imagePath)

blur = int(input("How much would you like the image blurred"))
rows, cols = im.size
matrix = [[0 for i in range(cols)] for j in range(rows)]

f, ((ax1), (ax4), (ax5)) = plt.subplots(3, 1, sharex='col', sharey='row')

np_matrix = np.zeros((len(matrix),len(matrix[0])))
#This seperates the image into a matrix
for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        matrix[x][y] = im.getpixel((x,y))[0]
        if im.getpixel((x,y))[0] > 160:
            np_matrix[x, y] = 0
        else: 
            np_matrix[x,y] = 1

# matrixPrint(matrix)
Z = ifftn(np_matrix)
# print(Z)

#This part should slice Z
# for i in range(int(blur)):
#     np.delete(Z, 1,1)
#     np.delete(Z, -1,-1)
for x in range(len(Z)):
    for y in range(len(Z)):
        if not((x > blur and x < (im.size[0] - blur)) and (y > blur and y < (im.size[0]-blur))): 
            Z[x,y] = 0 
reversedImage = fftn(Z)

ax1.imshow(np_matrix, cmap=cm.gray)
ax4.imshow(np.real(Z), cmap=cm.gray)
ax5.imshow(np.real(reversedImage), cmap=cm.gray)
plt.show()

#This rebuilds a new image
# returnImage = Image.new(mode="RGB", size=im.size)
# for x in range(len(matrix)):
#     for y in range(len(matrix[x])):
#         returnImage.putpixel((x,y), (matrix[x][y], matrix[x][y], matrix[x][y]))


# returnImage.show()
