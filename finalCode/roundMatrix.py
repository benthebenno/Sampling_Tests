import struct
def roundMat(matrix, num, accountingForLoss):
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

    #This should not effect things but this represnts the bits lost by turning the max/min into binary
    if accountingForLoss:
        # print(f"This is the max before: {max} this is the min before: {min}")
        # min = int((bin(struct.unpack('!I', struct.pack('!f', min))[0])), base=2 )  
        # max = int(bin(struct.unpack('!I', struct.pack('!f', max))[0]), base=2)
        # print()
        # min = min & 0b11111111111111111111111111111000
        # max = max & 0b11111111111111111111111111111000
        # print(f"This is the max after: {max} this is the min after: {min}")
        #This estimate is overshooting my a lot, usally it manages to the 4/5 but gotta be safe
        min = round(min, 2)
        max = round(max, 2)
    
    #This value defines how many possible values there could be
    difference = num
    offset = (max - min)/difference
    # offset = round((max - min)/difference,0)

      
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

    for x in range(len(matrix)):
        for y in range(len(matrix)):
            matrix[x,y] = matrix[x,y]
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