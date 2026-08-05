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

# This function takes a list of lists as input and returns a flattened list using a loop
def flatten_loop(list_of_lists):
    result = []

    for sublist in list_of_lists:
        for item in sublist:
            result.append(item)

    return result
#print(flatten_loop([[1,2],[3,4],[5]]))

# This function takes a list of lists as input and returns a flattened list using a list comprehension
def flatten_comp(list_of_lists):
    return [item for sublist in list_of_lists for item in sublist]
#print(flatten_comp([[1,2],[3,4],[5]]))

# This function reads a file containing numbers and returns the mean of those numbers. It handles exceptions for file not found and invalid number formats.
def mean_of_file(path):
    numbers = []

    try:
        with open(path, "r") as file:
            for line in file:
                try:
                    numbers.append(float(line.strip()))
                except ValueError:
                    pass

        if numbers:
            return sum(numbers) / len(numbers)
        return None

    except FileNotFoundError:
        print("File not found.")
        return None

# List Comprehension are enclosed in square brackets[] and eagerly evaluates and stores all elements in memory immediately.
# It uses high memory and returns a standard list object. It also supports indexing and slicing.

#Generator Expressions are enclosed in parantheses() and a generator expression lazily evaluates elements one by one on demand.
# It uses low memory and returns a generator object. It does not support indexing and slicing.

# Generator Expressions are better for working with large datasets, assing data to functions like sum(), max(), min(), any(), and all() and When you only need each value once


if __name__ == "__main__":

    text = "Hello World! Hello Python."

    print(word_count(text))
    print(word_count_counter(text))

    nested = [[1,2],[3,4],[5]]

    print(flatten_loop(nested))
    print(flatten_comp(nested))

    print(mean_of_file("numbers.txt"))

    # Missing file example
    print(mean_of_file("missing.txt"))
