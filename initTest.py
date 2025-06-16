from initMaker import initMaker
from matrixPrint import matrixPrint
import random 
from tests import hasSameSums

# print("Welcome to my Sampling Program")
# print("This program will have you describe a matrices parameters, then the type of algorithm you desire to create a random sample")
# matrix_x = int(input("How wide is your matrix:"))
# matrix_y = int(input("How tall is your matrix:"))

# rows, cols = (matrix_x, matrix_y)
# matrix = [[0 for i in range(cols)] for j in range(rows)]

# x_array = []
# y_array = []

# print("Now input how many items are included per collum")

# for i in range(matrix_x):
#     collum_num = input("Collum " + str(i) + "has this many items:")
#     x_array.append(int(collum_num))


# for i in range(matrix_y):
#     row_num = input("Row " + str(i) + "has this many items:")
#     y_array.append(int(row_num))

# return_matrix =initMaker(x_array, y_array)
# matrixPrint(return_matrix)
def matrixSum(matrix):
    x_array = []
    y_array = []
    for x in range(len(matrix)):
        x_sum = 0
        for y in range(len(matrix[0])):
            x_sum += matrix[x][y]
        x_array.append(x_sum)
    for y in range(len(matrix[0])):
        y_sum = 0
        for x in range(len(matrix)):
            y_sum += matrix[x][y]
        y_array.append(y_sum)
    return (x_array, y_array)
             

# for i in range (2, 150):
#         print("It has made it to matrix of size: " + str(i) )
#         rows, cols = (i, i)
#         matrix = [[0 for i in range(cols)] for j in range(rows)]

#         rows, cols = (i, i)
#         saved_matrix = [[0 for i in range(cols)] for j in range(rows)]

#         for x in range(i):
#             for y in range(i):
#                 new_num = random.randrange(0,2)
#                 matrix[x][y]= new_num
#                 saved_matrix[x][y] = new_num
#         (x_array, y_array) = matrixSum(matrix)
#         # matrixPrint(saved_matrix)
#         # print(f"x_array= {x_array}")
#         # print(f"y_array= {y_array}")

#         newMatrix = initMaker(x_array, y_array)
#         if newMatrix == saved_matrix:
#              print("For this they are the same")
#         if not hasSameSums(saved_matrix, newMatrix):
#             # matrixPrint(saved_matrix)
#             matrixPrint(newMatrix)
#             print("THIS HAS FAILED")
#             break
        # for x in range(len(newMatrix)):
        #     for y in range(len(newMatrix)):
        #         if newMatrix[x][y] > 1:
        #             print("This has failed, matrix contains wrong number")
        #             matrixPrint(saved_matrix)
        #             matrixPrint(newMatrix)
        #             break

