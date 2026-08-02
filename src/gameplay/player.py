from direct.showbase.ShowBaseGlobal import globalClock

class Player:
    def __init__(self, base, anim_path: dict):
        self.base = base
        self.x_pos = 0.0

        # Load the idle animation.
        # Right
        self.idle_anim_right = base.loader.loadModel(str(anim_path["idle_right"]))
        self.idle_anim_right.reparentTo(base.render)
        self.idle_anim_right.setPos(0, 0, 0.1)
        self.idle_seq_right = self._get_sequence_node(self.idle_anim_right)

        # Left
        self.idle_anim_left = base.loader.loadModel(str(anim_path["idle_left"]))
        self.idle_anim_left.reparentTo(base.render)
        self.idle_anim_left.setPos(0, 0, 0.1)
        self.idle_seq_left = self._get_sequence_node(self.idle_anim_left)

        # Right
        self.run_anim_right = base.loader.loadModel(str(anim_path["run_right"]))
        self.run_anim_right.reparentTo(base.render)
        self.run_anim_right.setPos(0, 0, 0.1)
        self.run_seq_right = self._get_sequence_node(self.run_anim_right)

        # Left
        self.run_anim_left = base.loader.loadModel(str(anim_path["run_left"]))
        self.run_anim_left.reparentTo(base.render)
        self.run_anim_left.setPos(0, 0, 0.1)
        self.run_seq_left = self._get_sequence_node(self.run_anim_left)

        self.idle_anim_right_show()

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

    # Animations
    def idle_anim_right_show(self):
        self.idle_anim_right.show()
        self.idle_anim_left.hide()
        self.run_anim_right.hide()
        self.run_anim_left.hide()

        self.idle_seq_right.loop(True)
        self.idle_seq_left.stop()
        self.run_seq_right.stop()
        self.run_seq_left.stop()

    def idle_anim_left_show(self):
        self.idle_anim_right.hide()
        self.idle_anim_left.show()
        self.run_anim_right.hide()
        self.run_anim_left.hide()

        self.idle_seq_right.stop()
        self.idle_seq_left.loop(True)
        self.run_seq_right.stop()
        self.run_seq_left.stop()

    def run_anim_right_show(self):
        self.idle_anim_right.hide()
        self.idle_anim_left.hide()
        self.run_anim_right.show()
        self.run_anim_left.hide()

        self.idle_seq_right.stop()
        self.idle_seq_left.stop()
        self.run_seq_right.loop(True)
        self.run_seq_left.stop()

    def run_anim_left_show(self):
        self.idle_anim_right.hide()
        self.idle_anim_left.hide()
        self.run_anim_right.hide()
        self.run_anim_left.show()

        self.idle_seq_right.stop()
        self.idle_seq_left.stop()
        self.run_seq_right.stop()
        self.run_seq_left.loop(True)

    def update(self, task):
        dt = globalClock.getDt()

        moving = self.keys["left"] or self.keys["right"]

        if self.keys["left"]:
            self.x_pos -= self.speed * dt
            self.facing = "left"
        elif self.keys["right"]:
            self.x_pos += self.speed * dt
            self.facing = "right"

        # Apply the single shared position to all four models
        for model in (self.idle_anim_right, self.idle_anim_left,
                      self.run_anim_right, self.run_anim_left):
            model.setX(self.x_pos)

        if moving and not self.is_moving:
            if self.facing == "left":
                self.run_anim_left_show()
            else:
                self.run_anim_right_show()
            self.is_moving = True
        elif not moving and self.is_moving:
            if self.facing == "left":
                self.idle_anim_left_show()
            else:
                self.idle_anim_right_show()
            self.is_moving = False

        return task.cont