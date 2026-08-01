from direct.showbase.ShowBase import ShowBase

class SonicHackNSlashPanda3D(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)


if __name__ == "__main__":
    game : SonicHackNSlashPanda3D = SonicHackNSlashPanda3D()
    game.run()
