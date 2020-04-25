from random import randint  # Will be used to generate a random number
import re  # Will use regex expression to validate the user guess input

"""
Hangman is a word guessing game. 
The player must guess the right word within a certain amount of tries.
"""


class Hangman:
    # Open and read a selection of word list to generate a random word
    try:
        with open("input/random_english_words.txt", "r") as words:
            dictionary = words.readlines()
    except FileNotFoundError:
        print("Check File Path!")
    finally:
        words.close()

    dictionary_list = []
    for word in dictionary:
        dictionary_list.append(word.replace("\n", ""))

    __dictionary_size = len(dictionary_list)

    __guesses_left = 6
    __random_word = dictionary_list[randint(1, __dictionary_size)]
    print("cheat: ", __random_word)
    random_word_char_list = [i for i in __random_word.replace(' ', '')]
    len_of_random_word = len(__random_word)
    print("Guess the Word: ", "_ " * len_of_random_word, "\n")

    right_guessed_word = ['False'] * len_of_random_word
    print("Random Word: ", random_word_char_list)
    print("Guessed Word: ", right_guessed_word)

    def start_game(self):
        print("Welcome to hangman!")
        print("You have %s tries make sure you make it count!" % self.__guesses_left)
        while self.__guesses_left > 0:
            try:
                user_guess = str(input("Please guess a letter: ")).lower()
                pattern = re.compile("^([a-zA-Z])$")  # Checking if the char is alphabet only
                if len(user_guess) > 1 or not pattern.match(user_guess):
                    raise ValueError
                else:
                    game_won = self.check_letter(user_guess)
                    if game_won:
                        print("Congratulation! You've Won!\nGuessed Word: %s" % self.__random_word)
                        break
            except ValueError:
                print("Invalid Entry!")

    def check_letter(self, character):
        game_won = True

        indexes = [i for i in range(0, len(self.random_word_char_list)) if character in self.random_word_char_list[i]]
        for i in indexes:
            self.right_guessed_word[i] = character

        if self.random_word_char_list == self.right_guessed_word:
            return game_won

        if len(indexes) >= 1:
            self.__get_game_status()
        elif len(indexes) == 0:
            self.__guesses_left = self.__guesses_left - 1
            if self.__guesses_left == 0:
                print("Sorry you lost!")
            else:
                print("Wrong Guess!")

    def __get_game_status(self):
        for i in self.right_guessed_word:
            if "False" in i:
                print("_", end=' ')
            else:
                print(i, end=' ')
        print("\n")


new_game = Hangman()
new_game.start_game()

