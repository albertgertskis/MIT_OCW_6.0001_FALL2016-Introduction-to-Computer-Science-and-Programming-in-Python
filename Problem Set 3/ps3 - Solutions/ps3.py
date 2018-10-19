# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
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
def get_word_score(word, n):
    """
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
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    # Length of the word
    word_length = len(word)
    # Sum of the points for letters in the word
    first_score = 0

    # Get summed score of scrabble letter value for each letter in the word
    for letter in word:
        first_score += SCRABBLE_LETTER_VALUES[letter.lower()]

    # Get score based on word length played and number of cards remaining in hand
    second_score = (7 * word_length - 3 * (n - word_length))
    # This second score cannot be a value less than 1
    if second_score < 1:
        second_score = 1
    
    # Return the total score which is the product of scores 1 and 2 
    return first_score * second_score

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """

    hand={}
    # Subtract 1 from the number of vowels to allow one of the vowels to be
    # replaced with a wildcard
    num_vowels = int(math.ceil(n / 3)) - 1

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    # num_vowels + 1 because one of the letters in the hand will be a wildcard
    for i in range(num_vowels + 1, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    # Add the wildcard to the hand
    hand['*'] += 1

    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
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

    # Make a copy of the hand to remove letters from
    new_hand = dict(hand)

    # For every letter in the word
    for letter in word:
        # # If the letter exists in the hand

        ######################################################################################
        ########### REMOVE THIS IF ALL UNIT TESTS PASSED AND PROGRAM RUNS PROPERLY ###########
        #  if new_hand.get(letter.lower()) != None:                                          #
        #     # If that letter is still in the hand (the letter doesn't have a               #
        #     # count of 0 in the hand). This is added to make sure that if a                #
        #     # player makes a word that isn't valid with letters that they                  #
        #     # either don't have or use up too many of their hand's letters, the            #
        #     # value will not be less than 0                                                #
        ######################################################################################
        ######################################################################################
        
        if new_hand[letter.lower()] > 0:
            # Remove the current letter in the word from the "new" hand
            new_hand[letter.lower()] -= 1
        
    # Return the new hand containing only the remaining letters
    return new_hand


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
    lowercase_hand = dict(hand)
    lowercase_word = word.lower()

    # Store the different word possibilities that can be craated
    # with a wildcard
    wildcard_filled_words = []
    # The copy array is needed for when every word contained within
    # it is iterated over and removed if it is not in the word list.
    # If this array does not exist, when doing this iteration and removal,
    # words would be skipped over if the previous word was removed from the array
    wildcard_filled_words_copy = []

    # If the word has a wildcard in it
    if '*' in lowercase_word:
        # Find and save the location of the '*' in the string
        wildcard_location = lowercase_word.find('*')
        # For every vowel in the alphabet
        for letter in VOWELS:
            # Switch the wildcard for the current vowel and add it to the
            # array holding the different word possibilities that can be
            # created with that wildcard
            wildcard_filled_words.append(lowercase_word.replace('*', letter))
            wildcard_filled_words_copy.append(lowercase_word.replace('*', letter))
        # For every word in the wildcard replaced word list
        for wildcard_filled_word in wildcard_filled_words_copy:
            # If that word is not in the word list
            if wildcard_filled_word not in word_list:
                # Remove that word from the possible words
                wildcard_filled_words.remove(wildcard_filled_word)

        # If there are no wildcard-replaced words contained in the word list
        # return False
        if wildcard_filled_words == []:
            return False
        # Otherwise, if there are wildcard-replaced words contained in the word list
        else:
            # Test each word to see if it can be spelled using the given hand.
            for wildcard_filled_word in wildcard_filled_words:
                # For every letter in the wildcard-replaced word
                for index, letter in enumerate(wildcard_filled_word):
                    # If the current letter is the letter replacing the wildcard
                    if index == wildcard_location:
                        # Use the wildcard as the letter value to test if the
                        # word with the wildcard symbole can be spelled from the hand
                        letter = '*'
                        # If the letter does not exist in the hand, break to move
                        # on to the next word
                        if lowercase_hand.get(letter) == None:
                            # Remove the current wildcard-filled word from the
                            # wildcard-filled word list
                            wildcard_filled_words.remove(wildcard_filled_word)
                            # Reset the letter count in the hand for the next word
                            lowercase_hand = dict(hand)
                            break
                        # Otherwise, if the letter does exist in the hand (even with count 0)
                        else:
                            # If there is a count of less than 1 of that letter in the hand
                            if lowercase_hand[letter] < 1:
                                # Remove the current wildcard-filled word from the
                                # wildcard-filled word list
                                wildcard_filled_words.remove(wildcard_filled_word)
                                # Reset the letter count in the hand for the next word
                                lowercase_hand = dict(hand)
                                # That word cannot be created because the current hand does not
                                # have enough of that letter so break and move on to the next
                                # word
                                break
                            # Otherwise, if there is a count of 1 or more of that letter in the hand
                            else:
                                # Subtract 1 from that letter's count in that hand
                                lowercase_hand[letter] -= 1
            # If there is not wildcard-filled word that can be spelled using
            # the user's current hand, it not a valid word
            if wildcard_filled_words == []:
                return False
            # Otherwise, it is a valid word
            else:
                return True


    # If the word does not have a wildcard in it and is not in the word 
    # list, return False
    elif lowercase_word not in word_list:
        return False


    # For every letter in the word
    for letter in lowercase_word:
        # If the letter does not exist in the hand, return False
        if lowercase_hand.get(letter) == None:
            return False
        # Otherwise, if the letter does exist in the hand (even with count 0)
        else:
            # If there is a count of less than 1 of that letter in the hand
            if lowercase_hand[letter] < 1:
                # That word cannot be created because the current hand does not
                # have enough of that letter
                return False
            # Otherwise, if there is a count of 1 or more of that letter in the hand
            else:
                # Subtract 1 from that letter's count in that hand
                lowercase_hand[letter] -= 1

    # Return true if the word is in the word list and is entirely composed
    # of letters in the hand
    return True

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    
    pass  # TO DO... Remove this line when you implement this function

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
    
    # As long as there are still letters left in the hand:
    
        # Display the hand
        
        # Ask user for input
        
        # If the input is two exclamation points:
        
            # End the game (break out of the loop)

            
        # Otherwise (the input is not two exclamation points):

            # If the word is valid:

                # Tell the user how many points the word earned,
                # and the updated total score

            # Otherwise (the word is not valid):
                # Reject invalid word (print a message)
                
            # update the user's hand by removing the letters of their inputted word
            

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score

    # Return the total score as result of function



#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
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
    
    pass  # TO DO... Remove this line when you implement this function
       
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
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
    
    print("play_game not implemented.") # TO DO... Remove this line when you implement this function
    


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
