### John Lavin
#### G00192754

# Countdown Letters Game Solver
A Python script to solve the Countdown Letters Game. 

The Countdown Letters Game consists of 9 randomly selected letters (at least 3 vowels and 4 consonants). The letters must be arranged to form the longest word possible. The length of the word determines the number of points earned, e.g. chair = 5 points. If a 9 letter word is constructed the contestant receives double points (18 points) for the round.  


## Background
[solver.py][4] file.

The first task I completed was to test my word list. A simple search for a word in my dictionary file. 
I used a script I got online at [wordlistTester][1]. 
My next step was to research Python’s built in iterator module [itertools][2]. This is where I learned of the permutations function:
```python
from itertools import permutations
```
Next step was to compare my list of permutations to actual words from my dictionary file. This was achieved using Python’s [intersection][3] method: 
```python
result = [set(words).intersection(perms)]
```
On completion I was getting an average time of 0.9 seconds. I realised there were definitely faster ways of comparing anagrams and dictionary words. I began researching different ways to develop a function to check if a word was present in an anagram. This lead to my discovery of [STEALTHCOPTER Blog][5]. I developed [solver3.py][6] from this blog. Solver3.py is the python script which solves the Countdown Letters Game in the quickest time. 




## Words list
I found a pretty decent words list at this [GitHub][7] Repository. Only problem was it contained both upper and lower-case letters. I created a small script [convertToLowercase.py][8] to rectify this problem. Next I went about sorting the dictionary starting with the longest length at the top. Words with more than 9 letters were removed as the Countdown game only allows 9 letters. I used the [sortedDictionary.py][9] script to achieve this. This sorted dictionary improved the algorithms speed greatly. 

Evolution of word list : [wordlist.txt][10] -> [dictionary.txt][11] -> [sortedDic.txt][12]


## Python script
My main script is [solver3.py][6]. My first attempt which turned out to be too slow can be found at [solver.py][4]. 

The most important section is:

```python
def anagramCheck(word,checkword):  
    for letter in word:  
        if letter in checkword:  
            checkword=checkword.replace(letter, '', 1)  
        else:  
            return 0  
    return 1  
```
This function checks if a given word is an anagram of another word. Takes two string inputs (dictionary word, anagram). Loops through every letter in word, checks against checkword. If letter is present in checkword, removes from checkword so it can't be used again.


## Preprocessing
The only preprocessing involved is the parsing of the dictionary file and the removal of any extra space at the end of each line with line.strip().
Once the preprocessing is done we can run the game solver again and again without that overhead.



## Results
All results are taken on an average of running the script 20 times.

The script runs at 0.4112 seconds when it is first executed. This slow time is down to the preprocessing. After the initial preprocessing the script runs at 0.2496 seconds on average. With some of the fastest times at 0.2091 seconds. This is due to a smaller list of anagrams returned with only 48 words. Slower times of 0.4313 were found when larger lists of 400 plus words were returned.

To increase the speed of the script I decided to limit the number of words returned to just the top result (longest word). This greatly improved the speed with an average of 0.1841 seconds achieved. The fact that it no longer had to search the entire dictionary for every match cut the time in half. 

One of the fastest times I found was 0.10009. This was with the word “friended”. This fast time can be attributed to the way I have the dictionary sorted (longest words to the top).



## References
[1]: https://github.com/YesManKablam/CountdownConundrumSolver/blob/master/solver.py
[2]: https://docs.python.org/2/library/itertools.html 
[3]: http://stackoverflow.com/questions/1388818/how-can-i-compare-two-lists-in-python-and-return-matches
[4]: https://github.com/JnLvn/Countdown-Letter-Game/blob/master/solver.py
[5]: http://www.stealthcopter.com/blog/2009/11/python-anagram-solver/
[6]: https://github.com/JnLvn/Countdown-Letter-Game/blob/master/solver3.py
[7]: https://github.com/dwyl/english-words/blob/master/words2.txt
[8]: https://github.com/JnLvn/Countdown-Letter-Game/blob/master/convertToLowercase.py
[9]: https://github.com/JnLvn/Countdown-Letter-Game/blob/master/sortedDictionary.py
[10]: https://github.com/JnLvn/Countdown-Letter-Game/blob/master/wordlist.txt
[11]: https://github.com/JnLvn/Countdown-Letter-Game/blob/master/dictionary.txt
[12]: https://github.com/JnLvn/Countdown-Letter-Game/blob/master/sortedDic.txt


