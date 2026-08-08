# Lab 3 - Python Utility Functions
# This file contains reusable functions for word counting,
# list flattening, and calculating the mean of numbers from a file.
import string
import logging
from typing import List, Dict
from collections import Counter

def word_list(text: str) -> list:
    text= text.lower()
    for ch in string.punctuation:
        text = text.replace(ch, "")
    words= text.split()
    return words

# This function takes a string as input and returns a dictionary of word to count and convert the string to lowercase and remove punctuation
def word_count(text: str) -> Dict[str, int]:
    words= word_list(text)
    counts = {}

    for word in words:
        counts[word] = counts.get(word, 0) + 1

    return counts
#print(word_count("Hello, Hello World!"))

# This fuction also do the same thing as word_count but uses the Counter class from the collections module to count the words in the string
def word_count_counter(text: str) -> Counter:
    words= word_list(text)
    counts = Counter(words)

    return counts
#print(word_count_counter("Hello, Hello World!"))

# This function takes a list of lists as input and returns a flattened list using a loop
def flatten_loop(list_of_lists: List[List[int]]) -> List[int]:
    result = []

    for sublist in list_of_lists:
        for item in sublist:
            result.append(item)

    return result
#print(flatten_loop([[1,2],[3,4],[5]]))

# This function takes a list of lists as input and returns a flattened list using a list comprehension
def flatten_comp(list_of_lists: List[List[int]]) -> List[int]:
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
                except ValueError as error:
                    logging.warning(
                        "Invalid number in line '%s': %s",
                        line.strip(),
                        error
                    )
        if numbers:
            return sum(numbers) / len(numbers)
        return None

    except FileNotFoundError:
        print(f"File not found: {path}")
        return None

