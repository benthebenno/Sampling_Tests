import numpy as np

def testSeed(int, seedNum):
    if seedNum == 1:
        return int
    

def wFourierF( matrix, seedFunction, k, l):
    sumArray = []
    for x in range(1, len(matrix)):
        for y in range(1, len(matrix)):
            sumArray.append(matrix[x,y]*np.e**(2*np.pi*1j*((seedFunction(x, 1)*k+seedFunction(y, 1)*l)/len(matrix))))
    sum = 0
    for val in sumArray:
        sum += val
    return sum

def wFourierI( matrix, seedFunction, k, l):
    sumArray = []
    for x in range(1, len(matrix)):
        for y in range(1, len(matrix)):
            sumArray.append((1/(len(matrix)**2))*matrix[x,y]*np.e**(-2*np.pi*1j*((seedFunction(x, 1)*k+seedFunction(y, 1)*l)/len(matrix))))
    sum = 0
    for val in sumArray:
        sum += val
    return sum


def wfft(matrix):
    returnMat = np.zeros((len(matrix),len(matrix[0])))
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            returnMat[(x,y)] = wFourierF(matrix, testSeed, x, y)
    return returnMat
        
def iwfft(matrix):
    returnMat = np.zeros((len(matrix),len(matrix[0])))
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            returnMat[(x,y)] = wFourierI(matrix, testSeed, x, y)
    return returnMat


            
