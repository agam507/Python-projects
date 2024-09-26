import random 
 
print("Hi welcome to the game, This is a number guessing game.\nYou got 5 chances to guess the number. \nLet's start the game") 
 
num_guess = random.randrange(100) 
chance=5 
guess=0 
 
for x in range(6): 
    if guess < chance: 
        guess+=1 
        ur_guess = int(input('Enter number: \n')) 
     
        if ur_guess == num_guess: 
            print("Chance", guess) 
            print('You guessed it right \nThe number was',num_guess) 
            break 
        elif ur_guess < num_guess: 
            print("Chance", guess) 
            print('Too small') 
        elif ur_guess > num_guess: 
            print("Chance", guess) 
            print('Too big') 
    else: 
        print('You lost.\nThe number was',num_guess) 
        print('\nNo chances left \nBetter Luck Next Time')