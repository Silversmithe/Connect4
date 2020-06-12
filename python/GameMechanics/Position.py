

class Pos(object):
    MIN = 1
    MAX_ROWS = 6
    MAX_COLS = 7

    """
    Defines a location on the board
    """
    def __init__(self, row, col):

        assert(Pos.MIN <= row <= Pos.MAX_ROWS)
        assert(Pos.MIN <= col <= Pos.MAX_COLS)

        self.row = row
        self.col = col

    def get_pos(self):
        """
        Return theoretical row and column
        :return:
        """
        return [self.row, self.col]

    def get_pos_index(self):
        """
        Return actual row and column for indexed arrays
        :return:
        """
        return [self.row-1, self.col-1]

    def __str__(self):
        """
        Returns string form
        :return:
        """
        return "({}, {})".format(self.row, self.col)

