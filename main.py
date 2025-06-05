from initMaker import initMaker
from swapAlgo import swapAlgo


def matrixPrint(matrix):
    for i in range(len(matrix)):
        for m in matrix:
            print(m[i], end="")
        print("")
        


print("Welcome to my Sampling Program")
print("This program will have you describe a matrices parameters, then the type of algorithm you desire to create a random sample")
matrix_x = int(input("How wide is your matrix:"))
matrix_y = int(input("How tall is your matrix:"))

rows, cols = (matrix_x, matrix_y)
matrix = [[0 for i in range(cols)] for j in range(rows)]
# x_array = []
# y_array = []


print("Now to fill the matrix")
for x in range(matrix_x):
    for y in range(matrix_y):
        value = input("At position (" + str(x) +"," + str(y) + ") the value is:")
        matrix[x][y] = int(value)

matrixPrint(matrix)
# print("Now input how many items are included per collum")

# for i in range(matrix_x):
#     collum_num = input("Collum " + str(i) + "has this many items:")
#     x_array.append(int(collum_num))


# for i in range(matrix_y):
#     row_num = input("Row " + str(i) + "has this many items:")
#     y_array.append(int(row_num))

print("Now choose what type of model you would like")
print("     1. Swap Algorithm")

choice = input("Enter Number:")
if choice == str(1):
    iterations  = input("How many iterations would you like this model to run for: ")
    # initMatrix = initMaker(x_array, y_array)
    # print("MADE IT TO THE END")
    # matrixPrint()
    final = swapAlgo(matrix, iterations)
    print("This is the random matrix:")
    matrixPrint(final)
else: 
    print("Not a valid choice")
