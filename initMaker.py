from tests import matrixPrint
#taken from here https://www.geeksforgeeks.org/generate-a-matrix-with-each-row-and-column-of-given-sum/

def initMaker(x_array, y_array):

    rows, cols = (len(x_array), len(y_array))
    matrix = [[0 for i in range(cols)] for j in range(rows)]
   
    # print(f"x Array = {x_array}")
    # print(f"y array = {y_array}")
    # matrixPrint(matrix)

    currRowSum = [0] * rows
    currColSum = [0] * cols    
    for i in range(rows):
        for j in range(cols):
            rowVal = x_array[i] - currRowSum[i]
            colVal = y_array[j] - currColSum[j]

            matrix[i][j] = min(rowVal, colVal, 1)

            currRowSum[i] += matrix[i][j]
            currColSum[j] += matrix[i][j]
    return matrix 



    # #This loop populates the collums by the first valid option 
    # for i in range(len(x_array)):
    #     # print(matrix)
    #     frequency = x_array[i]
    #     # print("frequency")
    #     # print(frequency)
    #     sucess = 0
    #     for y_index in range(len(y_array)):
    #         if sucess == frequency:   
    #             # print("break triggered")
    #             break 
    #         if rowHasRoom(x_array, y_array, matrix, y_index):
    #             # print("row increase triggered")
    #             # print(matrix)
    #             # print(i)
    #             # print(y_index)
    #             #This places in last spot, might work better
    #             matrix[i][len(y_array) - y_index - 1] = 1
    #             # print(matrix)
    #             sucess += 1
    #     # if sucess < frequency:
    #     #     matrixPrint(matrix)
    #     #     print("This is not a valid matrix please try again")
    #     #     return IndexError
    # print("This should populate the collums correctly")

    # # print(matrix)
    # #This loop populates the rows with the first valid option
    # for i in range(len(y_array)):
    #     frequency = y_array[i]
    #     sucess = 0
    #     # print(frequency)
    #     for x_index in range(len(x_array)):
    #         if sucess == frequency: 
    #             break 
    #         if collumHasRoom(x_array, y_array, matrix[x_index], x_index):
    #             matrix[len(x_array) - x_index - 1][i] = 1
    #             sucess += 1
    #         else:
    #             sucess +=1 
    #     if sucess < frequency:
    #         print(matrix)
    #         print("This is not a valid matrix please try again")
    #         return IndexError
    # return matrix

def collumHasRoom(x_array, y_array, collum, index):
    sum = 0
    for i in collum:
        sum += i
    if sum < x_array[index]:
        return True
    return False


def rowHasRoom(x_array, y_array, matrix, index):
    row = []
    for i in range(len(x_array)):
        row.append(matrix[i][index])
    sum = 0
    for i in row:
        sum += i
    if sum < y_array[index]:
        return True
    return False


