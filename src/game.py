#Importing the ShowBase class.
from direct.showbase.ShowBase import ShowBase
from src.gameplay.player import Player

class SonicHackNSlashPanda3D(ShowBase):
    """
    The core of the game
    """
    def __init__(self, scene_path: str, sonic_anim_path: dict):
        """
        Initializes the game.

        :param scene_path : the path of the scene.
        """
        super().__init__(self)

        self.scene = self.loader.loadModel(scene_path)

        self.scene.reparentTo(self.render)

        self.scene.setPos(-8, 42, 0)

        self.player = Player(self, sonic_anim_path)