

class Piece(object):

    def __init__(self, identity, pos):
        """

        :param identity: int : defines whose piece it is
        """
        # ID is a number
        self.ID = identity
        self.POS = pos

    def get_id(self):
        """
        Return Identity
        :return:
        """
        return self.ID

    def get_pos(self):
        """
        Return theoretical pos
        :return:
        """
        return self.POS.get_pos()

    def get_pos_index(self):
        """
        Return actual pos
        :return:
        """
        return self.POS.get_pos_index()

    def info(self):
        """
        Print info on piece
        :return:
        """
        print("ID: {}, POS: {}".format(self.ID, str(self.POS)))

    def __str__(self):
        return "{}".format(self.ID)
