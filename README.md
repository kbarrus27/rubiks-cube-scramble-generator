# Rubik's Cube Scramble Generator
A simple Python program that generates a sequence of Rubik's Cube moves: Right, Left, Up, Down, Front, Back, and their inverses (designated with an ' character).
- You will need the random module to run this program.
- The default length of the sequence is 25 moves, but you can change that by editing numberOfMoves in line 7.

### Known issues:
- Sometimes you'll get a move and its inverse right next to each other, like R and R'. Technically, these moves would cancel each other out.
- You might end up with a "2" move and the same move right next to it, like this: R2 R. Technically, this is the same as R'.
