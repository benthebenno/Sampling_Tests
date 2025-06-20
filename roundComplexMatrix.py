import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm


def closer(firstVal, secondVal):
    if firstVal >= 0 and secondVal >=0: 
        if firstVal < secondVal:
            return True
        else:
            return False
    if firstVal <= 0 and secondVal <=0:
        if firstVal*-1 < secondVal*-1:
            return True
        else: 
            return False
    if firstVal <= 0 and secondVal >= 0:
        if secondVal + firstVal > 0:
            return True
        else:
            return False
    if firstVal >= 0 and secondVal <= 0:
        if firstVal + secondVal > 0:
            return True
        else:
            return False
    print(firstVal)
    print(secondVal)
    return RuntimeError

def roundCM(matrix, split):
    f, ((beforeRound), (AfterRound)) = plt.subplots(2, 1, sharex='col', sharey='row')

    # https://stackoverflow.com/questions/5891410/numpy-array-initialization-fill-with-identical-values for the full command
    diffMatrix = np.full((len(matrix), len(matrix[0])), 100)


    
    beforeRound.imshow(np.real(matrix.copy()), cmap=cm.gray)
    min = 100 
    max = -100

    #This finds the max and min values of the matrix
    max_index = 0
    possible_values = []
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix[x,y] > max:
                max = matrix[x,y] 
                max_index = (x,y)
            if matrix[x,y] < min:
                min = matrix[x,y] 

    #THIS is done as the max value is generally wayyyyy higher than the rest of the values and really messes up the rounding
    possible_values.append(matrix[max_index])
    matrix[max_index] = 0 

    max = -100
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix[x,y] > max:
                max = matrix[x,y] 
                
    diff = max - min
    

    for i in range(split):
        possible_values.append(min + diff*i)


    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            for i in range(split-1):
                print(matrix[x,y])
                print(possible_values[i])
                print("")
                diffVal = matrix[x,y] - possible_values[i]
                if matrix[x,y] >= possible_values[i] and matrix[x,y] <= possible_values[i+1] and closer(diffVal, diffMatrix[x,y]):
                    matrix[x,y] = possible_values[i]
                    diffMatrix[x,y] = diffVal
   
    print(diffMatrix)
    AfterRound.imshow(np.real(matrix), cmap=cm.gray)

    plt.show()


    return matrix