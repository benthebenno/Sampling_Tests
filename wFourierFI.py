import numpy as np


class Seed:
    def __init__(self, array):
        tempArray = np.array(array)
        np.random.shuffle(tempArray)
        self.mixedArray = tempArray
        # print(f"Temp Array = {tempArray}")
        # print(self.mixedArray)
        # print( np.random.shuffle(np.array(array)))

    def giveItem(self, int):
        # print(self.mixedArray)
        return self.mixedArray[int]
    

def wFourierF( matrix, shuffled, k, l):
    N = len(matrix)
    sum = 0
    for x in range(0, len(matrix)):
        for y in range(0, len(matrix)):
            # sum += (matrix[x,y]*((np.cos(2*np.pi*(x*k+y*l)/N))-(1j*(np.sin(2*np.pi*(x*k+y*l)/N)))))
            # sum += matrix[x,y]*np.e**(-2*np.pi*1j*((seedFunction(x, 1)*k+seedFunction(y, 1)*l)/len(matrix)))
            sum += matrix[x,y]*np.e**(-2*np.pi*1j*((shuffled.giveItem(x)*k+shuffled.giveItem(y)*l)/len(matrix)))
    return sum

def wFourierI(matrix, shuffled, k, l):
    sumArray = []
    N = len(matrix)
    sum = 0
    for x in range(0, len(matrix)):
        for y in range(0, len(matrix)):
            # sum += ((1/(len(matrix)**2))*matrix[x,y]*((np.cos(2*np.pi*(x*k+y*l)/N))-(1j*(np.sin(2*np.pi*(x*k+y*l)/N)))))
            # sum += (1/(len(matrix)**2))*matrix[x,y]*np.e**(2*np.pi*1j*((seedFunction(x, 1)*k+seedFunction(y, 1)*l)/len(matrix)))
            sum += (1/(len(matrix)**2))*matrix[x,y]*np.e**(2*np.pi*1j*((shuffled.giveItem(x)*k+shuffled.giveItem(y)*l)/len(matrix)))
            # print("")
    return sum


def wfft(matrix):
    returnMat = np.zeros((len(matrix),len(matrix[0])), dtype=complex)
    tempArray = []
    for i in range(len(matrix)):
        tempArray.append(i)
    # print(tempArray)
    shuffled = Seed(tempArray)
    # print(shuffled.giveItem(0))
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            currrentVal = wFourierF(matrix, shuffled, x, y)
            returnMat[(x,y)] = currrentVal
    print(x)
    return (returnMat,shuffled)
        
def iwfft(matrix, shuffled):
    returnMat = np.zeros((len(matrix),len(matrix[0])), dtype=complex)
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            returnMat[(x,y)] = wFourierI(matrix, shuffled, x, y)
    print(x)
    return returnMat


            
