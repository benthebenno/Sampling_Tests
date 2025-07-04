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
        emptySpaceMatrix = np.full((len(matrix),len(matrix[0])), True, dtype=bool )
        offset = len(matrix)//2
        shuffled[(offset,offset)] = matrix[offset,offset]
        trackMatrix[(offset,offset)] = False
        emptySpaceMatrix[(offset,offset)] = False
        x = (len(matrix)//2) * -1
        y = (len(matrix)//2) * -1
        while (findEmpty(shuffled, trackMatrix)[1]):
            print("this is the track")
            print(trackMatrix)
            print("")
            print("This is the shuffle")
            print(shuffled)
            print("")
            if x > len(matrix)//2:
                x = (len(matrix)//2) * -1 
                y += 1
            if y > len(matrix)//2:
                x = (len(matrix)//2) * -1 
                y = (len(matrix)//2) * -1


            if not trackMatrix[x+offset,y+offset]:
                # print("IT BROKED")
                x+=1
                continue 
    
            value1 = matrix[x+offset,y+offset]
            (xoff, yoff) = fcv(matrix,x,y)
            value1corresponding = matrix[xoff+offset, yoff+offset]

            trackMatrix[x+offset,y+offset] = False
            trackMatrix[xoff+offset, yoff+offset] = False
            # print(f"These are the two values {x}, {y}")
            options = findEmpty(shuffled, emptySpaceMatrix)
            
            # print(trackMatrix[x,y])
            
            choice = random.choice(options[0])
            # print(f"These are the options: {options[0]} This is the choice: {choice}")
            shuffled[choice[0]+offset, choice[1]+offset] = value1
            xcorval = choice[0] * -1
            ycorval = choice[1] * -1
            xcorval += offset
            ycorval += offset
            shuffled[xcorval,ycorval] = value1corresponding
            
            emptySpaceMatrix[choice[0]+offset, choice[1]+offset] = False
            emptySpaceMatrix[xcorval,ycorval] = False


            print("This is where it is placed")
            print(choice[0]+offset, choice[1]+offset)
            print(xcorval,ycorval)
            # print(f"This iterations takes the value at {x,y}, which is {x+offset, y+offset} in the original matrix. Then finds its corresponding point which is {xoff, yoff}, which is {xoff+offset, yoff+offset} in the original matrix. ")
            # print(f"It then places the original value in {choice[0], choice[1]}, which is {choice[0]+offset, choice[1]+offset} in the shuffled matrix, then it places the corresponding value in {choice[0] * -1, choice[1] * -1 }, which is {xcorval, ycorval} in shuffled.")
            x += 1
                 
        self.sMat = shuffled



    

def wFourierF( matrix, k, l):
    N = len(matrix)
    sum = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            sum += matrix[x,y]*np.e**(-2*np.pi*1j*((k*x+l*y)/len(matrix)))
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
    offset = len(matrix)//2
    for x in range(len(matrix)//2 * -1, len(matrix)//2 + 1):
        for y in range(len(matrix[0])//2 * -1, len(matrix[0])//2 + 1):
            currrentVal = wFourierF(matrix, x, y)
            returnMat[(x+offset,y+offset)] = currrentVal
    shuffled = Seed(returnMat).sMat
    return (returnMat, shuffled)

def iwfft(matrix):
    returnMat = np.zeros((len(matrix),len(matrix[0])), dtype=complex)
    offset = len(matrix)//2
    for x in range(len(matrix)//2 * -1, len(matrix)//2 + 1):
        for y in range(len(matrix[0])//2 * -1, len(matrix[0])//2 + 1):
            returnMat[(x+offset,y+offset)] = wFourierI(matrix, x, y)
    return returnMat



            
