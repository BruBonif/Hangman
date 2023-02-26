import random

words = ['apple','banana','pear']

class hangman():

  def initialize(self,words):
    global word
    global table
    global repeated_words
    word = random.choice(words).lower()
    table = ['-'] * len(word)
    repeated_words = []
    return table,word,repeated_words

  def display_table(self,table):
    for slot in table:
      print(slot, end = '')

  def user_input(self):
    global letter
    letter = input("\nEnter the letter: \n")
    try:
      if ord('a') <= ord(letter) <= ord('z'):
        return letter

      elif letter in "1234567890":
        print('\nInvalid: Enter a letter\n')

      elif letter in "!$%&\'()*+,-./:;<=>?@[\\]^_`{|}~":
        print("\nInvalid: Symbols not allowed\n")
    except:
        print("\nError : Invalid input\n")

  def update_table(self,letter,word,table):
    for index,letter_word in enumerate(word):
      if letter_word == letter:
        table[index] = letter

  def check_win(self,table,lives):
    if '-' not in table:
      print("\nCongratulations, you win ")
      return True
    elif lives == 0:
      print("You lost all your lives")
      return True
    
    else:
      return False

  def game(self,words):
    lives = 5
    self.initialize(words)
    print("This is the hangame\n")
    print("You have 5 lives, don't waste them\n")
    self.display_table(table)
    while self.check_win(table,lives) == False:
      self.user_input()
      if letter in repeated_words:
        lives -= 1
        print(f"You repeated that word, {lives} live left")
        continue
      elif letter not in word:
        lives -= 1
        print(f'Wrong word, {lives} lives left')
        repeated_words.append(letter)
        continue
      else:
        print("Congrats!")
        repeated_words.append(letter)
        self.update_table(letter,word,table)
        self.display_table(table)
        continue
obj = hangman()

obj.game(words)
    

    
  
        
        
      
      


    

  



  