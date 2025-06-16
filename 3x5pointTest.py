import numpy as np
import random
from alySwap import altSwapAlgo
from scipy.fft import ifftn 
from scipy.fft import fftn 
import matplotlib.cm as cm
from initTest import matrixSum
import matplotlib.pyplot as plt

iterations = int(input("How many iterations would you like the swap to run for? The higher the more data points"))
input_x = int(input("What x value do you want to check?"))
input_y = int(input("What y value do you want to check?"))

#This section makes and populates a 3x5 matrix
np_matrix = np.zeros((3,5))
for y in range(len(np_matrix[0])):
    for x in range(len(np_matrix)):
        np_matrix[(x,y)] = random.randrange(0,2)    
    
#This is an array of each matrix made by the swap
matrixArray = altSwapAlgo(np_matrix, iterations)



data = []
for matrix in matrixArray:
    data.append(fftn(matrix)[input_x,input_y])

#This line removes any duplicates
# print(data)

#This plots the imaginary data, taken from https://www.geeksforgeeks.org/python/how-to-plot-a-complex-number-in-python-using-matplotlib/

x = [ele.real for ele in data]

y = [ele.imag for ele in data]

print(f"There are {len(data)} points in this graph")

plt.scatter(x, y)
plt.ylabel('Imaginary')
plt.xlabel('Real')
plt.show()

occuranceDict = {}
for element in data:
    occuranceDict[element] = 0
    for secondElement in data:
        if element == secondElement:
            occuranceDict[element] += 1

keys = occuranceDict.keys()
values = occuranceDict.values()

        

plt.bar(keys,values)
plt.ylabel('Occurances')
plt.xlabel('Numbers')
plt.show()

#SHOULD TRIM ANY DUPLICATES
