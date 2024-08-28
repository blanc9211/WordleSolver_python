# wordle_tester.py

from wordle_game import WordleGame
from wordle_solver import WordleSolver
from wordle_utils import load_words

def test_solver(num_games, word_list_file):
    word_list = load_words(word_list_file)
    success_count = 0

    if num_games == 1:
        game = WordleGame(word_list)
        solver = WordleSolver(word_list)

        while not game.game_over():
            guess = solver.get_best_guess()
            feedback = game.guess_word(guess)
            if feedback:
                if game.is_solved(feedback):
                    print(f"\nGame Solved in {game.attempts} tries!")
                    game.print_wordle() 
                    break
                solver.update_possible_words(guess, feedback)
        if not game.is_solved(feedback):
            print(f"\nGame Over! The word was: {game.target_word}")

    else:
        for _ in range(num_games):
            game = WordleGame(word_list)
            solver = WordleSolver(word_list)

            while not game.game_over():
                guess = solver.get_best_guess()
                feedback = game.guess_word(guess)
                if feedback:
                    if game.is_solved(feedback):
                        success_count += 1
                        break
                    solver.update_possible_words(guess, feedback)

        accuracy = success_count / num_games * 100
        print(f"Total Games: {num_games}")
        print(f"Total Success: {success_count}")
        print(f"Solver accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    num_games = 10  # Change this to the number for 1 game with print wordle and >1 to test accuracy
    file_1 = 'words_12792.txt'
    file_2 = 'words_2315.txt'
    word_list_file='dataset/'+ file_2 
    if num_games!=1: 
        print('-'* 30)
        print("File Name :",word_list_file)
        print('-'* 30)
        for i in range(3):
            test_solver(num_games,word_list_file)
            print('-'* 30)
    test_solver(num_games,word_list_file)