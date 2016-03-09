# Test the wordlist
# Script from https://github.com/YesManKablam/CountdownConundrumSolver/blob/master/solver.py

# Opens dictionary file.
# Wordlist from https://github.com/dwyl/english-words/blob/master/words2.txt
with open('dictionary.txt', 'r') as fileopen:
    words = [line.strip() for line in fileopen]


# Takes input from console to use as the anagram.
testInput = input('Enter word: ')

# Running time for the algorithm.
# It starts here, otherwise it takes into account waiting for user input.
import time
start_time = time.time()

# The permutations script will generate every possible combo of a word.
# This does not currently match the countdown rule however.
# If you enter a 9 letter word, it will only return the 9 letter anagrams.
# But it's mad fast and this whole thing is 9 lines including the timing function
from itertools import permutations
perms = [''.join(p) for p in permutations(testInput)]

# Returns where the permutations match the dictionary files.
# Using sets here to remove any duplicates.
print(set(words) & set(perms))

# Prints running time of the script.
print("--- %s seconds ---" % (time.time() - start_time))