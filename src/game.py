#Importing the ShowBase class.
from direct.showbase.ShowBase import ShowBase

class SonicHackNSlashPanda3D(ShowBase):
    """
    The core of the game
    """
    def __init__(self):
        """
        Initializes the game.

        :param self the object itself
        """
        ShowBase.__init__(self)