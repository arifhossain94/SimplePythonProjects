from random import randint


number = randint(1, 10)
# print("Cheat Code: ", number)
life = 3
print("Welcome Player!")
print("You have three chances to guess the correct number from 1 - 10...start!")
while life > 0:
    try:
        guess = int(input("Guess a number: "))
        if guess == number:
            print("You beat me AHHHHHHhhhhhhh....")
            break
        elif guess > number:
            print("Not bad!")
            life = life - 1
        else:
            life = life - 1
            print("HAH! That tickled!")

        if life == 0:
            print("You Lost!")
    except ValueError:
        print("Please enter a Number!\n")
