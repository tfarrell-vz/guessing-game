import random

class Game:
    def __init__(self):
        self.guesses = []
        self.won = False
        self.answer = random.randint(1,100)

    def make_guess(self, num):
        self.guesses.append(num)
        if num == self.answer:
            self.won = True

    def game_won(self):
        return self.won