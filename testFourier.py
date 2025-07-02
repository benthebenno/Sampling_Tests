import numpy as np
import random



#stands for find corresponding value, this function returns the x,y corradinate of the value corresponding to whatever is inputted
def fcv(matrix, x, y):
    val = matrix[x,y]
    offset = ((len(matrix)-1)/2)
    nx = int(x + offset)
    ny = int(y + offset)
    print(nx,ny)
    # corresponding = matrix[nx, ny]
    # if val-corresponding != 0:
    #     return IndexError
    return (nx,ny)
def findEmpty(matrix):
    options = []
    happened = False
    for x in range(int((len(matrix)-1)/2)):
        for y in range(int((len(matrix[0])-1)/2)):
            if matrix[x,y] == -99899:
                happened = True
                options.append((x,y))
    return (options, happened)

class Seed:
    def __init__(self, matrix):
        shuffled = np.full((len(matrix),len(matrix[0])), -99899, dtype=complex)
        shuffled[(0,0)] = matrix[0,0]
        while (findEmpty(shuffled)[1]):
            for x in range(1, int((len(matrix)- 1 )/2) ):
                for y in range(1, (int((len(matrix)- 1)/2))):
                    print(f"x,y {x,y}")
                    # print(shuffled)
                    # if random.randrange(0,2) == 0:
                    value1 = matrix[x,y]
                    value1corresponding = matrix[fcv(matrix,x,y)]
                    options = findEmpty(shuffled)
                    if not options[1]:
                        break 
                    choice = random.choice(options[0])
                    shuffled[choice] = value1
                    shuffled[fcv(shuffled, choice[0], choice[1])] = value1corresponding
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
    shuffled = Seed(matrix).sMat
    x_count = 0
    y_count = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            currrentVal = wFourierF(shuffled, x_count, y_count)
            returnMat[(x,y)] = currrentVal
            y_count += 1
        x_count += 1
        y_count = 0
    return (returnMat,shuffled)
        
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



            
