#Rubik's Cube Scramble generator

import random

moves = ['R', 'L', 'U', 'B', 'F', 'D', "R'", "L'", "U'", "B'", "F'", "D'"]
numberOfMoves = 25
sequence = []

while len(sequence) < numberOfMoves:

    #Generate a move
    nextMove = moves[random.randint(0,11)]
        
    #If this is the first move, add it to the list
    if len(sequence) < 1:
        sequence.append(nextMove)
    
    #If this isn't the first move:
    else:
        lastMove = sequence[len(sequence)-1]
       
        #Check to see if this and the last move are same "type" of move, like R and R' and R2
        if nextMove[0] == lastMove[0]: 
            
            #If lastMove and nextMove are the same (two Rs or two R's), change the prior move to its "2" version (R2)
            if nextMove == lastMove:
                sequence[len(sequence)-1] = lastMove[0] + '2'

            #Otherwise, don't do anything -- the program will pick a new move on its next loop
        
        #If this move and the last move are different "types" of moves, like R and L, add this move to the sequence
        else:
            sequence.append(nextMove)

print("Here is your final list of moves: ")
for letter in sequence:
    print(letter, end = "   ")
