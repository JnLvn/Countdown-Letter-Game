### John Lavin
#### G00192754

# Countdown Letters Game Solver
A Python script to solve the Countdown Letters Game. 

The Countdown Letters Game consists of 9 randomly selected letters (at least 3 vowels and 4 consonants). The letters must be arranged to form the longest word possible. The length of the word determines the number of points earned, e.g. chair = 5 points. If a 9 letter word is constructed the contestant receives double points (18 points) for the round.  


## Background
The first task I completed was to test my word list. A simple search for a word in my dictionary file. 
I used a script I got online at [wordlistTester][1]

My next step was to research Python’s built in iterator module [itertools][2]. This is where I learned of the permutations function: 
```python
from itertools import permutations
```

Next step was to compare my list of permutations to actual words from my dictionary file. This was achieved using Python’s [intersection][3] method: 
```python
result = [set(words).intersection(perms)]
```



## Words list
My words list is in the file [wordslist.txt](wordslist.txt) in this repoistory/gist.
I got my words list from the [Oxford Learner's Dictionaries][1] website.

## Python script
My script is in the files [solver.py](solver.py) in this repository and it works as follows.
The most important section is:

```python
import random
print(random.shuffle("My code is cool."))
```

Previously it looks like this:
```python
# Note that the following snippet of code was adapted from
# the Stack Overflow post available here: http://www.so.com/post/123
import nothing
```
That didn't work too well, so I changed it.

## Preprocessing
My script does a lot of preprocessing, which only needs to be run once.
Once the preprocessing is done we can run the game solver again and again without that overhead.

## Efficiency
Here's some stuff about how efficient my code is, including an analysis of how many calculations my algorithm requires.

## Results
My script runs very quickly, and certainly within the 30 seconds allowed in the Coutdown letters game.


## References
[1]: https://github.com/YesManKablam/CountdownConundrumSolver/blob/master/solver.py
[2]: https://docs.python.org/2/library/itertools.html 
[3]: http://stackoverflow.com/questions/1388818/how-can-i-compare-two-lists-in-python-and-return-matches
