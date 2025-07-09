from PIL import Image
from matrixPrint import matrixPrint
from scipy.fft import ifftn 
from scipy.fft import fftn
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from roundComplexMatrix import roundCM
from finalCode.testFourier import wfft
from finalCode.testFourier import iwfft

imagePath = input("Please give an image path: ")
im = Image.open(imagePath)
rows, cols = im.size
matrix = [[0 for i in range(cols)] for j in range(rows)]

# f, ((ax1), (graph)) = plt.subplots(2, 1, sharex='col', sharey='row')

np_matrix = np.zeros((len(matrix),len(matrix[0])))

#This seperates the image into a matrix, of points an non points, perhaps not the most elegant solution but it
for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        if im.getpixel((x,y))[0] > 130:
            np_matrix[x, y] = 0
        else: 
            np_matrix[x,y] = 1

transformed = wfft(np_matrix)

data = []
transformed2 = np.real(wfft(transformed[1])[0])
# print(transformed2)
for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        data.append(transformed2[x,y])

#This plots the imaginary data, taken from https://www.geeksforgeeks.org/python/how-to-plot-a-complex-number-in-python-using-matplotlib/
print(data)
x = [ele.real for ele in data]

y = [ele.imag for ele in data]

print(f"There are {len(data)} points in this graph")

plt.scatter(x, y)
plt.ylabel('Imaginary')
plt.xlabel('Real')
plt.show()