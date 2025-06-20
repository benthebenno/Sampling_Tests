def round(matrix):
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix [(x,y)] < 0.5:
                matrix[(x,y)]=0
            else: 
                matrix[(x,y)]=1
    return matrix