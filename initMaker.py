from tests import matrixPrint
#taken from here https://www.geeksforgeeks.org/generate-a-matrix-with-each-row-and-column-of-given-sum/
from tests import hasSameSums


def findMaxIndex(array):
    indexCount = 0
    maxNum = -1
    count = 0
    for num in array:
        if maxNum < num:
            maxNum = num
            indexCount = count
        count += 1
    return indexCount

def isNotEmpty(array):
    for i in array:
        if i != 0:
            return True
    return False

def initMaker(x_array, y_array):
    rows, cols = (len(x_array), len(y_array))
    matrix = [[0 for i in range(cols)] for j in range(rows)]

    while isNotEmpty(x_array) :
        # print(f"x_array in loop= {x_array}")
        # print(f"y_array in loop= {y_array}")
        currentX = findMaxIndex(x_array)
        # print(f"currentX {currentX}")
        # print(matrix)
        tempArray = y_array.copy()
        for i in range(x_array[currentX]):
            currentY = findMaxIndex(tempArray)
            tempArray[currentY] = -1
            matrix[currentX][currentY] = 1
            x_array[currentX] -= 1
            y_array[currentY] -= 1 
    

    
    return matrix 




