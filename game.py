import random

class Game:
    def __init__(self):
        self.guesses = []
        self.won = False
        self.answer = random.randint(1,100)