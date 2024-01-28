from wonderwords import RandomWord

GUESSED_LETTERS = []

def greet():
    print("Welcome to Hangman!")


def get_random_noun():
    return RandomWord().word(include_parts_of_speech=["nouns"])


def get_user_guess():
    while True:
        letter = input("Enter a letter: ").lower()
        if (len(letter) != 1) or (not letter.isalpha()):
            print("Invalid input.")
        elif letter in GUESSED_LETTERS:
            print("You already guessed this letter.")
        else:
            break
    return letter


def get_round_result(letter, word):
    GUESSED_LETTERS.append(letter)
    if letter in word:
        print(f"{letter.upper()} is in the word!")
    else:
        print(f"{letter.upper()} is not in the word!")


def end_round(word):
    current_string = ""
    end_game = True
    for letter in word:
        if letter in GUESSED_LETTERS:
            current_string += letter.upper()
        else:
            end_game = False
            current_string += "_"
    if end_game == True:
        print(f"You win! The word was {word.upper()}!")
    else:
        print(current_string)
        print(f"Guessed letters: {' '.join(sorted(GUESSED_LETTERS))}")
    print("--------------------")
    return end_game


def play_round(word):
    guess = get_user_guess()
    get_round_result(guess, word)
    return end_round(word)

def play_game():
    greet()
    word = get_random_noun()
    while True:
        if play_round(word) == True:
            break

play_game()


