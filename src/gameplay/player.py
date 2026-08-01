from direct.showbase.ShowBaseGlobal import globalClock


class Player:
    def __init__(self, base, anim_path: dict):
        self.base = base

        # Load the idle animation.
        # self.idle_anim = base.loader.loadModel(str(anim_path["idle"]))
        # self.idle_anim.reparentTo(base.render)
        # self.idle_anim.setPos(0, 0, 0.75)

        # Load the run animation.
        self.run_anim = base.loader.loadModel(str(anim_path["run"]))
        self.run_anim.reparentTo(base.render)
        self.run_anim.setPos(0, 0, 0.75)

    def update(self, task):
        dt = globalClock.getDt()

        return task.cont