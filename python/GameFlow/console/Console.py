import sys
import os


class Console(object):
    """
        Class responsible for handling input from the user
    """
    def __init__(self):
        self.log_file = "log.txt"
        # initialize log
        with open(self.log_file, 'a') as file:
            file.write("** NEW LOG CREATED **\n")

    @staticmethod
    def read_for_condition(prompt, condition):
        """
        Continues to prompt user for input until the condition
        is fulfilled
        :param prompt: prompt for the input
        :param condition: the function that checks condition of input
        :return: value
        """
        user_input = None

        while user_input is None:
            user_input = condition(input(prompt))

        return user_input

    @staticmethod
    def yes_or_no(prompt):
        """
            Primpt the user to say yes or no
            @:param: prompt
            :return: true of yes, false if no
        """
        user_input = None

        while user_input is None:
            user_input = input("{}: yes/no >>> ".format(prompt))
            if user_input.lower() == 'yes' or user_input.lower() == 'y':
                return True
            elif user_input.lower() == 'no' or user_input.lower() == 'n':
                return False
            else:
                user_input = None

    @staticmethod
    def press_enter_to_continue():
        """
        Wait until someone presses enter
        :return:
        """
        user_input = input("Press Enter To Continue...")

    def log(self, msg):
        """
        Log information
        :param msg:
        :return:
        """
        with open(self.log_file, 'a') as file:
            file.write(msg)

    @staticmethod
    def clear_console():
        """
            clear console
        :return:
        """
        # not covering cygwin
        if sys.platform == "darwin":
            os.system("clear")
        elif sys.platform == "linux":
            os.system("clear")
        else:
            os.system("cls")

