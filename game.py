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


def main():
    game = Game()
    while not game.won:
        guess = input(">> Enter a guess: ")
        game.make_guess(guess)

    print("You won! It only took you %s attempts" % len(game.guesses))

if __name__ == '__main__':
    main()