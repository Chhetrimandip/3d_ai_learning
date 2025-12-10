
def validfinder():
ad    num = 8
    board = np.zeros((num,num), dtype=int)
    nomatch = False
    while nomatch == False:
        nomatch = True
        for i in range(8):
            for j in range(8):
                board[i][j] = 1
                for k in range(i-1,i+2):
                    if k>=8 or k<0: continue
                    for l in range(j-1,j+2):
                        if l >= 8 or l <0: continue
                        if board[k][l] == 1:
                            nomatch = False
                            board[i][j] = 0
                            print(f"I = {i} J = {j}")
                            break
                if nomatch == False:
    return board

print(validfinder())