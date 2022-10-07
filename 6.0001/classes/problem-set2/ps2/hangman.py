# Problem Set 2, hangman.py
# Name:
# Collaborators: 
# Time spent: 6:27:49

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random

# sample_letters = ['a', 'b', 'c', 'd','e','f','g','h','i','j']
alphabet = 'abcdefghijklmnopqrstuvwxyz'
WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------
 
# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for letter in letters_guessed:
      if letter not in secret_word:
        return False
    return True
    


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far('_ ').
    '''
    guessed_word = ''
    for letter in secret_word:
      if letter not in letters_guessed:
        guessed_word += '_ '
      else: 
        guessed_word += letter
    return guessed_word

# print(get_guessed_word(choose_word(wordlist),sample_letters)) works
    



def get_available_letters(letters_guessed, alphabet = 'abcdefghijklmnopqrstuvwxyz'):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''    

    for letter in alphabet:
      if letter in letters_guessed and letter != "*":
        alphabet = alphabet.replace(letter, "")
    return alphabet
    
# print(get_available_letters(sample_letters, alphabet))# working
# print(alphabet)


def hangman(secret_word = "luan"):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
  
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game Hangman!")
    secret_word = "luan"
    letters_guessed = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    print(f"I am thinking of a word that is {len(secret_word)} letters long. \n ------------")
    guessed_remaining = 6
    found = False
    score = len(list(set(secret_word))) * guessed_remaining

    while not found:
      print(f"You have {guessed_remaining} guesses left.")
      print(f"Available letters: {alphabet}")

      while True:
        try:
          letter = input("Please guess a letter: ")

          if ((not letter.isalpha()) or len(letter) != 1):
            raise ValueError
          break      
        except ValueError:
            print('Please enter only a single letter.')

      if (letter in secret_word):
        guess_message = "Good guess: " 
      elif letter in letters_guessed:
        guessed_remaining -= 1
        print(f"Oops! You've already guessed that letter. You now have {guessed_remaining} warnings: ")
      else:
        guess_message = "Oops! That letter is not in my word: "
        guessed_remaining -= 1 if letter not in ['a', 'e', 'i', 'o', 'u'] else 2
      
      letters_guessed.append(letter.lower())
      alphabet = get_available_letters(letters_guessed, alphabet)

      print(guess_message, get_guessed_word(secret_word, letters_guessed)," \n ------------")


      if get_guessed_word(secret_word, letters_guessed) == secret_word:
        print("Congratulations, you won!")
        print(f"Your total score for this game is: {score}")
        found = True

        if input("PLAY AGAIN? (Y = Yes // N = No)").upper() == "Y": 
          hangman(choose_word(wordlist))  
        break 

      elif guessed_remaining == 0:
        print(f"Sorry, you ran out of guesses. The word was: '{secret_word}'")

        if input("TRY AGAIN? (Y = Yes // N = No)").upper() == "Y": 
          hangman(choose_word(wordlist))  
        break

      #when no more guesses
      
    
      
      




# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    
    my_word = my_word.replace("_ ", "_")
    if len(my_word) != len(other_word): return False
    match = True
    for letter in range(len(other_word)):
      if other_word[letter] != my_word[letter] and my_word[letter] != "_": 
        match = False
        break 
    return match 

# print(match_with_gaps("l_ a_ ","luan")) # works


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    possible_matches = ""
    for word in wordlist:
      if match_with_gaps(my_word, word):
        possible_matches += word + " "
    print(possible_matches) if possible_matches != "" else print("No matches found.")

# show_possible_matches("t_ _ t") #works


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game Hangman!")
    # secret_word = "luan"
    letters_guessed = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz*'
    print(f"I am thinking of a word that is {len(secret_word)} letters long. \n ------------")
    guessed_remaining = 6
    found = False
    score = len(list(set(secret_word))) * guessed_remaining

    while not found:
      print(f"You have {guessed_remaining} guesses left.")
      print(f"Available letters: {alphabet}")
      
      while True:
        try:
          letter = input("Please guess a letter: ")
          if (letter not in alphabet  or len(letter) != 1):
            raise ValueError
          break      
        except ValueError:
            print('Please enter only a single letter.')
      
      if letter == "*":
        show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        guess_message = ""
      elif letter in letters_guessed:
        guessed_remaining -= 1
        print(f"Oops! You've already guessed that letter. You now have {guessed_remaining} warnings: ")
        guess_message = ""
      elif (letter not in secret_word):
        guess_message = "Oops! That letter is not in my word: "
        guessed_remaining -= 1 if letter in "bcdfghjklmnpqrstvwxyz*" else 2
      else:
        guess_message = "Good guess: " 
      
      letters_guessed.append(letter.lower())
      alphabet = get_available_letters(letters_guessed, alphabet)
      print(guess_message, get_guessed_word(secret_word, letters_guessed)," \n ------------")
      if get_guessed_word(secret_word, letters_guessed) == secret_word:
        print("Congratulations, you won!")
        print(f"Your total score for this game is: {score}")
        found = True

        if input("PLAY AGAIN? (Y = Yes // N = No)").upper() == "Y": 
          hangman(choose_word(wordlist))  
        break 
      elif guessed_remaining == 0:
        print(f"Sorry, you ran out of guesses. The word was: '{secret_word}'")

        if input("TRY AGAIN? (Y = Yes // N = No)").upper() == "Y": 
          hangman(choose_word(wordlist))  
        break



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
