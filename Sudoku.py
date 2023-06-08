import numpy as np
game = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,0,1,9,0,0,5],
        [0,0,0,0,0,0,0,0,0]]

def solution():
    global game
    #loopin 9x9 game
    for row in range(0,9):
        for col in range(0,9):
            #Checking for emply block (0 val)
            if game[row][col] == 0:
                for num in range(1,10):
                    if correctNumber(row,col,num):
                        game[row][col] = num
                        #continue solving 
                        solution()
                        #backtrack val to 0
                        game[row][col] = 0
                return
    print(np.matrix(game))
    input('More solutions...')

#Chceking for corrent number in block
def correctNumber(row,col,num):
    global game

    #Check for row
    for c in range(0,9):
        if game[row][c] == num:
            return False
    
    #Check for col
    for r in range(0,9):
        if game[r][col] == num:
            return False
        
    #check for square
    #getting starting row and col of square
    r0 = (row//3)*3    #0*3 1*3 2*3
    c0 = (col//3)*3 
    #looping 3x3 square
    for i in range(0,3):   
        for j in range(0,3):
            if game[r0+i][c0+j] == num:
                return False
            
    return True  # number is correct fit

solution()