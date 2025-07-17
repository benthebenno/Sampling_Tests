from testFourier import iwfft
from testFourier import wfft
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from roundMatrix import roundMat
from testFourier import unshuffle
from testFourier import makeBinary2Vals

#This file runs for an inputted amount of iterations, creating new QR code encryptions and then unencrypts them, this tests how much data is lost in 
# the FEC process, I have found that rounding to 8 is the lowest we can go while still getting consistently under 15 differences

imagePath = input("Please give an image path: ")
im = Image.open(imagePath)

iteration = int(input("How many loops do you want:"))
failArray = []

rows, cols = im.size
matrix = [[0 for i in range(cols)] for j in range(rows)] 
np_matrix = np.zeros((len(matrix),len(matrix[0])))

#This seperates the image into a matrix, of binary data, this matrix is used for transformation and comparison
for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        if im.getpixel((x,y))[0] > 130:
            np_matrix[x, y] = 0
        else: 
            np_matrix[x,y] = 1

for count in range (iteration):

    print(count)
    
    #These two lines makes a shuffled matrix of real values
    first = wfft(np_matrix)
    second = roundMat(np.real(wfft(first[1])[0]), 8, False)

    #These two lines reverse the last two lines and output the final matrix, the fourth would be identical to the first if we did not round
    # but we round to make it so information can actually be displayed
    third = iwfft(second[0])
    fourth = makeBinary2Vals(roundMat(np.real(iwfft(unshuffle(third, first[2]))), 2, True)[0])


    #This part compares the final matrix to the original to see how diffrent they are, then this data is saved
    failcount = 0
    for x in range(len(np_matrix)):
        for y in range(len(np_matrix)):
            if np_matrix[(x,y)] !=  (fourth[(x,y)]):
                failcount += 1
    failArray.append(failcount)
    print(f"Fails are: {failcount}")


#This final section takes all the stored data and makes it into a graph which is displayed
info = {}
for x in failArray:
    if x in info.keys():
        info[x] += 1
    else:
        info[x] = 1

plt.bar(info.keys(), info.values())
plt.show()


