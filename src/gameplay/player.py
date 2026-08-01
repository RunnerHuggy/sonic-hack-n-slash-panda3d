from direct.showbase.ShowBaseGlobal import globalClock


class Player:
    def __init__(self, base, anim_path: dict):
        self.base = base

        self.idle_sprite = base.loader.loadModel(str(anim_path["idle"]))

        self.idle_sprite.reparentTo(base.render)

        self.idle_sprite.setPos(0, 0, 0.75)

    def update(self, task):
        dt = globalClock.getDt()

        return task.cont