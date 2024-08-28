#wordle_utils.py

from collections import Counter

def load_words(word_list_file):
    with open(word_list_file, 'r') as file:
        return file.read().splitlines()

def calculate_letter_frequencies(word_list):
    letter_counts = Counter()
    for word in word_list:
        letter_counts.update(word)
    return letter_counts
