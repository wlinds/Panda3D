from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from math import pi, sin, cos

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

    def topDownCameraTask(self, task):
        self.camera.setPos(0, 0, 60)
        self.camera.lookAt(0, 0, 0)
        return Task.cont

app = MyApp()
app.run()
