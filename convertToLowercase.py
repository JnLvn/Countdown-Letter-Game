# Script to convert wordlist.txt into a text file with only lowercase letters
# contribution http://stackoverflow.com/questions/17329113/convert-list-to-lower-case

with open('wordlist.txt', 'r')as myfile:
   words = [line.strip() for line in myfile]

words = [item.lower() for item in words]

f = open("dictionary.txt", "w")
for item in words:
    f.write("%s\n" % item)