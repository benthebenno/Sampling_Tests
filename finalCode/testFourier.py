import numpy as np
import random
import PIL
import struct

#This file contains many functions important for the transformation and encryption process

#stands for find corresponding value, this function returns the x,y coordinates of the value corresponding to whatever is inputted
def fcv( x, y):
    nx = int(-1*x)
    ny = int(-1*y)
    return (nx,ny)

#This makes a matrix with only two values a binary matrix, this is used in conjunction with rounding a matrix to two values then using this
# function
def makeBinary2Vals(matrix):
    max = -100
    min = 100
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            if matrix[x,y] < min:
                min = matrix[x,y]
            if matrix[x,y] > max:
                max = matrix[x,y]
    if max == min:
       
        return ValueError
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            if matrix[x,y] == max:
                matrix[x,y] = 1
            if matrix[x,y] == min:
                matrix[x,y] = 0
    return matrix


# This is a helper function for the shuffler, finds if there are any empty spots in a matrix, by using the trackMatrix
def findEmpty(matrix, trackMatrix):
    options = []
    happened = False
    offset = len(matrix)//2
    for x in range(len(matrix)//2 * -1, len(matrix)//2 + 1):
        for y in range(len(matrix[0])//2 * -1, len(matrix[0])//2 + 1):
            if trackMatrix[x+offset,y+offset]:
                happened = True
                options.append((x,y))
    return (options, happened)

#This seed class is what shuffles the matrix, it holds the shuffled matrix, and the 'key' for unshuffling it. At the moment the 'key' is just
# a dictionary with the correct positions, with a little work this could be changed to be an actual encrypted key. 
class Seed:
    #This init takes in a matrix, and shuffles it while keeping the pairs (i.e 1,1 to -1,1) together
    def __init__(self, matrix):
        locations = {}

        #These three matrixes, work together to track where things have been placed and where they should be placed
        shuffled = np.full((len(matrix),len(matrix[0])), 0, dtype=complex)
        trackMatrix = np.full((len(matrix),len(matrix[0])), True, dtype=bool )
        emptySpaceMatrix = np.full((len(matrix),len(matrix[0])), True, dtype=bool )

        offset = len(matrix)//2
        shuffled[(offset,offset)] = matrix[offset,offset]
        trackMatrix[(offset,offset)] = False
        emptySpaceMatrix[(offset,offset)] = False
        x = (len(matrix)//2) * -1
        y = (len(matrix)//2) * -1
        locations[(offset,offset)] = (offset,offset)
        while (findEmpty(shuffled, trackMatrix)[1]):
            if x > len(matrix)//2:
                x = (len(matrix)//2) * -1 
                y += 1
            if y > len(matrix)//2:
                x = (len(matrix)//2) * -1 
                y = (len(matrix)//2) * -1
            if not trackMatrix[x+offset,y+offset]:
                x+=1
                continue 
    
            value1 = matrix[x+offset,y+offset]
            (xoff, yoff) = fcv(x,y)
            value1corresponding = matrix[xoff+offset, yoff+offset]

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
            locations[(choice[0] + offset, choice[1]+offset)] = (x+offset, y+offset)
            locations[(xcorval,ycorval)] = (xoff+offset, yoff+offset)
            emptySpaceMatrix[choice[0]+offset, choice[1]+offset] = False
            emptySpaceMatrix[xcorval,ycorval] = False
            x += 1                
        self.sMat = shuffled
        self.key = locations

    

def wFourierF( matrix, k, l):
    N = len(matrix)
    sum = 0
    offset = len(matrix)//2

    for x in range(len(matrix)//2 * -1, len(matrix)//2 + 1):
        for y in range(len(matrix[0])//2 * -1, len(matrix[0])//2 + 1):  
            sum += matrix[x+offset,y+offset]*np.e**(-2*np.pi*1j*((k*x+l*y)/len(matrix)))
    return sum

def wFourierI(matrix, k, l):
    N = len(matrix)
    sum = 0
    offset = len(matrix)//2
    for x in range(len(matrix)//2 * -1, len(matrix)//2 + 1):
        for y in range(len(matrix[0])//2 * -1, len(matrix[0])//2 + 1):
            sum += (1/(len(matrix)**2))*matrix[x+offset,y+offset]*np.e**(2*np.pi*1j*((x*k+y*l)/len(matrix)))
    return sum

#This function does a Forwards Fourier Transformation, based of the equation given by Professor Levinson  
def wfft(matrix):
    returnMat = np.zeros((len(matrix),len(matrix[0])), dtype=complex)
    offset = len(matrix)//2
    for x in range(len(matrix)//2 * -1, len(matrix)//2 + 1):
        for y in range(len(matrix[0])//2 * -1, len(matrix[0])//2 + 1):
            currrentVal = wFourierF(matrix, x, y)
            returnMat[(x+offset,y+offset)] = currrentVal
    seed = Seed(returnMat)
    return (returnMat, seed.sMat, seed)

#This function takes a matrix and seed, then unshuffles the matrix, since the key is the correct location were the pixel should be placed
def unshuffle(matrix, seed):
    copy = matrix.copy()
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            matrix[seed.key[(x,y)]] = copy[x,y]
    return matrix

#This function does a Inverse Fourier Transformation, based of the equation given by Professor Levinson  
def iwfft(matrix):
    returnMat = np.zeros((len(matrix),len(matrix[0])), dtype=complex)
    offset = len(matrix)//2
    for x in range(len(matrix)//2 * -1, len(matrix)//2 + 1):
        for y in range(len(matrix[0])//2 * -1, len(matrix[0])//2 + 1):
            returnMat[(x+offset,y+offset)] = wFourierI(matrix, x, y)
    return returnMat

#This function can be added to either shuffleTest.py or similarity.py (or technically any file though I would not reccomend others) to make a full
# FEC-Code
def makeColorPicture(matrix, values):
    # These colors are ["black", "blue", "green", "cyan", "red", "magenta", "yellow", "white"]
    colors = [(0,0,0), (0,35,245), (55,125,34), (115,251,253), (235,51,36), (88,19,94), (255,254,145), (255,255,255)]
    im = PIL.Image.new(mode="RGB", size=(len(matrix) + 1, len(matrix[0]) + 1), )

    # These are 32 bit ints but we dont care about the end numbers as the decimal really does not need to be that accurate
    min = str(bin(struct.unpack('!I', struct.pack('!f', values[0]))[0]))
    max = str(bin(struct.unpack('!I', struct.pack('!f', values[7]))[0]))

    for x in range(1, len(matrix)):
        for y in range(1, len(matrix[0])):
            count = 0
            for val in values:
                if val == matrix[x,y]:
                    im.putpixel((x,y), colors[count])
                count += 1
    for i in range(1, 29):
        if min[i+1] == "0":
            im.putpixel((i, 0), colors[7])
        if max[i+1] == "0":
            im.putpixel((29, i), colors[7]) 
        if min[i+1] == "1":
            im.putpixel((i, 0), colors[2])
        if max[i+1] == "1":
            im.putpixel((29, i), colors[2]) 
    im.save("FEC-Code.png")
    im.show()
