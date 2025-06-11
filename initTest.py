from initMaker import initMaker
from matrixPrint import matrixPrint

print("Welcome to my Sampling Program")
print("This program will have you describe a matrices parameters, then the type of algorithm you desire to create a random sample")
matrix_x = int(input("How wide is your matrix:"))
matrix_y = int(input("How tall is your matrix:"))

rows, cols = (matrix_x, matrix_y)
matrix = [[0 for i in range(cols)] for j in range(rows)]

x_array = []
y_array = []

print("Now input how many items are included per collum")

for i in range(matrix_x):
    collum_num = input("Collum " + str(i) + "has this many items:")
    x_array.append(int(collum_num))


for i in range(matrix_y):
    row_num = input("Row " + str(i) + "has this many items:")
    y_array.append(int(row_num))

return_matrix =initMaker(x_array, y_array)
matrixPrint(return_matrix)