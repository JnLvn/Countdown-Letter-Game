# Script to solve the Countdown Letters Game.

# Opens dictionary file.
# Wordlist from https://github.com/dwyl/english-words/blob/master/words2.txt...converted to lowercase by me.
with open('dictionary.txt', 'r') as fileopen:
    words = [line.strip() for line in fileopen]

# Enter letters for anagram.
testInput = input('Enter 9 letters: ')

import time
start_time = time.time()

from itertools import permutations
perms = [''.join(p) for p in permutations(testInput, 2)]
perms1 = [''.join(p) for p in permutations(testInput, 3)]
perms2 = [''.join(p) for p in permutations(testInput, 4)]
perms3 = [''.join(p) for p in permutations(testInput, 5)]
perms4 = [''.join(p) for p in permutations(testInput, 6)]
perms5 = [''.join(p) for p in permutations(testInput, 7)]
perms6 = [''.join(p) for p in permutations(testInput, 8)]
perms7 = [''.join(p) for p in permutations(testInput, 9)]

result = [set(words).intersection(perms)]
result1= [set(words).intersection(perms1)]
result2= [set(words).intersection(perms2)]
result3= [set(words).intersection(perms3)]
result4= [set(words).intersection(perms4)]
result5= [set(words).intersection(perms5)]
result6= [set(words).intersection(perms6)]
result7= [set(words).intersection(perms7)]

mergedlist = result7 + result6 + result5 + result4 +result3 + result2 + result1 + result

r = max(mergedlist, key=str)

print (r)
#print (result7, result6, result5, result4, result3, result2, result1, result)

# Prints running time of the script.
print("--- %s seconds ---" % (time.time() - start_time))