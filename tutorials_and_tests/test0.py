from direct.showbase.ShowBase import ShowBase
from panda3d.core import PointLight, AmbientLight
from panda3d.core import Vec4

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Load a model and reparent it to render
        self.environ = self.loader.loadModel("models/environment")
        self.environ.reparentTo(self.render)

        # Scale and position the model
        self.environ.setScale(0.25, 0.25, 0.25)
        self.environ.setPos(-8, 42, 0)

        # Add lights to the scene
        plight = PointLight('plight')
        plight.setColor(Vec4(0.8, 0.8, 0.8, 1))
        plnp = self.environ.attachNewNode(plight)
        plnp.setPos(20, -20, 100)
        self.render.setLight(plnp)

        alight = AmbientLight('alight')
        alight.setColor(Vec4(0.2, 0.2, 0.2, 1))
        alnp = self.render.attachNewNode(alight)
        self.render.setLight(alnp)

if __name__ == "__main__":
    app = MyApp()
    app.run()
