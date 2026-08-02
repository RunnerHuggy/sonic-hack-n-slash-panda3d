# game.py
from direct.showbase.ShowBase import ShowBase
from direct.showbase.ShowBaseGlobal import globalClock

from src.gameplay.player import Player


class SonicHackNSlashPanda3D(ShowBase):
    """
    The core of the game
    """

    def __init__(self, scene_path: str, sonic_anim_path: dict):
        super().__init__(self)

        self.scene = self.loader.loadModel(scene_path)
        self.scene.reparentTo(self.render)
        self.scene.setPos(-8, 42, -0.75)

        # Camera settings
        self.camera.setPos(20, 35, 25)
        self.camera.lookAt(20, 35, 25)

        self.player = Player(self, sonic_anim_path)

        # Camera follows player
        self.taskMgr.add(self.update_camera, "camera-update")

    def update_camera(self, task):
        self.camera.setX(self.player.x_pos)

        return task.cont