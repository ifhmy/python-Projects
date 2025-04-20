import random

while True:
    want_play = input("Do you want to play the guessing game? (yes/no): ").strip().lower() 

    if want_play == "yes":
        print("Welcome to the Guessing Game!")

        choose = input("Choose a number between 1 and 10: ")
        if int(choose) <= 0 or int(choose) >= 11:
            print("Invalid number, please choose a number between 1 and 10.")
        else:
            print("You chose: " + choose)
            pc = random.randint(1, 10)
            print("PC chose: " + str(pc))
            if int(choose) == int(pc):
                print("You win!")
            else:
                print("You lose!") 

    elif want_play == "no":
        print("Okay, maybe next time!")
        exit()
    else:
        print("invalid input, please enter yes or no only")
        

