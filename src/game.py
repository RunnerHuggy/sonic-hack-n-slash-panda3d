#Importing the ShowBase class.
from direct.showbase.ShowBase import ShowBase

class SonicHackNSlashPanda3D(ShowBase):
    """
    The core of the game
    """
    def __init__(self, scene_path: str):
        """
        Initializes the game.

        :param scene_path : the path of the scene.
        """
        ShowBase.__init__(self)

        self.scene = self.loader.loadModel(scene_path)

        self.scene.reparentTo(self.render)

        self.scene.setPos(-8, 42, 0)