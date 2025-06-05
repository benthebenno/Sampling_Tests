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
        # matrixPrint(matrix)
        # print("row num= " + str(row_num))
        # print("colum_num= " + str(colum_num))
        # print("Num picked= " + str(firstNum))
        if firstNum == 1:
            row = makeRow(colum_num, matrix, len(matrix))
            secondNum = -1
            for i in row:
                if i == 0:
                    secondNum = i
            if secondNum == -1:
                print("no second number in row")
                continue
            second_colum = matrix[secondNum]

            thirdNum = -1
            for i in second_colum:
                if i == 1:
                    thirdNum = i
            if thirdNum == -1:
                print("No third number in colum")
                continue

            #this final part discovers if it is a checherboard
            if matrix[colum_num][thirdNum] == 0:
                #now to swap THIS REALLY SHOULD BE CHECKED
                print("it found a match")
                matrixPrint(matrix)
                print(str(colum_num)+"," + str(row_num))
                print(str(secondNum)+"," + str(thirdNum))
                print(str(second_colum)+"," + str(row_num))
                print(str(colum_num)+","+str(thirdNum))

                matrix[colum_num][row_num] = 0
                matrix[secondNum][thirdNum] = 0
                matrix[second_colum][row_num] = 1
                matrix[colum_num][thirdNum] = 1

        
