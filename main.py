# Symplifying the initializing
from src.game import SonicHackNSlashPanda3D

if __name__ == "__main__":
    game : SonicHackNSlashPanda3D = SonicHackNSlashPanda3D("src/assets/3d-objects/floor.glb")
    game.run()
