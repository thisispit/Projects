import random
from words_list import words
import string


def get_valid_word(words):
    words=random.choice(words)
    while '-' in words or ' ' in words:
        words=random.choice(words)
    return words.upper()

def hangman():
    word=get_valid_word(words)
    word_letter=set(word)
    alphabet=set(string.ascii_uppercase)
    used_letter=set()

    lives=6
    while len(word_letter)>0 and lives>0:

        #letter used
        print('You have ',lives ,'lives left \nused these letters: ', ' '.join(used_letter))

        #current word
        word_list=[letter if letter in used_letter else '_' for letter in word]
        print('Current word: ', ' '.join(word_list))

        #user input
        user_letter=input('\nGuess a letter: ').upper()
        if user_letter in alphabet-used_letter:
            used_letter.add(user_letter)
            if user_letter in word_letter:
                word_letter.remove(user_letter)
            
            else:
                lives -=1
                print('Letter is not in the word.')
        
        elif user_letter in used_letter:
            print('You have already used that character. Please try again.')
        
        else:
            print('Invalid character. Please try again.')
    
    if lives==0:
        print('You died, the word was: ',word)
    
    else:
        print('You guessed the word: ',word)


hangman()
