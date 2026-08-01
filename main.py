# Simplifying the initializing
from src.game import SonicHackNSlashPanda3D


if __name__ == "__main__":
    game : SonicHackNSlashPanda3D = SonicHackNSlashPanda3D(
        "src/assets/3d-objects/floor.glb",
        {
            "idle": "src/assets/sprites/sonic/idle/sonic_idle.egg",
            "run": "src/assets/sprites/sonic/run/sonic_run.egg",
        }
    )
    game.run()
