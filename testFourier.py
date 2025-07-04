import numpy as np
import random

#stands for find corresponding value, this function returns the x,y corradinate of the value corresponding to whatever is inputted
def fcv(matrix, x, y):
    nx = int(-1*x)
    ny = int(-1*y)
    return (nx,ny)
def findEmpty(matrix):
    options = []
    happened = False
    for x in range(int((len(matrix))/2+1)):
        for y in range(int((len(matrix[0]))/2+1)):
            # print(x,y)
            # print(matrix[x,y])
            if matrix[x,y] == -99899:
                # print("went in")
                happened = True
                options.append((x,y))
    return (options, happened)

class Seed:
    def __init__(self, matrix):
        shuffled = np.full((len(matrix),len(matrix[0])), -99899, dtype=complex)
        shuffled[(0,0)] = matrix[0,0]
        offset = len(matrix)//2
        x = (len(matrix)//2) * -1
        y = (len(matrix)//2) * -1
        print(f"This is the x,y {x,y}")
        print(len(matrix))
        print(len(matrix)//2)
        while (findEmpty(shuffled)[1]):
                    
                    # print(f"This is the value they go up too {len(matrix)//2}")
            # for x in range(1, int((len(matrix)- 1 )/2) ):
            #     for y in range(1, (int((len(matrix)- 1)/2))):
                    # print(f"x,y {x,y}")
                    # print(shuffled)
                    # if random.randrange(0,2) == 0:
                    # print("This is what it will replace")
                    # print(x,y)
                    # print(fcv(matrix,x,y)) 
                    if x > len(matrix)//2:
                        x = 0 
                        y += 1
                    if y > len(matrix)//2:
                        x = 1 
                        y = 0
                    print("THIS IS THE X,Y")
                    print(x,y)
                    value1 = matrix[x+offset,y+offset]
                    (xoff, yoff) = fcv(matrix,x,y)
                    value1corresponding = matrix[xoff+offset, yoff+offset]
                    options = findEmpty(shuffled)
                    if not options[1]:
                        print("IT BROKED")
                        break 
                    choice = random.choice(options[0])
                    shuffled[choice] = value1
                    shuffled[fcv(shuffled, choice[0], choice[1])] = value1corresponding
                    x += 1
                   
                    # print("STRAT")
                    # print(shuffled)
            # print(findEmpty(shuffled)[1])
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
    for x in range(-len(matrix)//2, len(matrix)//2):
        for y in range(-len(matrix[0])//2, len(matrix[0])//2):
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



            
