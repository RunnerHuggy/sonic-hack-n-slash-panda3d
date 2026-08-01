from direct.showbase.ShowBaseGlobal import globalClock

class Player:
    def __init__(self, base, anim_path: dict):
        self.base = base

        # Load the idle animation.
        self.idle_anim = base.loader.loadModel(str(anim_path["idle_right"]))
        self.idle_anim.reparentTo(base.render)
        self.idle_anim.setPos(0, 0, 0.75)
        self.idle_seq = self._get_sequence_node(self.idle_anim)

        # Load the run animation.
        self.run_anim = base.loader.loadModel(str(anim_path["run_right"]))
        self.run_anim.reparentTo(base.render)
        self.run_anim.setPos(0, 0, 0.75)
        self.run_seq = self._get_sequence_node(self.run_anim)

        self.idle_anim_show()
        self.run_anim_hide()

        self.is_moving = False
        self.facing = "right"

        self.speed = 5.0

        self.keys = {
            "left": False,
            "right": False
        }

        self._setup_input()

        base.taskMgr.add(self.update, "player-update")

    def _get_sequence_node(self, model_root):
        node_path = model_root.find("**/+SequenceNode")
        if node_path.isEmpty():
            raise ValueError(
                f"No sequence found under {model_root} - "
                "check that the egg file has a <Switch> { 1 } group"
            )
        return node_path.node()

    def _setup_input(self):
        #Moving left
        self.base.accept("a", self._set_key, ["left", True])
        self.base.accept("a-up", self._set_key, ["left", False])

        #Moving right
        self.base.accept("d", self._set_key, ["right", True])
        self.base.accept("d-up", self._set_key, ["right", False])

    def _set_key(self, key, value):
        self.keys[key] = value

    # Facing
    def face_right(self):
        self.idle_anim.setH(0)
        self.run_anim.setH(0)
        self.facing = "right"

    def face_left(self):
        self.idle_anim.setH(180)
        self.run_anim.setH(180)
        self.facing = "left"

    # Animations
    def idle_anim_show(self):
        self.idle_anim.show()
        self.idle_seq.loop(True)

    def idle_anim_hide(self):
        self.idle_anim.hide()
        self.idle_seq.stop()

    def run_anim_show(self):
        self.run_anim.show()
        self.run_seq.loop(True)

    def run_anim_hide(self):
        self.run_anim.hide()
        self.run_seq.stop()

    def update(self, task):
        dt = globalClock.getDt()

        moving = self.keys["left"] or self.keys["right"]

        if self.keys["left"]:
            self.idle_anim.setX(self.idle_anim.getX() - self.speed * dt)
            self.run_anim.setX(self.run_anim.getX() - self.speed * dt)
            if self.facing != "left":
                self.face_left()
        elif self.keys["right"]:
            self.idle_anim.setX(self.idle_anim.getX() + self.speed * dt)
            self.run_anim.setX(self.run_anim.getX() + self.speed * dt)
            if self.facing != "right":
                self.face_right()

        if moving and not self.is_moving:
            self.idle_anim_hide()
            self.run_anim_show()
            self.is_moving = True
        elif not moving and self.is_moving:
            self.idle_anim_show()
            self.run_anim_hide()
            self.is_moving = False

        return task.cont