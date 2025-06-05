import random
from matrixPrint import matrixPrint 
def makeRow(index, matrix, length):
    row = []
    for i in range(length):
        row.append(matrix[i][index])
    return row

def rectabgleLoop(matrix, iterations):
    for i in range(int(iterations)):
        row_num = random.randrange(0, len(matrix))
        colum_num = random.randrange(0, len(matrix[0]))
        firstNum = matrix[colum_num][row_num]
        matrixPrint(matrix)
        print("row num= " + str(row_num))
        print("colum_num= " + str(colum_num))
        print("Num picked= " + str(firstNum))
        if firstNum == 1:
            row = makeRow(row_num, matrix, len(matrix[0]))
            print(row)