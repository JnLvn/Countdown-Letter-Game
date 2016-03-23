# http://www.stealthcopter.com/blog/2009/11/python-anagram-solver/
# Script to solve the Countdown Letters Game.

import time
start_time = time.time()
 
# Lists for generating random anagrams.
import random
anagram = []
vowels = ['a','e','i','o','u']
consonant = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','x','z','w','y']

# Set the anagram with the necessary consonants & vowels.
for i in range (0,3):
    anagram.append(random.choice(vowels))
for i in range (0,4):
    anagram.append(random.choice(consonant))
for i in range (0,2):
    anagram.append(random.choice(vowels + consonant))
    
# Import the shuffle function to shuffle up the anagram and give it a less organised look. 
from random import shuffle
shuffle(anagram)
print ("Anagram :", ''.join(anagram))
print ("***************************")
a = (''.join(anagram))
 

# function to check if a given word is an anagram of another word.
# Two string inputs (dictionary word, anagram) 
# Loops through every letter in word, checks against checkword. 
# If letter is present in checkword, removes from checkword so it can't be used again.
def anagramCheck(word,checkword):  
    for letter in word:  
        if letter in checkword:  
            checkword=checkword.replace(letter, '', 1)  
        else:  
            return 0  
    return 1  


i = 1 # For presentation purpose only.

# Loop through every line in the dictionary file.
# Strip line to remove any extra space at end of lines.
# Ignore lines of lenght smaller than 3. There will always be at least a 3 letter word.
f=open('sortedDic.txt', 'r')  
for line in f:  
    line=line.strip()  
    if len(line)>=3:  
        if anagramCheck(line,a):
            print (i , ":", line)
            i += 1
             
f.close() 


# Prints running time of the script.
print("--- %s seconds ---" % (time.time() - start_time))