# 6.00x Problem Set 6
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#

lower = string.ascii_lowercase
upper = string.ascii_uppercase
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    dict1_lower = {}
    dict1_upper = {}


    for i in upper:
        value_index = upper.index(i) + shift
        if value_index > 25:
            new_val = value_index%26
        else:
            new_val = value_index
        dict1_upper[i]=upper[new_val]
        

    dict2_lower = {i.lower():j.lower() for (i,j) in zip(dict1_upper.keys(), dict1_upper.values())}
    
    dict1_upper.update(dict2_lower)
    

    return dict1_upper

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    collector = ""
    for i in text:
        if i in lower or i in upper:
            x = coder[i]
            collector = collector + x
        else:
            collector = collector + i
    return collector

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    x = applyCoder(text,buildCoder(shift))
    return x

#
# Problem 2: Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """ 
    maxnum_realwords = 0       #1. Set the maximum number of real words found to 0.
    best_shift = 0             #2. Set the best shift to 0.
    for shift in range(0, 26): #3. For each possible shift from 0 to 26:
        x = applyShift(text, shift)  #4. Shift the entire text by this shift.
        list1 = x.split(' ')
        valid = 0                    #5. Split the text up into a list of the individual words.
        for word in list1:           #6. Count the number of valid words in this list.
            if isWord(wordList, word)==True:
                valid += 1
            else:
                pass
        if valid > maxnum_realwords:   #7. If this number of valid words is more than the largest
            maxnum_realwords = valid   #8. Record the number of valid words.
            best_shift = shift         #9. Set the best shift to the current shift.
        else:
            pass
            
        shift = shift + 1#10. Increment the current possible shift by 1. Repeat the loop starting at line 3.
    return best_shift

def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    wordList = loadWords()
    text = getStoryString()
    print (text)
    shift = findBestShift(wordList, text)
    
    return applyShift(text, shift)

#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    # To test findBestShift:


    wordList = loadWords()
    s = applyShift('Hello, world!', 8)
    bestShift = findBestShift(wordList, s)
    assert applyShift(s, bestShift) == 'Hello, world!'
    # To test decryptStory, comment the above four lines and uncomment this line:
    #    decryptStory()
    
    """
    test
    
    >>> decryptStory()
Loading word list from file...
   55909 words loaded.
Tkmu Pvyboi sc k widrsmkv mrkbkmdob mbokdon yx dro czeb yp k wywoxd dy rovz myfob kx sxceppsmsoxdvi zvkxxon rkmu. 
Ro rkc loox boqscdobon pyb mvkccoc kd WSD dgsmo lopybo, led rkc bozybdonvi xofob zkccon k mvkcc. 
Sd rkc loox dro dbknsdsyx yp dro bocsnoxdc yp Okcd Mkwzec dy lomywo Tkmu Pvyboi pyb k pog xsqrdc okmr iokb 
dy onemkdo sxmywsxq cdenoxdc sx dro gkic, wokxc, kxn odrsmc yp rkmusxq.

'Jack Florey is a mythical character created on the spur of a moment to help cover an insufficiently planned hack. 
He has been registered for classes at MIT twice before, but has reportedly never passed a class. 
It has been the tradition of the residents of East Campus to become Jack Florey for a few nights each year
to educate incoming students in the ways, means, and ethics of hacking.\n'
"""

