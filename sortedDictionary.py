# http://stackoverflow.com/questions/2587402/sorting-python-list-based-on-the-length-of-the-string

with open('dictionary.txt', 'r') as fileopen:
    words = [line.strip() for line in fileopen]

# Sort dictionary by lenght
sortedList = sorted(words, key=len)

# Reverses list, longest lenght to the top
resverseDic = reversed(sortedList)
f = open("sortedDic.txt","w")

# Write word to text file with 9 letters or lower
for item in resverseDic:
    if len(item) < 10:
        f.write("%s\n" % item)