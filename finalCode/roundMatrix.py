def roundMat(matrix, num):
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            matrix[(x,y)] = round(matrix[(x,y)], 0)
    min = 100
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix[(x,y)] < min:
                min = matrix[(x,y)]

    max = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix[(x,y)] > max:
                max = matrix[(x,y)]
    
    #This value defines how many possible values there could be
    difference = num
    offset = round((max - min)/difference,0)
      
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            for i in range(difference):    
                if matrix[(x,y)] >= min + offset*i and matrix[(x,y)] <= min+offset*(i+1):
                    matrix[(x,y)] = min + offset*i
    # for i in range(difference):
    #     print(min+ (i*offset))
            

    return matrix

def roundMatToBinary(matrix, num):
   
    # for x in range(len(matrix)):
    #     for y in range(len(matrix[0])):
    #         matrix[(x,y)] = round(matrix[(x,y)], 0)
    # min = 100
    # for x in range(len(matrix)):
    #     for y in range(len(matrix[0])):
    #         if matrix[(x,y)] < min:
    #             min = matrix[(x,y)]

    # max = 0
    # for x in range(len(matrix)):
    #     for y in range(len(matrix[0])):
    #         if matrix[(x,y)] > max:
    #             max = matrix[(x,y)]
    
    #This value defines how many possible values there could be
    difference = num
    # offset = round(((max) - min)/difference,0)
    # print(f"this is the max {max}")
    # print(f"this is the min {min}")
    # print(f"This is the offset {offset}")
    # if offset == 0:
    #     offset = 1
    max = 1
    min = -1 
    offset = 1
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            for i in range(difference):    
                if matrix[(x,y)] >= min + offset*i and matrix[(x,y)] <= min+offset*(i+1):
                    matrix[(x,y)] = min + offset*i
    # print("THis is the top")
    # print(matrix)
    # max = min + offset
    max = 0
    min = -1 
    offset = 1
    
    # print(matrix)
    # print("")

    # print("this is before binary")
    # print(matrix)
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            # print(f"This is the value {matrix[(x,y)]}")
            # print(max,min)
            if matrix[(x,y)] == max:
                # print("It is set to 1")
                matrix[(x,y)] = 1
            if matrix[(x,y)] == min:
                # print("It is set to 0")
                matrix[(x,y)] = 0
    # for i in range(difference):
    #     print(min+ (i*offset))
    # print("this is after")
    # print(matrix)

    return matrix