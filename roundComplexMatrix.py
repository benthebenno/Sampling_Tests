
def roundCM(matrix, split):
    min = 100 
    max = -100

    #This finds the max and min values of the matrix
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix[x,y] > max:
                max = matrix[x,y] 
            if matrix[x,y] < min:
                min = matrix[x,y] 
    print("min/max")
    print(min)
    print(max)
    diff = max - min
    possible_values = []

    for i in range(split):
        possible_values.append(min + diff*i)


    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            for i in range(split-1):
                # print(i)
                # print(f"This is the matrix value: {matrix[x,y]}")
                # print(f"This is the possible value at i: {possible_values[i]}")
                # print(f"This is the possible value at i+1: {possible_values[i+1]}")
                if matrix[x,y] >= possible_values[i] and matrix[x,y] <= possible_values[i+1]:
                    # print("triggered")
                    matrix[x,y] = possible_values[i]
    print("Matrix:")
    print(matrix)
    print("")
    print("Possible Values")
    print(possible_values)
    

    return matrix