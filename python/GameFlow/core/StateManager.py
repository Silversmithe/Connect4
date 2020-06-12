import pygame
from pygame.locals import *
from sys import exit


class StateManager(object):

    def __init__(self, states):
        self.GAME_STATES = states
        self.CURRENT_STATE = None
        self.RUNNING = False

    def state_exists(self, state_id):
        """
        Validate that the state mentioned exists
        :return:
        """
        return state_id in self.GAME_STATES

    def startup(self):
        """
        Initializing the manager
        :return:
        """
        if len(self.GAME_STATES) > 0:
            self.RUNNING = True
            for state in self.GAME_STATES:
                if state is not None:
                    self.CURRENT_STATE = state
                    break

            return True

        return False

    def cleanup(self):
        """
        Exiting gracefully
        :return:
        """
        self.GAME_STATES.clear()
        self.CURRENT_STATE = None
        self.RUNNING = False

    def change_state(self, state_id):
        """
        Switching States
        :return:
        """
        if self.state_exists(state_id=state_id):
            # clean up the current state
            self.CURRENT_STATE.cleanup()
            # change to the new state
            self.CURRENT_STATE = self.GAME_STATES[state_id]
            # setup the new state
            self.CURRENT_STATE.startup()
            return True

        return False

    def update(self):
        """

        :return:
        """
        pass

    def draw(self):
        """

        :return:
        """
        pass

    def is_running(self):
        """
        :return: boolean if manager is running or not
        """
        return self.RUNNING

    # INITIALIZATION AND RUNNING
    @staticmethod
    def init():
        """Initialize all the important aspects of the game
            environment
        """
        # initialize pygame
        pygame.init()
        # setup the screen
        screen = pygame.display.set_mode((640, 480), pygame.DOUBLEBUF, 32)
        pygame.display.set_caption("Connect4X")

    @staticmethod
    def run():
        """
        Main loop of the state manager

        init

        while true:

            check events

            update state
            draw state
        :return:
        """
        while True:
            # take state's listener and run in loop
            # state's listener should return if it needs
            #   - to change state or not, otherwise, perform action

            # check events in the system
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()

            pygame.display.update()



