from random import randint

# number variable will generate a random number from 1 - 10
number = randint(1, 10)
# print the value of the random number
# print("Cheat Code: ", number)

# Guess you have before you lose the game
life = 3
# Introductory for the game
print("Welcome Player!")
print("You have %s chances to guess the correct number from 1 - 10...start!" % life)
# Alternative formatter - index can be used within {}
# print("You have {} chances to guess the correct number from 1 - 10...start!".format(life))

# Keep running program until chances are exhausted
while life > 0:
    try:
        guess = int(input("Guess a number: "))
        if guess == number:  # Loop ends if the user enters correct number!
            print("You beat me AHHHHHHhhhhhhh....")
            break
        elif guess > number:
            print("Not bad! But WRONG!!!! ")
            life = life - 1  # remove a life if guess is wrong
        else:
            life = life - 1  # remove a life if guess is wrong
            print("HAH! That tickled! Try harder will you!!!! Muhuhahahahah!")

        if life == 0:  # Game over when life hits 0
            print("You Lost!")
    except ValueError:  # Will throw value exception if user input is not an integer type
        print("Please enter a Number!\n")  # Will resume input until user inputs integer
