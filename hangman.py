# script to play the hangman game with user from a list of words to guess in the list


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
=========
''', '''
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

from dis import dis
import random
import clear
# words = ['watermelon', 'pineapple', 'apple', 'orange', 'banana', 'mango', 'pear','kiwi', 'peach']
from wordlist import words 
end_of_game = False
counter = 6

choosen_word = random.choice(words)
# print(choosen_word)

word_length = len(choosen_word)


display = []
for aplha in choosen_word:
    display += '_'

print(display)
while not end_of_game:
    guess_letter = input('Guess a letter: ').lower()
    for position in range(word_length):
        letter = choosen_word[position]
        # print(letter)
        if guess_letter == letter:
            display[position] = letter
    print(display)
    
    if guess_letter not in choosen_word:
        counter -= 1
        print(counter)
        if counter == 0:
            end_of_game = True
            print('You Loose')
    if '_'not in display:
        end_of_game = True
        print("You Win")

    print(stages[counter])