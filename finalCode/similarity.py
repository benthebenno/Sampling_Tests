from finalCode.testFourier import iwfft
from finalCode.testFourier import wfft
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from finalCode.roundMatrix import roundMat
from finalCode.testFourier import unshuffle
imagePath = input("Please give an image path: ")
im = Image.open(imagePath)

rows, cols = im.size
matrix = [[0 for i in range(cols)] for j in range(rows)]

f, ((ax1), (ax2)) = plt.subplots(2, 1, sharex='col', sharey='row')
    

np_matrix = np.zeros((len(matrix),len(matrix[0])))

#This seperates the image into a matrix, of points an non points, perhaps not the most elegant solution but it
for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        if im.getpixel((x,y))[0] > 130:
            np_matrix[x, y] = 0
        else: 
            np_matrix[x,y] = 1

first = wfft(np_matrix)
print("first Done")
second = roundMat(np.real(wfft(first[1])[0]), 8)
print("second Done")
third = iwfft(second)
print("Third Done")
fourth = roundMat(np.real(iwfft(unshuffle(third, first[2]))), 2)
print("Fourth Done")
fails = []
failcount = 0
for x in range(len(np_matrix)):
    for y in range(len(np_matrix)):
        if np_matrix[(x,y)] !=  (fourth[(x,y)] + 1):
            print("It failes")
            print(np_matrix[(x,y)])
            print(fourth[(x,y)])
            failcount += 1
            fails.append((x,y))


print(f"There were {failcount} failures")
print(fails)
            
ax1.imshow(np.real(np_matrix), cmap=cm.gray)
ax2.imshow(np.real(fourth), cmap=cm.gray)
plt.show()

