from testFourier import iwfft
from testFourier import wfft
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from roundMatrix import roundMat
from testFourier import unshuffle
from testFourier import makeBinary2Vals
# imagePath = input("Please give an image path: ")
im = Image.open("realQRWiki.png")
iteration = int(input("How many loops do you want:"))
failArray = []
for count in range (iteration):
    print(count)
    rows, cols = im.size
    matrix = [[0 for i in range(cols)] for j in range(rows)]

    # f, ((ax1), (ax2)) = plt.subplots(2, 1, sharex='col', sharey='row')
        

    np_matrix = np.zeros((len(matrix),len(matrix[0])))

    #This seperates the image into a matrix, of points an non points, perhaps not the most elegant solution but it
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if im.getpixel((x,y))[0] > 130:
                np_matrix[x, y] = 0
            else: 
                np_matrix[x,y] = 1

    first = wfft(np_matrix)
    # print("first Done")
    second = roundMat(np.real(wfft(first[1])[0]), 8, False)
    # print("second Done")
    third = iwfft(second[0])
    # print("Third Done")
    fourth = makeBinary2Vals(roundMat(np.real(iwfft(unshuffle(third, first[2]))), 2, True)[0])
    # print("Fourth Done")
    fails = []
    failcount = 0
    for x in range(len(np_matrix)):
        for y in range(len(np_matrix)):
            if np_matrix[(x,y)] !=  (fourth[(x,y)]):
                
                failcount += 1
                fails.append((x,y))
    failArray.append(failcount)
    print(f"Fails are: {failcount}")
    # if failcount > 400:
    #     print("Fails over 400 times")
        # print(fourth)

info = {}
for x in failArray:
    if x in info.keys():
        info[x] += 1
    else:
        info[x] = 1

plt.bar(info.keys(), info.values())
plt.show()
# print(np.real(iwfft(unshuffle(third, first[2]))))            


