import random
from GameFlow.console.Console import Console
from GameMechanics.Board import Board
from GameMechanics.Spectator import Spectator
from enum import Enum


class InstanceTranscript(object):
    """Holds information about the game"""
    def __init__(self, winner, loser, length, board, tie=False):
        self.WINNER = winner
        self.LOSER = loser
        self.GAME_LENGTH = length
        self.BOARD = board
        self.TIE = tie

    def __str__(self):
        if self.TIE:
            return "RECEIPT:\n\n" \
                   "TIE\n" \
                   "GAME LENGTH: {}\n\n".format(self.GAME_LENGTH)
        else:
            return "RECEIPT:\n\n" \
                   "WINNER: {}\n" \
                   "LOSER: {}\n" \
                   "GAME LENGTH: {}\n\n".format(self.WINNER.NAME, self.LOSER.NAME, self.GAME_LENGTH)


class InstanceController(object):
    """
    Controls the newly controlled game

    Interface between the engine and the graphics
    """

    class State(Enum):
        ACTIVE_GAME = 0
        INACTIVE_GAME = 1
        # will have controls for reset soon
        RESET = 2

    def __init__(self, player1, player2):
        self.console = Console()
        self.STATE = InstanceController.State.ACTIVE_GAME
        self.RECEIPT = None

        self.PLAYER_ONE = player1
        self.PLAYER_TWO = player2

        self.Turn = None
        self.pick_player_start()

        self.BOARD = Board(self.PLAYER_ONE, self.PLAYER_TWO)

    def reset(self):
        """

        :return:
        """
        self.STATE = InstanceController.State.ACTIVE_GAME
        self.RECEIPT = None
        self.pick_player_start()
        self.BOARD.reset_board()

    def pick_player_start(self):
        select = random.random()
        if select < 0.5:
            self.Turn = self.PLAYER_ONE
        else:
            self.Turn = self.PLAYER_TWO

    def use_turn(self):
        """

        :return:
        """
        result = None

        result = self.Turn.player_move()
        if result is not None:
            self.BOARD.set_piece(self.Turn, result)
            # adding to history
            self.BOARD.HISTORY.append([self.Turn.NAME, result])
            self.RECEIPT = self.inspect_for_win(self.Turn)
        else:
            self.RECEIPT = self.inspect_for_win(self.Turn, quit=True)

        # check result
        if self.RECEIPT is not None:
            self.STATE = InstanceController.State.INACTIVE_GAME
            # stat inactive & display board
            self.BOARD.print_board()

    def inspect_for_win(self, player, quit=False):
        print("JUDGEMENT")

        if quit is True:
            self.PLAYER_ONE.STATE = Spectator.State.TIE
            self.PLAYER_TWO.STATE = Spectator.State.TIE
            return InstanceTranscript(board=self.BOARD,
                                      length=len(self.BOARD.HISTORY),
                                      winner=None,
                                      loser=None,
                                      tie=True)

        horizon = self.BOARD.REFEREE.check_all_horizontal(player.ID)
        vertical = self.BOARD.REFEREE.check_all_vertical(player.ID)
        diagonal = self.BOARD.REFEREE.check_all_diagonal(player.ID)

        win = horizon[0] or vertical[0] or diagonal[0]

        if win:
            if player == self.PLAYER_TWO:
                self.PLAYER_ONE.STATE = Spectator.State.LOSE
                self.PLAYER_TWO.STATE = Spectator.State.WIN
                receipt = InstanceTranscript(board=self.BOARD,
                                             length=len(self.BOARD.HISTORY),
                                             winner=self.PLAYER_TWO,
                                             loser=self.PLAYER_ONE)
            else:
                self.PLAYER_ONE.STATE = Spectator.State.WIN
                self.PLAYER_TWO.STATE = Spectator.State.LOSE
                receipt = InstanceTranscript(board=self.BOARD,
                                             length=len(self.BOARD.HISTORY),
                                             winner=self.PLAYER_ONE,
                                             loser=self.PLAYER_TWO)

            # make board inactive
            # someone wins, create reciept and return
            return receipt

        else:
            # do not change the state
            # do not send reciept
            # change player turn
            if self.Turn == self.PLAYER_ONE:
                self.Turn = self.PLAYER_TWO
            else:
                self.Turn = self.PLAYER_ONE

            return None

    def run(self):
        """

        :return:
        """

        while self.STATE == InstanceController.State.ACTIVE_GAME:

            try:
                self.BOARD.print_board()
                self.use_turn()

            except KeyboardInterrupt:
                pass

        print("GAME FINISHED!\n")
        print(str(self.RECEIPT))
        self.RECEIPT.BOARD.print_history()


