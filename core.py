import random

class HotNCold:
    """ 
    A class representing the core game logic for the Hot & Cold game. 
    It manages the game state, including the current level, the random number to guess, and the number of attempts. 
    It provides methods to set the game level, reset the round, check the validity of a guess, and check if a guess is hot, cold, or correct. 
    """

    def __init__(self):
        # Initialize the game state
        self.level_ranges = {
            "Easy": 10,
            "Medium": 100,
            "Epic": 1000,
        }
        self.current_level = "Easy"
        self.max_number = self.level_ranges[self.current_level]
        self.random_number = None
        self.attempts = 0

        self.reset_round()

    def set_level(self, level_name):
        if level_name not in self.level_ranges:
            return
        self.current_level = level_name
        self.max_number = self.level_ranges[level_name]
        self.reset_round()

    def reset_round(self):
        self.random_number = random.randint(1, self.max_number)

    def _check_guess_validity(self, guess):
        if not guess.isdigit() or not (1 <= int(guess) <= self.max_number):
            return False
        return True

    def _check_guess(self, guess):
        if guess < self.random_number:
            return "hot"
        elif guess > self.random_number:
            return "cold"
        else:
            return "correct"
