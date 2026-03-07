import random

class HotNCold:
    def __init__(self, selected_level="Easy", selected_max_value=10):
        # Initialize the game state
        self.level = selected_level
        self.max_number = selected_max_value
        self.random_number = None
        self.attempts = 0

        self.reset_round()

    def _update_level(self, level_name, max_value):
        self.level = level_name
        self.max_number = max_value
        self.reset_round()

    def set_level(self, level_name):
        if level_name not in self.level_ranges:
            return
        self.level = level_name
        self.max_number = self.level_ranges[level_name]
        self.reset_round()

    def reset_round(self):
        self.attempts = 0
        self.random_number = random.randint(1, self.max_number)

    def _check_guess_validity(self, guess):
        if not guess.isdigit() or not (1 <= int(guess) <= self.max_number):
            return False
        return True

    def _check_guess(self, guess):
        if guess == self.random_number:
            return {"direction": "correct", "case": 10}
        
        distance = abs(guess - self.random_number)
        distance_percentage = (distance / self.max_number) * 100
        
        # Map distance percentage to case 1-10 (1=furthest, 10=closest)
        if distance_percentage > 90:
            case = 1
        elif distance_percentage > 80:
            case = 2
        elif distance_percentage > 70:
            case = 3
        elif distance_percentage > 60:
            case = 4
        elif distance_percentage > 50:
            case = 5
        elif distance_percentage > 40:
            case = 6
        elif distance_percentage > 30:
            case = 7
        elif distance_percentage > 20:
            case = 8
        elif distance_percentage > 10:
            case = 9
        else:
            case = 10
        
        direction = "hot" if guess > self.random_number else "cold"
        return {"direction": direction, "case": case}
