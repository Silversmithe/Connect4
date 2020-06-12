import random
import time
from GameFlow.console.Console import Console
from GameMechanics.Spectator import Spectator


class CharacterSelect(object):
    """
        State for selecting character
    """
    def __init__(self):
        self.console = Console()
        self.skins = {
            1: "Black",
            2: "Red",
            3: "Blue",
            4: "Green",
            5: "Purple",
            6: "Smiley Face",
            7: "Devil Face",
            8: "Number Four",
            9: "All Star"
        }
        self.selected = list()
        self.players = list()

    def reset(self):
        """
        Reset the players and the selected items
        :return:
        """
        self.selected.clear()
        self.players.clear()

    def show_skins(self):
        """

        :return:
        """
        print("COIN OPTIONS:\n")
        for skin in self.skins:
            print("{} - {}".format(skin, self.skins[skin]))

        print()

    def start_for_one(self):
        """
        Character selection for one character
        :return:
        """
        self.start(num_chars=1)

    def start_for_two(self):
        """
        Character selection for two characters
        :return:
        """
        self.start(num_chars=2)

    def start_for_onlince(self):
        """
        Character selection for online play
        :return:
        """
        self.start(num_chars=1, online=True)

    def is_valid_input(self, prompt):
        """
        check to validate user input
        :param prompt: user input
        :return:
        """
        try:
            value = int(prompt)
        except ValueError:
            return None

        if value in self.skins:
            # if user input matches any of keys
            if value in self.selected:
                print("Coin is taken! Please choose another")
                return None
            else:
                print("{} skin selected,\n\n".format(self.skins[value]), end='')
                time.sleep(3)
                return value

    def start(self, num_chars, online=False):
        """
        Provides character select
        :return:
        """
        assert 1 <= num_chars <= 2

        selected = []
        number_of_characters = num_chars

        # for AI
        if num_chars == 1:
            # pick an AI character
            name = "Connect Bot"
            identity = random.randrange(1, 10)
            self.selected.append(identity)
            self.players.append(Spectator(name=name, identity=identity, ai=True))

        # human player registration
        for num in range(1, number_of_characters + 1):

            name = str(input("Player {}, what is your name? ".format(num)))
            self.show_skins()
            identity = self.console.read_for_condition("Okay {}, what coin would you like to use? >>> ".format(name),
                                                       self.is_valid_input)
            self.selected.append(identity)

            self.players.append(Spectator(name=name, identity=identity))
            self.console.clear_console()

        print("\nCharacters are ready to go!")
        for player in self.players:
            print(str(player))

        # if online, do connection things
        # if not online, just create the game instance
