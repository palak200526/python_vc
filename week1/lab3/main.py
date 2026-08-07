import string
from collections import Counter

# This function takes a string as input and returns a dictionary of word to count and convert the string to lowercase and remove punctuation
def word_count(text):
    text= text.lower()
    for ch in string.punctuation:
        text = text.replace(ch, "")
    words= text.split()
    counts = {}

    for word in words:
        counts[word] = counts.get(word, 0) + 1

    return counts
#print(word_count("Hello, Hello World!"))

# This fuction also do the same thing as word_count but uses the Counter class from the collections module to count the words in the string
def word_count_counter(text):
    text= text.lower()
    for ch in string.punctuation:
        text = text.replace(ch, "")
    words= text.split()
    counts = Counter(words)

    return counts
#print(word_count_counter("Hello, Hello World!"))