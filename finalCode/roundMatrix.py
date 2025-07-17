import struct

#This take in a matrix and some helper information, and returns a matrix with only num unique values (rounding each one to the closest)
def roundMat(matrix, num, accountingForLoss):
    #This loop rounds each value in the matrix to a whole integer, this is useful as if the numbers are too small sometimes they all become zero
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            matrix[(x,y)] = round(matrix[(x,y)], 0)
            
    #These two loops find the max and min values
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

    #This should not effect things much but this represents the bits lost by turning the max/min into binary
    if accountingForLoss:
        min = round(min, 2)
        max = round(max, 2)
    
    #This value defines how many possible values there could be
    difference = num

    #This offset is how the values between max and min are calculated
    offset = (max - min)/difference
      

    #This loop goes through each value in the matrix, and sets the value to whichever of the options it is closed too (lower first)
    #This part could probably be made more efficient which would cut down on errors
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            for i in range(difference):    
                if matrix[(x,y)] >= min + offset*i and matrix[(x,y)] <= min+offset*(i+1):
                    matrix[(x,y)] = min + offset*i 
  

    #This returns the options in an array
    options = []
    for i in range(difference):
        options.append(min+offset*i)

    return (matrix, options)
