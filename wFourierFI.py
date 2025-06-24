import numpy as np

def testSeed(int, seedNum):
    if seedNum == 1:
        return int
    

def wFourierF( matrix, seedFunction, k, l):
    N = len(matrix)
    sum = 0
    for x in range(0, len(matrix)):
        for y in range(0, len(matrix)):
            sum += (matrix[x,y]*((np.cos(2*np.pi*(x*k+y*l)/N))-(1j*(np.sin(2*np.pi*(x*k+y*l)/N)))))
    return sum

def wFourierI(matrix, seedFunction, k, l):
    sumArray = []
    N = len(matrix)
    sum = 0
    for x in range(0, len(matrix)):
        for y in range(0, len(matrix)):
            # sum += ((1/(len(matrix)**2))*matrix[x,y]*((np.cos(2*np.pi*(x*k+y*l)/N))-(1j*(np.sin(2*np.pi*(x*k+y*l)/N)))))
            sum += (1/(len(matrix)**2))*matrix[x,y]*np.e**(-2*np.pi*1j*((seedFunction(x, 1)*k+seedFunction(y, 1)*l)/len(matrix)))
            # print("")
    return sum


def wfft(matrix):
    returnMat = np.zeros((len(matrix),len(matrix[0])), dtype=complex)
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            currrentVal = wFourierF(matrix, testSeed, x, y)
            returnMat[(x,y)] = currrentVal
    return returnMat
        
def iwfft(matrix):
    returnMat = np.zeros((len(matrix),len(matrix[0])), dtype=complex)
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            returnMat[(x,y)] = wFourierI(matrix, testSeed, x, y)
    return returnMat


            
