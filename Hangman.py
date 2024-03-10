#This is a hangman game made by Fares Mohammed id:20230278
#description of the game: it is a game where a randon word is chosen
#the word letter number is displayed to the user, the user then takes
#turns trying to guess the word letter by letter until he wins
#user only has 7 lives


word_list = ["apple", "banana", "carrot", "dog", "elephant", "fish", "giraffe", "house", "igloo", "jacket", "kangaroo",
             "lion", "monkey", "napkin", "orange", "penguin", "quilt", "rabbit", "snake", "tiger", "umbrella", "violin",
             "whale", "xylophone", "yacht", "zebra"]
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

import random


def hangman():
    end_of_game = False
    lives = 6

    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)

    # Create blanks
    display = []
    for _ in range(word_length):
        display += "_"

    while not end_of_game:
        guess = input("Guess a letter: ").lower()

        if guess in display:
            print(f"You've already guessed {guess}")

        # Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
            if letter == guess:
                display[position] = letter

        # Check if user is wrong.
        if guess not in chosen_word:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")

            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")
                return

        # Join all the elements in the list and turn it into a String.
        print(f"{' '.join(display)}")

        # Check if user has got all letters.
        if "_" not in display:
            end_of_game = True
            print("You win.")
            return

        print(stages[lives])


def main():
    print(logo)
    while True:
        print("-------MAIN MENU-------")
        print("Choose from the following:\nA)Play a match\nB)Exit")
        choice = input().lower()
        if choice == "a":
            hangman()
        elif choice == "b":
            print("Exiting...")
        else:
            print("Invalid choice.")


main()
