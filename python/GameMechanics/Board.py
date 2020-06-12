import random
import time
from GameFlow.console.Console import Console
from GameMechanics.Inspector import Inspector
from GameMechanics.Position import Pos
from enum import Enum


class Board(object):

    """
    Only the container for most of the game information
    """
    ROWS = 6
    COLUMNS = 7

    class State(Enum):
        ACTIVE_GAME = 0
        INACTIVE_GAME = 1
        RESET = 2

    class ActiveState(Enum):
        PLAYER_ONE_TURN = 0
        PLAYER_TWO_TURN = 1

    def __init__(self, p1, p2):
        """ """
        self.console = Console()
        self.STATE = Board.State.ACTIVE_GAME
        # item [player ID, col]
        self.HISTORY = []

        self.ACTIVE_STATE = None
        self.pick_player_start()

        self.PLAYER_ONE = p1
        self.PLAYER_TWO = p2
        self.REFEREE = Inspector(self)

        self.PLAYER_ONE.BOARD = self
        self.PLAYER_TWO.BOARD = self

        # create board
        self.FIELD = [[], [], [], [], [], [], []]
        # filling board
        for c in range(0, Board.COLUMNS):
            for r in range(0, Board.ROWS):
                self.FIELD[c].append(None)

    def pick_player_start(self):
        select = random.random()
        if select < 0.5:
            self.ACTIVE_STATE = Board.ActiveState.PLAYER_ONE_TURN
        else:
            self.ACTIVE_STATE = Board.ActiveState.PLAYER_TWO_TURN

    # board creation/ analysis
    def reset_board(self):
        # fill board with NONE
        for c in range(0, Board.COLUMNS):
            for r in range(0, Board.ROWS):
                self.FIELD[c][r] = None

        self.HISTORY = []
        self.PLAYER_ONE.reset()
        self.PLAYER_TWO.reset()

    def print_board(self):
        self.console.clear_console()
        print("*"*50)
        # print spectator stats
        print("{}\n{}\n".format(str(self.PLAYER_ONE), str(self.PLAYER_TWO)))

        print(" ", end="")
        for c in range(1, Board.COLUMNS+1):
            print(" {} ".format(c), end="")
        print()

        for r in range(Board.ROWS-1, -1, -1):
            print("[", end="")
            for c in range(0, Board.COLUMNS):
                if self.FIELD[c][r] is None:
                    print(" - ", end="")
                else:
                    print(" {} ".format(str(self.FIELD[c][r])), end="")
            print("] -- {}".format(r+1), end="\n")

        print("*" * 50)
        print("Type a number and press enter to place a piece in that column")
        print("Type in 'q' or 'quit' to quit")
        print("*" * 50)

    def get_history(self):
        """

        :return: self.HISTORY: list of all moves in the game
        """
        return self.HISTORY

    def print_history(self):
        """

        :return:
        """
        print("-"*50)
        print("HISTORY")
        move_index = 0
        for piece in self.HISTORY:
            print("MOVE {}: {} --> COL {}".format(move_index, piece[0], piece[1]))
            move_index += 1
        print("-" * 50)

    def get_col_height(self, col):
        assert(1 <= col <= 7)
        count = 0
        column = self.FIELD[col-1]

        for piece in column:
            if piece is not None:
                # this is a piece, count it
                count += 1

        return count

    def get_piece(self, row, column):
        """

        :param row:
        :param column:
        :return:
        """
        assert(1 <= row <= self.ROWS)
        assert (1 <= column <= self.COLUMNS)

        return self.FIELD[column-1][row-1]

    # board manipulation
    def set_piece(self, player, column):
        height = self.get_col_height(column)

        if height >= Board.ROWS:
            # print("no space")
            return False
        else:
            pos = Pos(height+1, column)
            piece = player.give_piece(pos=pos)
            if piece is not None:
                index = piece.get_pos_index()
                self.FIELD[index[1]][index[0]] = piece
                return True
            else:
                # no more pieces to give
                # print("no pieces")
                return False
