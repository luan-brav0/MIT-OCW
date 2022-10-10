# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

# TODO - finish play_game; clean code (delete "remove!")


import math
import random
import re
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*': 0
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

# TODO - Remove!
word_list = load_words()

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	
# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, hand_lenth):
    """Assumes str "word" and in "hand_length";
    Returns int "word_score".

    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand_length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    word = word.lower()   # Cleans input to only lower chars.
    first_component = 0  # One of the score parameters to be evaluated, this one representing the score of the word played.
    word_dict = get_frequency_dict(word) # Creates dict with keys of letters in word and value the amount of such letter in the word. 
    
    # Implementing first component.
    for letter in word_dict:
        first_component += word_dict[letter] * SCRABBLE_LETTER_VALUES[letter]
    
    # The other component evaluated to return score, this one representing by the "(7*len(word) - 3 * (n - len(word)))" or "1", whichever is greater.
    if (7*len(word) - 3 * (hand_lenth - len(word))) > 1:    
        second_component = (7*len(word) - 3 * (hand_lenth - len(word)))  
    else:
        second_component = 1

    # Multiply componets to get score, returns.
    word_score = first_component * second_component
    return word_score

# TODO - REMOVE!
# get word score print test with word 'banana' and value 
# print('Get banana score:', get_word_score('banana',2)) # out: 432 (nice number btw)

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand, ending = ' '):
    """Assumes dict "hand"; 
    Returns list of chars "hand_letters".

    Displays (prints) the letters currently in the hand

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    Returns hand_letters: list (string)
    """
    hand_letters = []
    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=ending)
            hand_letters.append(letter)      # Prints all on the same line
    print()
    return hand_letters                              # Prints empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def shuffle_hand(hand):
    """Assumes dict hand
    Returns shuffled dict d (string -> int)
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)"""
    d = hand
    l = list(d.items())
    random.shuffle(l)
    d = dict(l)
    return d

def deal_hand(n):
    """
    Assumes int "n";
    Returns list "hand" 
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    print("Shuffling hand...")
    hand = {}
    # number of letter vowels. Hand has 1/3 of of vowels, one beign the wild card "*"
    num_vowels = int(math.ceil((n / 3)))
    hand['*'] = 1 # Adding wildcart
    for i in range(num_vowels - 1): # 2 vowels plus the "*" = 3 vowels = num_vowels
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    for i in range(num_vowels, n):    # i.e: from 3 to 7; Fills the rest of the hand
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    hand = shuffle_hand(hand)
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Assumes dict "hand" (str -> int), lower cap. string "word";
    Returns dict hand (str -> int).

    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    updated_hand = hand.copy()
    word = word.lower()
    print("Updating hand...")
    
    word_dict = get_frequency_dict(word) # String to dictionary.
    for letter in word_dict.keys():
        if letter in updated_hand and updated_hand[letter] - word_dict[letter] <= 0:
            updated_hand.pop(letter)
        elif letter in updated_hand.keys():
            updated_hand[letter] -= 1
    return updated_hand
# print (update_hand('quail', {'a': 1, 'q': 1, 'l': 2, 'm': 1, 'u': 1, 'i': 1}))

# TODO - REMOVE!
# Testing update_hand function: 
# print(update_hand({'h': 1, 'e': 1, 'l': 2, 'o': 1, 'a': 2}, 'hello'))
#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    '''
    IGNORE - implementation wildcards
    at git word score, check for *
    if yes, search regex with vowels in word
    if more than one word shows as possible result, evaluate word points for each and pick one of the largest (reorder list and pick at index 0)
     check for highest point word 

    word: string
    hand: dictionary (string -> integer)
    word_list: list
    '''
    word = word.lower()
    str_word_list = ' '.join(str(w) for w in word_list)
    word_dict = get_frequency_dict(word)
    word_in_hand = True
    for letter in word_dict.keys(): # for letters in word
        # Check if player the letter, and if has enough of them 
        if letter not in hand.keys() or word_dict[letter] > hand[letter]:
            word_in_hand = False
            break


    wild_in_list = False
    if "*" in word:
        if re.search('.+'+word.split('*')[0]+'.+'+r'[aeiou]'+'.+'+word.split('*')[1]+'.+', str_word_list):
            wild_matches = re.findall('.+'+word.split('*')[0]+'.+'+r'[aeiou]'+'.+'+word.split('*')[1]+'.+', str_word_list)
            wild_in_list = True   # word with wildcard matches a word in word_list

    
    return ((word in word_list) or wild_in_list) and word_in_hand

print('B*nana valid:',is_valid_word('b*nana',{'a': 3, 'b': 2,'n':2, '*':1 }, word_list))
#
# Problem #5: Playing a hand
#
def get_hand_len(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string -> int) 
    returns: integer
    """
    return sum(hand.values())
       
def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
    """
    
    # BEGIN PSEUDOCODE <-- Remove this comment when you implement this function
    # Keep track of the total score
    score = 0
    # As long as there are still letters left in the hand:
    while get_hand_len(hand) > 0:
        # Display the hand
        print('Hand:',display_hand(hand))
        # Ask user for input
        word = input("Choose word ('!!' to say you're done): ").lower()
                
        # If the input is two exclamation points:
        if word == "!!":
            print('\t!!\n\tEnding hand...')
            # End the game (break out of the loop)
            break            
        # Otherwise (the input is not two exclamation points):
        else:
            # If the word is valid:
            if is_valid_word(word, hand, word_list):
                # Tell the user how many points the word earned,
                word_score = get_word_score(word, get_hand_len(hand))
                print(f'{word} gets you more {word_score} points')
                # and the updated total score
                score += word_score
                print('Total score:', score)
            # Otherwise (the word is not valid):
            else:
                # Reject invalid word (print a message)
                print('Invalid word!')
                print('Total score:', score)

            # update the user's hand by removing the letters of their inputted word
            update_hand(hand, word)
    # Game is over (user entered '!!' or ran out of letters), 
    print('Done with hand...')
    # so tell user the total score
    print(f"Total hand score: {score}")
    # Return the total score as result of function
    return score
#
# Problem #6: Playing a game
# 
#
# procedure you will use to substitute a letter in a hand
#
def substitute_hand(hand, letter):
    """ 
    Assumes dict hand and str letter;
    Returns substituted_hand.

    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    updated_hand = hand.copy()
    if letter not in updated_hand:
        print(f"No such letter '{letter}' in hand {display_hand(updated_hand)}. Hand unchanged!")
        return updated_hand
    else:
        alphabet = VOWELS + CONSONANTS
        new_letter = alphabet[random.randint(0,len(alphabet) - 1)]
        print(f"Changing letter {updated_hand[letter]} letter(s) '{letter}'...\n for {updated_hand[letter]} letter(s) '{new_letter}'!")
        value = updated_hand[letter]
        updated_hand.pop(letter)
        updated_hand[new_letter] = value
        return updated_hand
   
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to'
     substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    print("WELCOME TO WORD.PY GAME")
    print(f"Rules:\n\tYou, the player, will have a hand of {HAND_SIZE} letters and you must try to make as many points by making words with such hand of letters.\n\tYou may have a wild card in your hand represented by the '*' sign. You may use it as any vowel in a word, but it will have no contribution to your score.\n\tDo you know as many words as your friends? Try to get the highest total score!")

    numhands = int(input("Enter total number of hands: "))
    hands = []
    score = 0
    for hand in range(0,numhands):
        hands.append(deal_hand(HAND_SIZE))
        
    h = 1 # hand counter/index
    for hand in hands:
        print (f"Hand {h}:", display_hand(hand))
        h += 1 
        substitute = True if input('Would you like to substitute a group of letters (Y/N, default N)? :').upper() == 'Y' else False
        if substitute:
            letter = input("Which letter would you like to replace: ").lower()
            hand = substitute_hand(hand, letter)
        else:
            print("\tNo substitution.")

        print() # empty line

        keep_hand = True
        while keep_hand == True:
            print()
            hand_score = play_hand(hand, word_list)
            keep_hand = True if input('Would you like to play again with this hand (Y/N, default N)?').upper() == 'Y'  else False
        score += hand_score
        print("\n\tCurrent total score:", score,'\n\t')

    print("\n\tNo more hands!\n\t\t GAME OVER!")
    print("Total score:", score)


            

        
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
