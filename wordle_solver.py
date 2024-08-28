# wordle_solver.py

from wordle_utils import calculate_letter_frequencies

class WordleSolver:
    def __init__(self, word_list):
        self.word_list = word_list
        self.letter_frequencies = calculate_letter_frequencies(self.word_list)
        self.possible_words = self.word_list.copy()

    def get_best_guess(self):
        def word_score(word):
            return sum(self.letter_frequencies[letter] for letter in set(word))
        
        scored_words = sorted(self.possible_words, key=word_score, reverse=True)
        return scored_words[0] if scored_words else None

    def update_possible_words(self, guess, feedback):
        # Eliminate words from possible_words based on feedback
        new_possible_words = []
        for word in self.possible_words:
            valid_word = True
            for i, (letter, fb) in enumerate(zip(guess, feedback)):
                
                # Yellow: correct letter, wrong position
                # Green: correct letter and position
                # Black: letter not in word

                if fb == 'G' and word[i] != letter:  
                    valid_word = False
                elif fb == 'Y' and (word[i] == letter or letter not in word):  
                    valid_word = False
                elif fb == 'B' and letter in word:  # Black: letter not in word
                    valid_word = False
            if valid_word:
                new_possible_words.append(word)
        self.possible_words = new_possible_words