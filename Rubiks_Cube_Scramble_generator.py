#Rubik's Cube Scramble generator
#12/18/2020 -- Katy Barrus

import random

moves = ['R', 'L', 'U', 'B', 'F', 'D', "R'", "L'", "U'", "B'", "F'", "D'"]
numberOfMoves = 25
sequence = []

'''
print(str(len(sequence)))
sequence += 'R'
print(str(len(sequence)))
print(sequence)
print(len(sequence) < numberOfMoves)

nextMove = moves[random.randint(0,11)]
lastMove = sequence[len(sequence)-1]
    
print("Last move: " + lastMove)
print("Next move: " + nextMove)
'''



while len(sequence) < numberOfMoves:
    
    #update variables
    nextMove = moves[random.randint(0,11)]
    #print("Next move: " + nextMove)
        
        
    #combine the same moves
    if len(sequence) > 0:
               
        lastMove = sequence[len(sequence)-1]
        #print("Last move: " + lastMove)
                
        if nextMove == lastMove:
            #print("These two moves are the same.")
            #print("Removing " + lastMove + "...")
            sequence.remove(lastMove)
        
            if nextMove in ['R', 'L', 'U', 'B', 'F', 'D']:
                #print("Changing " + nextMove + " to " + nextMove + "2...")
                nextMove = nextMove + "2"
            
            elif nextMove in ["R'", "L'", "U'", "B'", "F'", "D'"]:
                #print("Changing " + nextMove + "...")
                nextMove = nextMove.replace("'", "")
                nextMove = nextMove + "2"
                #print("The move is now " + nextMove + ".")
            
            else:
                print("Error -- move is not in list of moves")
        
        #if you have a "2" version of one move and then the same move after or before it
        elif nextMove in lastMove or ("'" in nextMove and nextMove - "'" in lastMove):
            #print("need to generate a new move")
            pass

        #if you have one move, and then an inverse of the same move
        elif nextMove == lastMove + "'":
            #print("need to generate a new move")
            pass

        elif nextMove + "'" == lastMove:
            #print("need to generate a new move")
            pass

        else:
            #add the next move
            sequence.append(nextMove)
    
    #print("Here is your current list of moves: ")
    #print(sequence)

                
                
    
    #check whether there are any moves that cancel each other out
    '''
    for letter in ['R', 'L', 'U', 'B', 'F', 'D']:
        if (letter in lastMove) and (letter in nextMove):
            
            #if you have the same move twice
            if nextMove == lastMove:
                print("These two moves are the same.")
                print("Removing " + lastMove + "...")
                sequence.remove(lastMove)
        
                if nextMove in ['R', 'L', 'U', 'B', 'F', 'D']:
                    print("Changing " + nextMove + " to " + nextMove + "2...")
                    nextMove = nextMove + "2"
            
                elif nextMove in ["R'", "L'", "U'", "B'", "F'", "D'"]:
                    print("Changing " + nextMove + "...")
                    nextMove = nextMove.replace("'", "")
                    nextMove = nextMove + "2"
                    print("The move is now " + nextMove + ".")
            
                else:
                    print("Error -- move is not in list of moves")
             
            #Other scenarios:
            #if you have a "2" version of one move and then the same move after or before it
            #if you have one move, and then an inverse of the same move
        
            #In both cases, generate a new move    
            else:
'''
    
    
print("Here is your final list of moves: ")
for letter in sequence:
    print(letter, end = " ")


'''
for i in sequence:
    print(sequence[int(i)] + '\n')
'''