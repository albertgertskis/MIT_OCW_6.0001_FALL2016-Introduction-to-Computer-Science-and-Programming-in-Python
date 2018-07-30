# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

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
    # To see if all the letters in secret_word have been guessed, compared the
    # set of letters in the secret word to all the letters guessed. If the letters
    # in the secret word are a subset of the letters guessed (because there can be
    # more unique letters guessed than there are in the secret word), then the
    # secret word has been found.
    return set(secret_word).issubset(letters_guessed)
    


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''

    # Stores the formatted word that will be outputted to the user.
    # This word is consists of letters and underscores.
    # Underscores signify a letter that has not been guessed yet.
    letters_guessed_list = []

    # For each letter in the secret word, check to see if it is in the
    # letters guessed list.
    for letter in secret_word:
        # If the current letter is in the letters guessed by the user, display
        # all instances of that letter in the secret word to the user.
        if letter in letters_guessed:
            letters_guessed_list.extend([letter, ' ']) # Use extend because append cannot add two values to a list at a time. A space needs to be added for readability.
        # If the current letter is not in letters guessed by the user, display
        # an underscore in the place of that letter.
        else:
            letters_guessed_list.append("_ ")

    return "".join(letters_guessed_list)
                    


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    
    # Create list to store letters that haven't been guessed yet
    # and present those letters to the user when asked.
    letters_not_guessed = []
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            letters_not_guessed.append(letter)
            
    return "".join(letters_not_guessed)
    
    

def hangman(secret_word):
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
    guesses_left = 6
    warnings_left = 3
    letters_guessed = []
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is %d letters long." % len(secret_word))
    print("You have %d warnings left." % warnings_left)

    # If the user has guesses left and word isn't guessed yet, let them
    # make another guess.
    while guesses_left >= 0 and is_word_guessed(secret_word, letters_guessed) is False:
        print("-------------")
        if guesses_left > 1 or guesses_left == 0:
            print("You have %d guesses left." % guesses_left)
        else:
            print("You have 1 guess left.")
        print("Available letters:", get_available_letters(letters_guessed))
        user_letter_guess = str.lower(input("Please guess a letter: "))
        
        # If the user guessed a letter from the word correctly and the letter 
        # is guessed was not chosen already, don't decrease the value of 
        # guesses_left, tell the user it was a good guess, and display to the 
        # user the secret word, with correctly guessed letters displayed and 
        # unguessed letters replaced with an underscore.

        # If the guessed letter is in the alphabet, continue
        if user_letter_guess.isalpha():
            if user_letter_guess not in letters_guessed:
                letters_guessed.append(user_letter_guess)
                # If the guessed letter is in the secret word, continue
                if user_letter_guess in secret_word:
                    # Reveal all instances of the letter just guessed
                    # in the secret word.
                    print("Good guess:", get_guessed_word(secret_word, letters_guessed))
                # If the guessed letter hasn't been guessed yet, add it to the
                # letters guessed and tell user it was a good guess.
                # If the guessed letter is not in the secret word, user
                # loses either 1 or 2 guesses depending on whether the
                # letter was a vowel or a consonant
                else:
                    print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
                    letters_guessed.append(user_letter_guess)
                    # If the letter guessed is incorrect and a vowel, the user loses 2 guesses
                    if user_letter_guess in 'aeiou':
                        guesses_left -= 2
                    # If the letter guesses is incorrect and a consonant, the user loses 1 guess
                    else:
                        guesses_left -= 1
            else:
                warnings_left -= 1
                if warnings_left > 1 or warnings_left == 0:
                    print("Oops! You've already guessed that letter. You have %d warnings left:" % warnings_left,
                          get_guessed_word(secret_word, letters_guessed))
                elif warnings_left == 1:
                    print("Oops! You've already guessed that letter. You have 1 warning left:",
                          get_guessed_word(secret_word, letters_guessed))
                else:
                    print("Oops! You've already guessed that letter. "
                          "You have no warnings left so you lose one guess:",
                          get_guessed_word(secret_word, letters_guessed))
                    guesses_left -= 1
        # If the guessed letter is not in the alphabet, warn user if warnings remain.
        # Otherwise, user loses one guess.
        else:
            warnings_left -= 1
            if warnings_left > 1:
                print("Oops! That is not a valid letter. You have %d warnings left:" % warnings_left, get_guessed_word(secret_word, letters_guessed))
            elif warnings_left == 1:
                print("Oops! That is not a valid letter. You have 1 warning left:", get_guessed_word(secret_word, letters_guessed))
            else:
                print("Oops! That is not a valid letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
                guesses_left -= 1

    #####################################
    #        GAME IS NOW OVER           #
    #####################################

    # If user guessed the word, print a congratulatory
    # message and tell the user their total score. The total score
    # is the (number of guesses remaining * unique letters) in the
    # secret word
    total_score = guesses_left * len(set(secret_word))
    if is_word_guessed(secret_word, letters_guessed) is True:
        print("\nCongratulations, you won!\nYour total score for this game is: %d" % total_score)
    # If the word wasn't guessed
    else:
        print("\nSorry, you ran out of guesses. The word was %s." % secret_word)


# When you've completed your hangman function, scroll down to the bottom
#of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
