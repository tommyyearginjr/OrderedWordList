#!/usr/bin/python3.5

# This script is an example of how to split a text by word, add all the words to a list, and alphabetize the words in another list.

myText = "While others may take what I say for granted, I'll just walk on by with a smile on my face."

print(myText)

words = []

words.append((myText.lower()).split(" "))

print(words)

words2 = []

for word in words[0]:
    words2.append(word)

print(words2)

words2.sort()

print(words2)

# By: Tommy H. Yeargin, Jr., on March 28, 2017. Go west, young man!
