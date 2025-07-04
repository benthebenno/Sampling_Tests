import numpy as np
import random

#stands for find corresponding value, this function returns the x,y corradinate of the value corresponding to whatever is inputted
def fcv(matrix, x, y):
    nx = int(-1*x)
    ny = int(-1*y)
    return (nx,ny)
def findEmpty(matrix, trackMatrix):
    options = []
    happened = False
    offset = len(matrix)//2
    # print(f"THIs is the offset {offset}")
    for x in range(len(matrix)//2 * -1, len(matrix)//2 + 1):
        for y in range(len(matrix[0])//2 * -1, len(matrix[0])//2 + 1):
            # print(x,y)
            if trackMatrix[x+offset,y+offset]:
                happened = True
                options.append((x,y))
    return (options, happened)

class Seed:
    def __init__(self, matrix):
        shuffled = np.full((len(matrix),len(matrix[0])), 0, dtype=complex)
        trackMatrix = np.full((len(matrix),len(matrix[0])), True, dtype=bool )
        offset = len(matrix)//2
        shuffled[(offset,offset)] = matrix[offset,offset]
        trackMatrix[(offset,offset)] = False
        x = (len(matrix)//2) * -1
        y = (len(matrix)//2) * -1
        while (findEmpty(shuffled, trackMatrix)[1]):
            if x > len(matrix)//2:
                x = 0 
                y += 1
            if y > len(matrix)//2:
                x = (len(matrix)//2) * -1 
                y = (len(matrix)//2) * -1
            value1 = matrix[x+offset,y+offset]
            (xoff, yoff) = fcv(matrix,x,y)
            value1corresponding = matrix[xoff+offset, yoff+offset]
            # print(f"These are the two values {x}, {y}")
            options = findEmpty(shuffled, trackMatrix)
            if not trackMatrix[x,y]:
                print("IT BROKED")
                x+=1
                continue 
            choice = random.choice(options[0])
            # print(f"These are the options: {options[0]} This is the choice: {choice}")
            shuffled[choice[0]+offset, choice[1]+offset] = value1
            xcorval = choice[0] * -1
            ycorval = choice[1] * -1
            xcorval += offset
            ycorval += offset
            shuffled[xcorval,ycorval] = value1corresponding
            trackMatrix[xcorval,ycorval] = False
            trackMatrix[choice[0]+offset, choice[1]+offset] = False
            print(f"This iterations takes the value at {x,y}, which is {x+offset, y+offset} in the original matrix. Then finds its corresponding point which is {xoff, yoff}, which is {xoff+offset, yoff+offset} in the original matrix. ")
            print(f"It then places the original value in {choice[0], choice[1]}, which is {choice[0]+offset, choice[1]+offset} in the shuffled matrix, then it places the corresponding value in {choice[0] * -1, choice[1] * -1 }, which is {xcorval, ycorval} in shuffled.")
            x += 1
                  
        self.sMat = shuffled



    

def wFourierF( matrix, k, l):
    N = len(matrix)
    sum = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            sum += matrix[x,y]*np.e**(-2*np.pi*1j*((k*x+l*y)/len(matrix)))
    return sum

def wFourierI(matrix, k, l, shuffled):
    N = len(matrix)
    sum = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            sum += (1/(len(matrix)**2))*matrix[x,y]*np.e**(2*np.pi*1j*((x*k+y*l)/len(matrix)))
    return sum


def wfft(matrix):
    returnMat = np.zeros((len(matrix),len(matrix[0])), dtype=complex)
    offset = len(matrix)//2
    for x in range(len(matrix)//2 * -1, len(matrix)//2 + 1):
        for y in range(len(matrix[0])//2 * -1, len(matrix[0])//2 + 1):
            currrentVal = wFourierF(matrix, x, y)
            returnMat[(x+offset,y+offset)] = currrentVal
    shuffled = Seed(returnMat).sMat
    return (returnMat, shuffled)
        
def unShuffle(matrix, shuffled):
    retMat = np.zeros((len(matrix),len(matrix[0])), dtype=complex)
    mixedArray = shuffled.mixedArray
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            retMat[(x,y)] = matrix[(mixedArray[x],mixedArray[y])]
    return retMat

def iwfft(matrix, shuffled):
    returnMat = np.zeros((len(matrix),len(matrix[0])), dtype=complex)
    # matrix = unShuffle(matrix,shuffled)
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            returnMat[(x,y)] = wFourierI(matrix, x, y, shuffled)
            
    print(x)
    return returnMat

def iwfftnoshuff(matrix):
    returnMat = np.zeros((len(matrix),len(matrix[0])), dtype=complex)
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            returnMat[(x,y)] = wFourierI(matrix, x, y)
            
    print(x)
    return returnMat



            
