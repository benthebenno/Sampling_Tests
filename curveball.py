import random

def curveBallAlgo(init_matrix, iterations):
    for i in range(iterations):
        row_a = random.randrange(0,len(init_matrix))
        row_b = random.randrange(0,len(init_matrix))
      
        while row_a == row_b:
            row_b = random.randrange(0,len(init_matrix))
        print("row_a= " + str(row_a))
        print("row_b= " + str(row_b))
        a_b = []
        b_a = []
        V = []
       
        for k in range(len(init_matrix)):
            if init_matrix[k][row_a] == 1:
                if init_matrix[k][row_b] == 0:
                    a_b.append(k)
        for l in range(len(init_matrix)):
            if init_matrix[l][row_a] == 0:
                if init_matrix[l][row_b] == 1:
                    b_a.append(l)
        for item in b_a:
            if random.randrange(0,2) == 1:
                V.append(item) 
        if len(b_a) < len(a_b):
            continue
        print("a_b= " + str(a_b))
        print("b_a= " + str(b_a))
        print("V= " + str(V))

        for a in range(len(init_matrix)):
            if a in V:
                init_matrix[a][row_a] = 1
            if (((a in a_b) or a in b_a) and (not(a in V))):
                init_matrix[a][row_a] = 0
        for b in range(len(init_matrix)):
            if (((b in a_b) or b in b_a) and (not(b in V))):
                init_matrix[b][row_b] = 1
            if b in V:
                init_matrix[b][row_b] = 0
    return init_matrix