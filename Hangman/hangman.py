import random
import string

from words import word


def get_valid_word(word):
    word1 = random.choice(word)
    while '-' in word1 or ' ' in word:
        word1 = random.choice(word)
    return word1.upper()


def hangman():
    word2 = get_valid_word(word)
    word_letters = set(word2)
    alphabet = set(string.ascii_uppercase)
    used_letters =  set()
    while len(word_letters) > 0:
        print("You have used these letters: ', ' ".join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ','".join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet -used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print("You have already used that character. Please try again.")
        else:
            print("Invalid character.Please try again.")

user_input = input('Type something: ')
print(user_input)