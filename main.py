# Simplifying the initializing
from src.game import SonicHackNSlashPanda3D


if __name__ == "__main__":
    game : SonicHackNSlashPanda3D = SonicHackNSlashPanda3D(
        "src/assets/3d-objects/floor.glb",
        {
            "idle_right": "src/assets/sprites/sonic/idle/right/sonic_idle.egg",
            "run_right": "src/assets/sprites/sonic/run/right/sonic_run.egg",
        }
    )
    game.run()
