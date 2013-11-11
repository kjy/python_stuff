# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "/Users/karenyang/Desktop/6.00.1x/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    if lettersGuessed == []:
        return False
    else:   
        for letter in secretWord:
            if letter in lettersGuessed:
                pass
            else:
                return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    slots=len(secretWord)
    palabra = slots*"_"
    if lettersGuessed == []:
        return palabra
    else:  
        lpalabra = list(palabra)
        for i in range(len(secretWord)):
            if secretWord[i] in lettersGuessed:
                lpalabra[i] = secretWord[i] 
            else:
                pass
    spalabra = ' '.join(lpalabra)            
    return spalabra
    
    
import string
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    available = string.ascii_lowercase
    available = list(available)
    for letter in lettersGuessed: 
        if letter in available:
            p = available.index(letter)
            del(available[p])
        else:
            pass
    notguessed = "".join(available)
    return notguessed
            

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''   
    lettersGuessed = []
    mistakesMade = 0
    availableLetters = "abcdefghijklmnopqrstuvwxyz"
    print ("Welcome to the game, Hangman!")
    lenword = len(secretWord)
    print ("I am thinking of a word that is " + str(lenword) + " letters long.")
    guesses = 8
    while guesses > 0:
        print ("You have " + str(guesses) + " guesses left.")
        print ("Available letters: " + getAvailableLetters(lettersGuessed))
        letter = raw_input("Please guess a letter: ")
        ll = letter.lower()
        if not (ll in lettersGuessed):
            lettersGuessed.append(ll)
            guesses -=1
        else:
            print ("Oops! You've already guessed that letter: " + getGuessedWord(secretWord,lettersGuessed))
        if ll in secretWord:
            print ("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
            if isWordGuessed(secretWord, lettersGuessed)==True:
                print ("Congratulations, you won!")
            else:
                pass
        else:
            mistakesMade -= 1
            guesses -=1
            print ("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
                          
    print ("Sorry, you ran out of guesses.  The word was " + secretWord)

             


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
 #secretWord while you're testing)
#secretWord = 'sea'               #Hardcode a specific keyword or generate a random one on next line
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)


"""
test
%run /Users/karenyang/Desktop/6.00.1x/ps3_hangman.py
Loading word list from file...
   55909 words loaded.
Welcome to the game, Hangman!
I am thinking of a word that is 7 letters long.
You have 8 guesses left.
Available letters: abcdefghijklmnopqrstuvwxyz

Please guess a letter: t
Oops! That letter is not in my word: _ _ _ _ _ _ _
You have 6 guesses left.
Available letters: abcdefghijklmnopqrsuvwxyz

Please guess a letter: k
Oops! That letter is not in my word: _ _ _ _ _ _ _
You have 4 guesses left.
Available letters: abcdefghijlmnopqrsuvwxyz

Please guess a letter: s
Oops! That letter is not in my word: _ _ _ _ _ _ _
You have 2 guesses left.
Available letters: abcdefghijlmnopqruvwxyz

Please guess a letter: c
Oops! That letter is not in my word: _ _ _ _ _ _ _
Sorry, you ran out of guesses.  The word was belgium
m

%run /Users/karenyang/Desktop/6.00.1x/ps3_hangman.py
Loading word list from file...
   55909 words loaded.
Welcome to the game, Hangman!
I am thinking of a word that is 7 letters long.
You have 8 guesses left.
Available letters: abcdefghijklmnopqrstuvwxyz

Please guess a letter: q
Oops! That letter is not in my word: _ _ _ _ _ _ _
You have 6 guesses left.
Available letters: abcdefghijklmnoprstuvwxyz

Please guess a letter: o
Good guess: _ _ o _ _ _ _
You have 5 guesses left.
Available letters: abcdefghijklmnprstuvwxyz

Please guess a letter: f
Oops! That letter is not in my word: _ _ o _ _ _ _
You have 3 guesses left.
Available letters: abcdeghijklmnprstuvwxyz

Please guess a letter: n
Good guess: _ _ o n _ _ _
You have 2 guesses left.
Available letters: abcdeghijklmprstuvwxyz

Please guess a letter: m
Oops! That letter is not in my word: _ _ o n _ _ _
Sorry, you ran out of guesses.  The word was pioneer

"""
