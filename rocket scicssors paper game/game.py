#start the game 
# ask player to make a move ( r,p,s)
# pc will make a move automatically
# if pc == player > Tie 
# if (player == Paper and pc == Rock) or (player ==Scissors and pc == paper )or (player == Rock and pc == Scissors) > player wins
#you win 
# any other case 
## pc wins

import random
user = input("Welcome to Rock, Paper, Scissors! Choose your move (r for rock, p for paper, s for scissors): ").lower()

if user not in ['r', 'p', 's']:
    print("Invalid input. Please choose r, p, or s.")
    exit()
print("User choose: "+user)
pc = random.choice(['r', 'p', 's'])
print("PC choose: "+pc)

if user == pc:
    print("It's a tie!")
elif (user == 'r' and pc == 's') or (user == 'p' and pc == 'r') or (user == 's' and pc == 'p'):
    print("You win!")
else:
    print("You lose! PC wins.")