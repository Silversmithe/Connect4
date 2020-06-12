"""
A class specifically for examining the board
"""


class Inspector(object):
    """
    Examines the board it has been given and returns
    information on the groupings of pieces.
    - So the inspector passes this information onto the
    controller to change the state of the board
    OR
    - the inspector passes the information onto the
    AI to make a decision
    """

    def __init__(self, board):
        self.BOARD = board

    def get_all_horizontal(self, identity):
        """

        :return: array of all groups of pieces of a certian id
        """
        # check for wins in the horizontal direction
        # brute force, all encompasing algorithm
        all_groups = []
        group = []
        for r in range(0, self.BOARD.ROWS):
            for c in range(0, self.BOARD.COLUMNS):
                if self.BOARD.FIELD[c][r] is None:
                    if len(group) > 0:
                        # if has 4 values, store and reset
                        all_groups.append(group)
                        group = []

                elif self.BOARD.FIELD[c][r].ID != identity:
                    # so if id of piece is not equal to ID you are
                    # looking for, reset set
                    if len(group) > 0:
                        # if has 4 values, store and reset
                        all_groups.append(group)
                        group = []

                elif self.BOARD.FIELD[c][r].ID == identity:
                    group.append(self.BOARD.FIELD[c][r])

        return all_groups

    # functions for scanning the grid
    def check_all_horizontal(self, identity):
        """

        :return: True if this ID wins, False if not
        """
        # check for wins in the horizontal direction
        # brute force, all encompasing algorithm
        horizontal_groupings = self.get_all_horizontal(identity)

        for group in horizontal_groupings:
            if len(group) >= 4:
                return [True, group]

        return [False, None]

    def get_all_vertical(self, identity):
        """

        :return: array of all groups of pieces of a certian id
        """
        # check for wins in the horizontal direction
        # brute force, all encompasing algorithm
        all_groups = []
        group = []
        for c in range(0, self.BOARD.COLUMNS):
            for r in range(0, self.BOARD.ROWS):
                if self.BOARD.FIELD[c][r] is None:
                    if len(group) > 0:
                        # if has 4 values, store and reset
                        all_groups.append(group)
                        group = []

                elif self.BOARD.FIELD[c][r].ID != identity:
                    # so if id of piece is not equal to ID you are
                    # looking for, reset set
                    if len(group) > 0:
                        # if has 4 values, store and reset
                        all_groups.append(group)
                        group = []

                elif self.BOARD.FIELD[c][r].ID == identity:
                    group.append(self.BOARD.FIELD[c][r])

        return all_groups

    def check_all_vertical(self, identity):
        """

        :return: size four array of locations
        """
        # check for wins in the vertical direction
        # brute force, all encompasing algorithm
        vertical_groups = self.get_all_vertical(identity)

        for group in vertical_groups:
            if len(group) >= 4:
                return [True, group]

        return [False, None]

    def get_all_diagonal(self, identity):
        """
        RISING SLASH ALGORITHM
        find all the horizontal checkers

        :param identity:
        :return:
        """
        temp_rise = []
        temp_drop = []
        group = []

        def increase_y(x, intercept):
            """
            a[5, -6]
            y = x + a

            :param x: slope
            :param intercept: y_intercept
            :return:
            """
            return x + intercept

        def decrease_y(x, intercept):
            """
            a[5, -6]
            y = (8+a)-x

            :param x: slope
            :param intercept: y_intercept
            :return:
            """
            return (8 + intercept) - x

        # actualy algorithm
        for a in range(-6, 6):
            # iterate through each intercept
            for c in range(1, self.BOARD.COLUMNS+1):

                # for each intercept iterate through each diagonal for function
                # check out rise first

                #######################
                # RISE VALUE
                #######################
                rise_val = increase_y(c, a)

                # if rise val is within acceptable row
                if 1 <= rise_val <= self.BOARD.ROWS:

                    # print(c, " ", rise_val)
                    # check identity
                    piece = self.BOARD.get_piece(row=rise_val, column=c)

                    if piece is None:
                        if len(temp_rise) > 0:
                            group.append(temp_rise)
                            temp_rise = []

                    elif piece.get_id() == identity:
                        # if identity, add to list
                        temp_rise.append(piece)

                    else:
                        # if the piece exists but is not the right
                        # identity
                        if len(temp_rise) > 0:
                            group.append(temp_rise)
                            temp_rise = []

                else:
                    # reached the end of a diagonal
                    # if the temp rise has something in it
                    # fill into group list
                    if len(temp_rise) > 0:
                        group.append(temp_rise)
                        temp_rise = []

                #######################
                # FALL VALUE
                #######################
                drop_val = decrease_y(c, a)

                # if rise val is within acceptable row
                if 1 <= drop_val <= self.BOARD.ROWS:

                    # check identity
                    piece = self.BOARD.get_piece(row=drop_val, column=c)

                    if piece is None:
                        if len(temp_drop) > 0:
                            group.append(temp_drop)
                            temp_drop = []

                    elif piece.get_id() == identity:
                        # if identity, add to list
                        temp_drop.append(piece)

                    else:
                        # if the piece exists but is not the right
                        # identity
                        if len(temp_drop) > 0:
                            group.append(temp_drop)
                            temp_drop = []

                else:
                    # reached the end of a diagonal
                    # if the temp rise has something in it
                    # fill into group list
                    if len(temp_drop) > 0:
                        group.append(temp_drop)
                        temp_drop = []

            # final flush of diagonals
            if len(temp_rise) > 0:
                group.append(temp_rise)
                temp_rise = []

            if len(temp_drop) > 0:
                group.append(temp_drop)
                temp_drop = []

        return group

    def check_all_diagonal(self, identity):
        """

        :return: size four array of locations
        """
        # check for wins in the vertical direction
        # brute force, all encompasing algorithm
        diagonal_groups = self.get_all_diagonal(identity=identity)

        for group in diagonal_groups:
            if len(group) >= 4:
                return [True, group]

        return [False, None]