import random
from matrixPrint import matrixPrint
def swapAlgo(init_matrix, iterations):
    for i in range(int(iterations)):
        # print("This is the iteration in the swap" + str(i))
        first_row = random.randrange(0, len(init_matrix))
        second_row = random.randrange(0, len(init_matrix))
        while first_row == second_row:
            second_row = random.randrange(0, len(init_matrix))
        
        first_collumn = random.randrange(0, len(init_matrix[0]))
        second_collumn = random.randrange(0, len(init_matrix[0]))
        while first_collumn == second_collumn:
            second_collumn = random.randrange(0, len(init_matrix[0]))

        #This makes sure first and second are ordered correctly

        if first_row > second_row:
            temp = first_row
            first_row = second_row
            second_row = temp

        if first_collumn > second_collumn:
            temp = first_collumn
            first_collumn = second_collumn
            second_collumn = temp
        # print("First index")
        # print(first_row)
        # print(first_collumn)
        # print("Second one")
        # print(second_row)
        # print(second_collumn)
        # print("")
        # print("Third")
        # print(second_row)
        # print(first_collumn)
        # print("fourth")
        # print(first_row)
        # print(second_collumn)  
        if init_matrix[first_row][first_collumn] == init_matrix[second_row][second_collumn]:
            if init_matrix[second_row][first_collumn] == init_matrix[first_row][second_collumn]:
                # print("A swap occured")
                first_num = init_matrix[first_row][first_collumn]
                second_num = init_matrix[second_row][first_collumn]

                #This is the actual swap
                init_matrix[first_row][first_collumn] = second_num
                init_matrix[second_row][second_collumn] = second_num
                init_matrix[second_row][first_collumn] = first_num
                init_matrix[first_row][second_collumn] = first_num
                # print(init_matrix)
    return init_matrix
