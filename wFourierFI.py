import numpy as np

class Seed:
    def __init__(self, array):
        tempArray = np.array(array)
        np.random.shuffle(tempArray)
        self.mixedArray = tempArray

    

def wFourierF( matrix, shuffled, k, l):
    N = len(matrix)
    sum = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            sum += matrix[x,y]*np.e**(-2*np.pi*1j*((x*k+y*l)/len(matrix)))
    return sum

def wFourierI(matrix, k, l):
    N = len(matrix)
    sum = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            sum += (1/(len(matrix)**2))*matrix[x,y]*np.e**(2*np.pi*1j*((x*k+y*l)/len(matrix)))
    return sum


def wfft(matrix):
    returnMat = np.zeros((len(matrix),len(matrix[0])), dtype=complex)
    tempArray = []
    for i in range(len(matrix)):
        tempArray.append(i)
    shuffled = Seed(tempArray)
    x_count = 0
    y_count = 0
    for x in shuffled.mixedArray:
        for y in shuffled.mixedArray:
            currrentVal = wFourierF(matrix, shuffled, x_count, y_count)
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
    matrix = unShuffle(matrix,shuffled)
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            returnMat[(x,y)] = wFourierI(matrix, x, y)
            
    print(x)
    return returnMat


            
