import random
print('Welcome to Hangman!')
wrong=0
HANGMANPICS = ['''
  
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
print('Lets play Hangman!')  
 

import random




# Insert the code from last exercise here.    

with open('wordbank.txt', 'r') as f:
  lines = f.readlines()
word=(random.choice(lines).strip())

guess = list(('_' * len(word)))
# Now ask the user to guess the word

while list(word) != guess:
  print(HANGMANPICS[wrong])
  print(' '.join(guess))
  
  letter=input("Guess a letter:").upper()
  
  if letter not in word:
    if wrong >= int(5):
      print(HANGMANPICS[wrong+1])
      print('Game Over')
      
      exit()
    else:
      print('incorrect')
      wrong+=1
  else:
      i = 0
      while i < len(word):
        if list(word)[i] == letter:
          guess[i] = letter
        i += 1

    
    

      
       
print('You\'re right! it\'s' , word + '.')  
