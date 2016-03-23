# Script to solve the Countdown Letters Game.
import time
start_time = time.time()

# Opens dictionary file.
# Wordlist from https://github.com/dwyl/english-words/blob/master/words2.txt...converted to lowercase by me.
with open('sortedDic.txt', 'r') as fileopen:
    words = [line.strip() for line in fileopen]

    
# Setting up lists here use of generating your anagram
import random
anagram = []
vowels = ['a','e','i','o','u']
consonant = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','x','z','w','y']

# Loops here will append the required vowels and consonants to the anagram
# It then fills the remaining space with either consonants or vowels
for i in range (0,3):
    anagram.append(random.choice(vowels))
for i in range (0,4):
    anagram.append(random.choice(consonant))
for i in range (0,2):
    anagram.append(random.choice(vowels + consonant))
    
# Imports the shuffle function and jumbles the anagram so that it doesn't really look like it follows a format
from random import shuffle
shuffle(anagram)
print (''.join(anagram))  

# Enter letters for anagram( Manual input I was using to test).
#testInput = input('Enter 9 letters: ')

#for i in testinput
# perms += [''.join(p) for p in permutations(testInput, i)]


# itertools provides a nice function to create permutations in different lenghts.
# http://stackoverflow.com/questions/104420/how-to-generate-all-permutations-of-a-list-in-python
# Creates lists with every permutation of the given lenght.
from itertools import permutations
perms = [''.join(p) for p in permutations(anagram, 2)]
perms1 = [''.join(p) for p in permutations(anagram, 3)]
perms2 = [''.join(p) for p in permutations(anagram, 4)]
perms3 = [''.join(p) for p in permutations(anagram, 5)]
perms4 = [''.join(p) for p in permutations(anagram, 6)]
perms5 = [''.join(p) for p in permutations(anagram, 7)]
perms6 = [''.join(p) for p in permutations(anagram, 8)]
perms7 = [''.join(p) for p in permutations(anagram, 9)]

# If permutation matches word from dictionary, add to list.
# http://stackoverflow.com/questions/1388818/how-can-i-compare-two-lists-in-python-and-return-matches
result = [set(words).intersection(perms)]
result1= [set(words).intersection(perms1)]
result2= [set(words).intersection(perms2)]
result3= [set(words).intersection(perms3)]
result4= [set(words).intersection(perms4)]
result5= [set(words).intersection(perms5)]
result6= [set(words).intersection(perms6)]
result7= [set(words).intersection(perms7)]

# Add lists together.
mergedlist = result7 + result6 + result5 + result4 +result3 + result2 + result1 + result

# Return longest string from list.
# http://stackoverflow.com/questions/873327/pythons-most-efficient-way-to-choose-longest-string-in-list
r = max(mergedlist)
#r= max(mergelist, key=str)

print (r)
#print (result7, result6, result5, result4, result3, result2, result1, result)

# Prints running time of the script.
print("--- %s seconds ---" % (time.time() - start_time))