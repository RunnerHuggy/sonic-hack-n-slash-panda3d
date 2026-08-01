from direct.showbase.ShowBaseGlobal import globalClock
from pathlib import Path
from panda3d.core import CardMaker

class Player:
    def __init__(self, base):
        self.base = base

        