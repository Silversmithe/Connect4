from GameMechanics.Events import Event
from GameMechanics.Piece import Piece
from GameMechanics.Position import Pos
from enum import Enum


class Spectator(object):

    MAX_PIECES = 21
    MIN_PIECES = 0


    class State(Enum):
        ACTIVE = 0
        INACTIVE = 1
        WIN = 3
        LOSE = 4
        TIE = 5

    def __init__(self, name, identity, ai=False, board=None):
        """
        initialize spectator
        """
        self.NAME = name
        self.AI = ai
        self.STATE = Spectator.State.ACTIVE
        self.ID = identity
        self.BOARD = board
        self.PIECE_COUNT = Spectator.MAX_PIECES
        self.QUIT = ["quit", "QUIT", "q", "Q"]

    # board manipulation
    def reset(self):
        self.PIECE_COUNT = Spectator.MAX_PIECES
        self.STATE = Spectator.State.ACTIVE

    # functions with board
    # can only observe the board, no editing it
    def set_board(self, board):
        self.BOARD = board

    def get_board(self):
        return self.BOARD if self.BOARD is not None else None

    # functions for pieces
    def give_piece(self, pos):
        if self.PIECE_COUNT == Spectator.MIN_PIECES:
            # no more pieces to give
            return None
        else:
            # decrement by one
            self.PIECE_COUNT -= 1
            # return a piece with the id of the player
            # and the specified position
            return Piece(self.ID, pos)

    def get_piece(self):
        if self.PIECE_COUNT < Spectator.MAX_PIECES:
            # increment by one
            self.PIECE_COUNT += 1

    # functions for movement decisions
    def human_move(self):
        """
        Function that gets human input
        :return:
        """
        move = -1
        while move < 1 or move > self.BOARD.COLUMNS:
            try:
                move = input("{}: Choose a column>>>  ".format(self.NAME))

                for i in self.QUIT:
                    if str(move) == i:
                        return None

                move = int(move)

            except KeyboardInterrupt:
                exit(0)
            except ValueError:
                pass
        if self.PIECE_COUNT <= 0:
            # cannot do anything
            self.STATE == Spectator.State.INACTIVE
            return None
        else:
            return move

    def ai_move(self):
        pass

    def player_move(self):
        # check for ai eventually
        if self.STATE == Spectator.State.ACTIVE:
            if self.AI:
                # AI MOVES
                # return self.ai_move()
                return self.human_move()

            else:
                # player moves
                return self.human_move()

        return None

    # build-in functions
    def __str__(self):
        return "PLAYER: {}\n" \
               "ID: {}\n" \
               "AI: {}\n" \
               "PIECES: {}\n".format(self.NAME,  self.ID, self.AI, self.PIECE_COUNT)
