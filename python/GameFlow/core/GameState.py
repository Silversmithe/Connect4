"""
Define the base class for a game state
"""
import abc


class GameState(metaclass=abc.ABCMeta):
    """
    State of the game
    """
    def __init__(self, label, identity):
        self.LABEL = label
        self.ID = identity

    def get_label(self):
        """
        :return: string : the english identifier
        """
        return self.LABEL

    def get_id(self):
        """

        :return:
        """
        return self.ID

    @abc.abstractclassmethod
    def startup(self):
        """
        What happens on entering a specific gamestate
        :return:
        """
        pass

    @abc.abstractclassmethod
    def cleanup(self):
        """
        What happens on leaving a specific gamestate
        :return:
        """
        pass

    @abc.abstractclassmethod
    def pause(self):
        """
        Gamestate is Paused (not the same as pausing game)
        :return:
        """
        pass

    @abc.abstractclassmethod
    def resume(self):
        """
        Gamestate has been resumed
        :return:
        """
        pass

    @abc.abstractclassmethod
    def handle_event(self):
        pass

    @abc.abstractclassmethod
    def update(self):
        pass

    @abc.abstractclassmethod
    def draw(self):
        pass





