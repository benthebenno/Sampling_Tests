
def roundCM(matrix):
    min = 100 
    max = -100

    #This finds the max and min values of the matrix
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix[x,y] > max:
                max = matrix[x,y] 
            if matrix[x,y] < min:
                min = matrix[x,y] 

    occurance = {}

    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix[x,y] in occurance:
                occurance[matrix[x,y]] += 1
            else:
                occurance[matrix[x,y]] = 1

# This is where I got this function https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    sortedDict = sorted(occurance.items(), key= lambda x: x[1], reverse=True)
    print(sortedDict)
