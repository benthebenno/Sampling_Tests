import random
from swapAlgo import swapAlgo
from matrixPrint import matrixPrint
from rectangleLoop import rectabgleLoop
from curveball import curveBallAlgo
def hasSameSums(firstM, secondM):
    if len(firstM) != len(secondM):
        return False
    if len(firstM[0]) != len(secondM[0]):
        return False
    
    for x in range(len(firstM)):
        firstSum = 0
        secondSum = 0
        for y in range(len(firstM[0])):
            firstSum += firstM[x][y] 
            secondSum += secondM[x][y]
        if firstSum != secondSum:
            return False
    for y in range (len(firstM[0])):
        firstSum = 0
        secondSum = 0
        for x in range(len(firstM)):
            firstSum += firstM[x][y]
            secondSum += secondM[x][y]
        if firstSum != secondSum:
            return False
    return True

def swapAlgoTests(iterations):
    for i in range (2, iterations):
        print("It has made it to matrix of size: " + str(i) )
        rows, cols = (i, i)
        matrix = [[0 for i in range(cols)] for j in range(rows)]

        rows, cols = (i, i)
        saved_matrix = [[0 for i in range(cols)] for j in range(rows)]

        for x in range(i):
            for y in range(i):
                new_num = random.randrange(0,2)
                matrix[x][y]= new_num
                saved_matrix[x][y] = new_num
        newMatrix = rectabgleLoop(matrix, 5000)
        if hasSameSums(saved_matrix,newMatrix):
            if saved_matrix == newMatrix:
                print("For this size the matrix are identical")
            continue
        else:
            print(saved_matrix)
            print(newMatrix)
            return False
    return True

def rectangleLoopTest(iterations):
    for i in range (2, iterations):
        print("It has made it to matrix of size: " + str(i) )
        rows, cols = (i, i)
        matrix = [[0 for i in range(cols)] for j in range(rows)]

        rows, cols = (i, i)
        saved_matrix = [[0 for i in range(cols)] for j in range(rows)]

        for x in range(i):
            for y in range(i):
                new_num = random.randrange(0,2)
                matrix[x][y]= new_num
                saved_matrix[x][y] = new_num
        newMatrix = swapAlgo(matrix, 5000)
        # print(newMatrix)
        # print(matrix)
        if hasSameSums(saved_matrix,newMatrix):
            if saved_matrix == newMatrix:
                print("For this size the matrix are identical")
            # matrixPrint(saved_matrix)
            # matrixPrint(matrix)
            # print("Start of new")
            # matrixPrint(newMatrix)
            # print("")
            continue
        else:
            print(saved_matrix)
            print(newMatrix)
            return False
    return True

def curveTest(iterations):
    for i in range (2, iterations):
        print("It has made it to matrix of size: " + str(i) )
        rows, cols = (i, i)
        matrix = [[0 for i in range(cols)] for j in range(rows)]

        rows, cols = (i, i)
        saved_matrix = [[0 for i in range(cols)] for j in range(rows)]

        for x in range(i):
            for y in range(i):
                new_num = random.randrange(0,2)
                matrix[x][y]= new_num
                saved_matrix[x][y] = new_num
        newMatrix = curveBallAlgo(matrix, 5000)
        # print(newMatrix)
        # print(matrix)
        if hasSameSums(saved_matrix,newMatrix):
            if saved_matrix == newMatrix:
                print("For this size the matrix are identical")
            # matrixPrint(saved_matrix)
            # matrixPrint(matrix)
            # print("Start of new")
            # matrixPrint(newMatrix)
            # print("")
            continue
        else:
            print(saved_matrix)
            print(newMatrix)
            return False
    return True

number= int(input("For these tests up to how large do you want the matrices to be?"))

if swapAlgoTests(number):
    print("swapAlgoTests Sucessful")
else:
    print("):")

if rectangleLoopTest(number):
    print("rectangle Loop test Sucessful")
else:
    print("):")


if curveTest(number):
    print("Curveball algorithm test Sucessful")
else:
    print("):")


