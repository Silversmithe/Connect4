

class Settings(object):
    """
        Object that manages the settings of the game
    """
    def __init__(self):
        pass

    @staticmethod
    def print_settings():
        """
        Print out the current settings
        :return:
        """
        print("\n** Settings **\n\n"
              "AI Difficulty: {}\n"
              "AI Sass: {}\n"
              "\tAI Politeness: {}\n".format("1 - 10", "**rolls eyes aggressively", "Gentleman --> (Why you gotta be so rude)"))

    @staticmethod
    def settings_menu():
        """
        Console settings menu
        :return:
        """
        pass
