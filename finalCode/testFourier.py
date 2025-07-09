import numpy as np
import random

#stands for find corresponding value, this function returns the x,y corradinate of the value corresponding to whatever is inputted
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
            if trackMatrix[x+offset,y+offset]:
                happened = True
                options.append((x,y))
    return (options, happened)

class Seed:
    def __init__(self, matrix):
        locations = {}
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

def wfft(matrix):
    returnMat = np.zeros((len(matrix),len(matrix[0])), dtype=complex)
    offset = len(matrix)//2
    for x in range(len(matrix)//2 * -1, len(matrix)//2 + 1):
        for y in range(len(matrix[0])//2 * -1, len(matrix[0])//2 + 1):
            currrentVal = wFourierF(matrix, x, y)
            returnMat[(x+offset,y+offset)] = currrentVal
    seed = Seed(returnMat)
    return (returnMat, seed.sMat, seed)

def unshuffle(matrix, seed):
    copy = matrix.copy()
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            matrix[seed.key[(x,y)]] = copy[x,y]
    return matrix

def iwfft(matrix):
    returnMat = np.zeros((len(matrix),len(matrix[0])), dtype=complex)
    offset = len(matrix)//2
    for x in range(len(matrix)//2 * -1, len(matrix)//2 + 1):
        for y in range(len(matrix[0])//2 * -1, len(matrix[0])//2 + 1):
            returnMat[(x+offset,y+offset)] = wFourierI(matrix, x, y)
    return returnMat




            
