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
            # happened = False
            for i in range(difference):    
                if matrix[(x,y)] >= min + offset*i and matrix[(x,y)] <= min+offset*(i+1):
                    # happened = True
                    matrix[(x,y)] = min + offset*i
                # else:
                #     print(f"This one did not work, it was value {matrix[(x,y)]}, with value  ")
            # if  not happened:
            #     print("IT FAILED")
            #     print(f"max: {max}")
            #     print(f"min: {min}")
            #     print(matrix[(x,y)])
            #     return NameError
    for i in range(difference):
        print(min+ (i*offset))
            

    return matrix