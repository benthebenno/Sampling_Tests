def roundMat(matrix, num):
    # for x in range(len(matrix)):
        # for y in range(len(matrix[0])):
            # matrix[(x,y)] = round(matrix[(x,y)], 0)
            
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
    # offset = round((max - min)/difference,0)
    offset = (max - min)/difference

      
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            for i in range(difference):    
                # print(f"Matrix val = {matrix[x,y]}")
                # print(f"max: {max}")
                # print(f"min: {min}")
                if matrix[(x,y)] >= min + offset*i and matrix[(x,y)] <= min+offset*(i+1):
                    matrix[(x,y)] = min + offset*i
  
    options = []
    for i in range(difference):
        options.append(min+offset*i)
    return (matrix, options)

def roundMatToSeven(matrix, num):
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            count = 0 
            for n in num:
                if matrix[x,y] == n:
                    matrix[x,y] = count
                count += 1
    return matrix