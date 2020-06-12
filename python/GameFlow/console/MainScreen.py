from GameFlow.console.Console import Console
from GameFlow.console.Settings import Settings
from GameFlow.console.CharacterSelect import CharacterSelect
from GameMechanics.InstanceController import InstanceController
from GameMechanics.Spectator import Spectator


class MainScreen(object):
    """
        Object that represents the main screen of the game.
        In charge of selecting the game type
    """
    def __init__(self):
        self.console = Console()
        self.character_select = CharacterSelect()
        self.settings = Settings()

        self.game_branch = {
            1: self.one_player_layer,
            2: self.two_player_layer,
            3: self.unavailable,
            4: self.layer_settings,
            5: self.die
        }

    def one_player_layer(self):
        """

        :return:
        """
        self.unavailable()
        # self.console.clear_console()
        # print("-" * 50)
        # self.character_select.start_for_one()
        # print("-" * 50)
        # self.console.press_enter_to_continue()
        # self.console.clear_console()
        #
        # # start game
        # player1 = self.character_select.players[0]
        # player2 = self.character_select.players[1]
        #
        # game_on = True
        #
        # while game_on:
        #
        #     game_inst = InstanceController(player1, player2)
        #
        #     game_inst.run()
        #
        #     self.console.press_enter_to_continue()
        #
        #     # to reset or not reset?
        #     self.console.clear_console()
        #     if self.console.yes_or_no("Would you like a rematch?") is True:
        #         # they want to rematch
        #         game_inst.reset()
        #         self.console.clear_console()
        #         game_on = True
        #     else:
        #         # get rid of previous character data
        #         self.character_select.reset()
        #         self.console.clear_console()
        #         game_on = False

        self.start()

    def two_player_layer(self):
        """

        :return:
        """
        self.console.clear_console()
        print("-" * 50)
        self.character_select.start_for_two()
        print("-" * 50)
        self.console.press_enter_to_continue()
        self.console.clear_console()

        # start game
        player1 = self.character_select.players[0]
        player2 = self.character_select.players[1]
        game_inst = InstanceController(player1, player2)

        game_on = True

        while game_on:

            game_inst.run()

            self.console.press_enter_to_continue()

            # to reset or not reset?
            self.console.clear_console()
            if self.console.yes_or_no("Would you like a rematch?") is True:
                # they want to rematch
                game_inst.reset()
                self.console.clear_console()
                game_on = True
            else:
                # get rid of previous character data
                self.character_select.reset()
                self.console.clear_console()
                game_on = False

        self.start()

    def layer_settings(self):
        """

        :return:
        """
        self.console.clear_console()
        print("-" * 50)
        self.settings.print_settings()
        print("-" * 50)
        self.console.press_enter_to_continue()
        self.console.clear_console()
        self.start()

    @staticmethod
    def is_valid_input(value):
        """
        Check for valid input
        :return:
        """
        if value is None:
            return None

        try:
            value = int(value)
        except ValueError:
            return None

        if 1 <= value <= 5:
            return value
        else:
            return None

    def start(self):
        """
        Displays the main screen
        :return:
        """
        print("*"*20)
        print("*" + " "*18 + "*")
        print("*" + " "*4 + "Connect 4X" + " "*4 + "*")
        print("*" + " " * 18 + "*")
        print("*" * 20)
        print("\nConsole Version 1.0.0\n")
        self.print_menu()
        self.get_input()

    def get_input(self):
        """
        Loop for getting input
        :return:
        """
        result = None

        try:
            while True:
                result = self.console.read_for_condition(prompt=">>> ", condition=self.is_valid_input)

                if result is not None:
                    break
        except KeyboardInterrupt:
            quit()

        # run command for next condition
        self.game_branch[result]()

    def unavailable(self):
        """
        Say that this service is unavailable
        :return:
        """
        print("\n**Sorry this Service is unavailable**\n")
        self.get_input()

    @staticmethod
    def die():
        """
        When the game closes
        :return:
        """
        print("*"*13)
        print("* Goodbye!! *")
        print("*" * 13)
        quit()

    @staticmethod
    def print_menu():
        """
        Print the menu
        :return:
        """
        print("1 - (One Player)\n"
              "2 - Two Player\n"
              "3 - (Online)\n"
              "4 - (Settings)\n"
              "5 - Quit\n")
