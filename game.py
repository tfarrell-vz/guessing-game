import random


class Player:
    def __init__(self, name=None):
        if name:
            self.name = name
        else:
            self.name = "anon"


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
        self.scores.append((player, score, upper_bound))

    def personal_best(self, player):
        player_scores = [score for score in self.scores if score[0] == player.name]
        player_scores.sort(key=lambda tup: tup[1]/tup[2])

        return player_scores[0]


def run_game(upper_bound=5):
    game = Game(upper_bound=upper_bound)
    while not game.won:
        guess = input(">> Enter a guess: ")
        game.make_guess(int(guess))

    print("\n*** You won! It only took you %s attempts *** \n" % len(game.guesses))
    return len(game.guesses)


def menu():
    print("--- Menu ---")
    print("Q: Quit")
    print("S: Display your high score")
    print("P: Play")
    print("N: Set player name")
    print("M: Menu")


def main():
    scoreboard = ScoreBoard()
    players = []

    current_player = Player(name=input(">> Set your player name: "))
    players.append(current_player)
    menu()

    while True:
        selection = input(">> Choose a menu option: ")

        if selection in "Qq":
            break

        elif selection in "Ss":
            try:
                name, score, bound = scoreboard.personal_best(current_player)
                print("{}: Your high score was {} guesses out of a max of {}".format(name, score, bound))

            except IndexError:
                print("Hey! You haven't even played the game yet!")

        elif selection in "Pp":
            print("Playing as: ", current_player.name)
            upper_bound = int(input(">> Choose the upper bound integer for the game: "))
            score = run_game(upper_bound)
            scoreboard.add_score(current_player.name, score, upper_bound)

        elif selection in "Mm":
            menu()

        elif selection in "Nn":
            player_name = input(">> Enter a player name: ")
            for player in players:
                if player.name == player_name:
                    current_player = player
                else:
                    current_player = Player(name=player_name)
                    players.append(current_player)

    scoreboard.scores.sort(key=lambda tup: tup[1]/tup[2])
    if scoreboard.scores:
        for player, score, upper_bound in scoreboard.scores:
            print("{}: {} out of {}".format(player, score, upper_bound))


if __name__ == '__main__':
    main()
