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


class ScoreBoard:
    def __init__(self):
        self.scores = []

    def add_score(self, player, score, upper_bound):
        self.scores.append((player,score, upper_bound))


def run_game(upper_bound=5):
    game = Game(upper_bound=upper_bound)
    while not game.won:
        guess = input(">> Enter a guess: ")
        game.make_guess(int(guess))

    print("You won! It only took you %s attempts\n" % len(game.guesses))
    return len(game.guesses)


def main():
    scoreboard = ScoreBoard()

    while True:
        selection = input(">> Choose a menu option: ")

        if selection in "Qq":
            break

        elif selection in "Pp":
            upper_bound = int(input(">> Choose the upper bound integer for the game: "))
            score = run_game(upper_bound)
            scoreboard.add_score("anon", score, upper_bound)

    if scoreboard.scores:
        for player, score, upper_bound in scoreboard.scores:
            print("{}: {} out of {}".format(player, score, upper_bound))


if __name__ == '__main__':
    main()
