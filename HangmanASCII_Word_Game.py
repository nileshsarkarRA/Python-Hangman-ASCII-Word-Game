# Hangman Game Word Guess by Nilesh
import random

# ASCII Codes = 0-6
Hang_man_art = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words_to_be_guessed = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ')

def choose_word():
    return random.choice(words_to_be_guessed.split())

def display_word(word, guessed_letters):
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display+= "_"
    return display

def start_hangman():
    word_to_guess = choose_word()
    guessed_letters = set()
    attempts = 0
    

    while True:
        print(Hang_man_art[attempts])
        print(display_word(word_to_guess, guessed_letters))

        user_input = input("Guess a letter: ")
        guess= user_input.lower()

        if guess in guessed_letters:
            print("You already guessed that letter!")
        elif guess in word_to_guess:
            guessed_letters.add(guess)
            if display_word(word_to_guess, guessed_letters)== word_to_guess:
                print(f"Congratulations! You guessed the word Correctly!!!\nYour guess : {word_to_guess}")

                break
            else:
                guessed_letters.add(guess)
                attempts+=1
                if attempts>= len(Hang_man_art):
                    print(f"Sorry! You ran out of Attempts, Game Over! The word was {word_to_guess}")
                    break

if __name__ == "__main__":
    start_hangman()


