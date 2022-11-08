import random

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


# Set up winning word and blanks
possible_words = ['peetowel', 'boogersoup', 'poopbucket', 'buttwater']
winning_word = random.choice(possible_words)
blanks = []
for letter in range(0, len(winning_word)):
    blanks.append("-")
print('WELCOME TO HANGMAN')


chances = 0
didWin = False
#Game Loop
while chances < 6:
    isCorrect = False
    player_guess = input('Guess a letter: ').lower()
    #check to see if guess is correct and replace blanks with letters
    for num in range(0, len(winning_word)):
        if player_guess == winning_word[num]:
            blanks[num] = player_guess
            isCorrect = True
    print(HANGMANPICS[chances])
    if blanks.count('-') == 0:
        didWin = True
        break
    if not isCorrect:
        chances += 1
        print(HANGMANPICS[chances])
    print(" ".join(blanks))

#End game function
if didWin == True:
    print(f"You Win! The word was {winning_word}")
else: 
    print(f"Game Over, you lose. The word was {winning_word}")
     
 
