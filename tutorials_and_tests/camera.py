from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from math import pi, sin, cos
from direct.gui.OnscreenText import OnscreenText

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.scene = self.loader.loadModel("models/environment")
        self.scene.reparentTo(self.render)
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

        self.taskMgr.add(self.topDownCameraTask, "TopDownCameraTask")

        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(0.005, 0.005, 0.005)
        self.pandaActor.reparentTo(self.render)
        self.pandaActor.loop("walk")

        self.pandaPos = self.pandaActor.getPos() # Init pos

        # Keybinds
        self.accept('w', self.setKey, ['forward', True])
        self.accept('w-up', self.setKey, ['forward', False])
        self.accept('s', self.setKey, ['backward', True])
        self.accept('s-up', self.setKey, ['backward', False])
        self.accept('a', self.setKey, ['left', True])
        self.accept('a-up', self.setKey, ['left', False])
        self.accept('d', self.setKey, ['right', True])
        self.accept('d-up', self.setKey, ['right', False])

        # Update position
        self.taskMgr.add(self.updatePandaTask, "UpdatePandaTask")

        self.keys = {"forward": False, "backward": False, "left": False, "right": False}

        self.coordText = OnscreenText(
            text="Panda Coordinates: (0, 0, 0)",
            pos=(0, 0.9),
            scale=0.07,
            fg=(1, 1, 1, 1),
            align=1,
            mayChange=True
        )

    def setKey(self, key, value):
        self.keys[key] = value

    def updatePandaTask(self, task):
        speed = 5.0

        if self.keys["forward"]:
            self.pandaPos.setY(self.pandaPos.getY() + speed * globalClock.getDt())
        if self.keys["backward"]:
            self.pandaPos.setY(self.pandaPos.getY() - speed * globalClock.getDt())
        if self.keys["left"]:
            self.pandaPos.setX(self.pandaPos.getX() - speed * globalClock.getDt())
        if self.keys["right"]:
            self.pandaPos.setX(self.pandaPos.getX() + speed * globalClock.getDt())

        self.pandaActor.setPos(self.pandaPos)
        self.coordText.setText(f"Panda Position: ({self.pandaPos.getX():.2f}, {self.pandaPos.getY():.2f}, {self.pandaPos.getZ():.2f})")

        return Task.cont

    def topDownCameraTask(self, task):
        self.camera.setPos(0, 0, 60)
        self.camera.lookAt(0, 0, 0)
        return Task.cont

app = MyApp()
app.run()
