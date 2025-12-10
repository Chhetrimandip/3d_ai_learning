def threexthree(f,s):
    t= [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]

    for i in range(0,3):
        for j in range(0,3):
            for k in range(0,3):
                t[i][j]+=f[i][k]*s[k][j] 
    return t

matrix_a = [
    [10, 20, 0],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_b = [
    [2, 0, 0],  # This looks like it might scale the X axis by 2
    [0, 2, 0],  # Scale Y by 2
    [0, 0, 2]   # Scale Z by 2
]
print(threexthree(matrix_a,matrix_b))