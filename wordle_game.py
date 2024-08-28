import random

class WordleGame:
    def __init__(self, word_list):
        self.word_list = word_list
        self.target_word = random.choice(self.word_list)
        self.max_attempts = 6
        self.attempts = 0
        self.guess_feedback_list = []

    def guess_word(self, guess):
        if len(guess) != 5 or guess not in self.word_list:
            return None  # Invalid guess

        # Initialize feedback list with empty strings
        feedback = [''] * 5
        for i, letter in enumerate(guess):
            if letter == self.target_word[i]:
                feedback[i] = 'G'  # Correct letter, correct position (Green)
            elif letter in self.target_word:
                feedback[i] = 'Y'  # Correct letter, wrong position (Yellow)
            else:
                feedback[i] = 'B'  # Incorrect letter (Black)
        
        self.guess_feedback_list.append((guess, feedback))
        self.attempts += 1
        return feedback

    def is_solved(self, feedback):
        return feedback == ['G'] * 5

    def game_over(self):
        return self.attempts >= self.max_attempts

    def print_wordle(self):
        border_char = '│'
        spacer = ' '
        border_width = 3  # Width of each box including padding
        horizontal_border = ' ' + '─' * (border_width * 8)  # Adjust length for 5 letters and borders

        print(horizontal_border)
        for guess, feedback in self.guess_feedback_list:
            row = border_char
            for letter, fb in zip(guess, feedback):
                # Determine color based on feedback
                color = ' \033[92m' if fb == 'G' else \
                        ' \033[93m' if fb == 'Y' else \
                        ' \033[90m'  # Gray for incorrect letters
                reset = ' \033[0m'
                # Format the letter with color and add it to the row
                row += f'{color}{letter.center(border_width - 1)}{reset}{border_char}'
            print(row)
            print(horizontal_border)
