import numpy as np
from finalCode.testFourier import wfft
from finalCode.testFourier import iwfft
from scipy.fft import ifftn
from scipy.fft import fftn
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from finalCode.testFourier import unshuffle
from finalCode.roundMatrix import roundMat
import random 

def fcv( x, y):
    nx = int(-1*x)
    ny = int(-1*y)
    return (nx,ny)

def findEmpty(matrix, trackMatrix):
    options = []
    happened = False
    offset = len(matrix)//2
    for x in range(len(matrix)//2 * -1, len(matrix)//2 + 1):
        for y in range(len(matrix[0])//2 * -1, len(matrix[0])//2 + 1):
            # print(x,y)
            if trackMatrix[x+offset,y+offset]:
                happened = True
                options.append((x,y))
    return (options, happened)

#This test assumes the number in 0,0 is 1
imagePath = input("Please give an image path: ")
im = Image.open(imagePath)

rows, cols = im.size
matrix = [[0 for i in range(cols)] for j in range(rows)]

f, ( (ax4), (ax5)) = plt.subplots(2, 1, sharex='col', sharey='row')
    

np_matrix = np.zeros((len(matrix),len(matrix[0])))

#This seperates the image into a matrix, of points an non points, perhaps not the most elegant solution but it
for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        if im.getpixel((x,y))[0] > 130:
            np_matrix[x, y] = 0
        else: 
            np_matrix[x,y] = 1

shuffled = np.full((len(np_matrix),len(np_matrix[0])), 0, dtype=complex)
trackMatrix = np.full((len(np_matrix),len(np_matrix[0])), True, dtype=bool )
emptySpaceMatrix = np.full((len(np_matrix),len(np_matrix[0])), True, dtype=bool )
offset = len(np_matrix)//2
shuffled[(offset,offset)] = np_matrix[offset,offset]
trackMatrix[(offset,offset)] = False
emptySpaceMatrix[(offset,offset)] = False
x = (len(np_matrix)//2) * -1
y = (len(np_matrix)//2) * -1
while (findEmpty(shuffled, trackMatrix)[1]):
    if x > len(np_matrix)//2:
        x = (len(np_matrix)//2) * -1 
        y += 1
    if y > len(np_matrix)//2:
        x = (len(np_matrix)//2) * -1 
        y = (len(np_matrix)//2) * -1
    if not trackMatrix[x+offset,y+offset]:
        x+=1
        continue 

    value1 = np_matrix[x+offset,y+offset]
    (xoff, yoff) = fcv(x,y)
    value1corresponding = np_matrix[xoff+offset, yoff+offset]

    trackMatrix[x+offset,y+offset] = False
    trackMatrix[xoff+offset, yoff+offset] = False
    options = findEmpty(shuffled, emptySpaceMatrix)            
    choice = random.choice(options[0])
    shuffled[choice[0]+offset, choice[1]+offset] = value1
    xcorval = choice[0] * -1
    ycorval = choice[1] * -1
    xcorval += offset
    ycorval += offset
    shuffled[xcorval,ycorval] = value1corresponding
    emptySpaceMatrix[choice[0]+offset, choice[1]+offset] = False
    emptySpaceMatrix[xcorval,ycorval] = False
    x+=1

ax4.imshow(np.real(np_matrix), cmap=cm.gray)
ax5.imshow(np.real(shuffled), cmap=cm.gray)
plt.show()
