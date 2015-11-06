import random


class Game:
    def __init__(self, upper_bound=100):
        self.guesses = []
        self.won = False
        self.answer = random.randint(1, upper_bound)

    def make_guess(self, num):
        self.guesses.append(num)
        if num == self.answer:
            self.won = True


def main():
    game = Game(upper_bound=5)
    while not game.won:
        guess = input(">> Enter a guess: ")
        game.make_guess(int(guess))

    print("You won! It only took you %s attempts" % len(game.guesses))


if __name__ == '__main__':
    main()
