from direct.showbase.ShowBase import ShowBase 
class SpaceJam(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.SetupScene()
  
    def SetupScene(self):
        self.Universe = self.loader.loadModel("./Assets/Universe/Universe.x")
        self.Universe.reparentTo(self.render)
        self.Universe.setScale(15000)

        self.Planet1 = self.loader.loadModel("./Assets/Planets/protoPlanet.x.obj")
        self.Planet1.reparentTo(self.render)
        self.Planet1.setPos(150, 5000, 67)
        self.Planet1.setScale(350)
        tex = self.loader.loadTexture("./Assets/Planets/Blue-Ice.jpg")
        self.Planet1.setTexture(tex, 1)

        self.Planet2 = self.loader.loadModel("./Assets/Planets/protoPlanet.x.obj")
        self.Planet2.reparentTo(self.render)
        self.Planet2.setPos(200, 6000, 80)
        self.Planet2.setScale(450)
        tex = self.loader.loadTexture("./Assets/Planets/Color-Shift.jpg")
        self.Planet2.setTexture(tex, 1)

        self.Planet3 = self.loader.loadModel("./Assets/Planets/protoPlanet.x.obj")
        self.Planet3.reparentTo(self.render)
        self.Planet3.setPos(100, 3000, 50)
        self.Planet3.setScale(400)
        tex = self.loader.loadTexture("./Assets/Planets/Concrete.png")
        self.Planet3.setTexture(tex, 1)

        self.Planet4 = self.loader.loadModel("./Assets/Planets/protoPlanet.x.obj")
        self.Planet4.reparentTo(self.render)
        self.Planet4.setPos(500, 4550, 60)
        self.Planet4.setScale(350)
        tex = self.loader.loadTexture("./Assets/Planets/Exo-Planet tex.jpg")
        self.Planet4.setTexture(tex, 1)

        self.Planet5 = self.loader.loadModel("./Assets/Planets/protoPlanet.x.obj")
        self.Planet5.reparentTo(self.render)
        self.Planet5.setPos(300, 4000, 45)
        self.Planet5.setScale(350) 
        tex = self.loader.loadTexture("./Assets/Planets/Hardening_Lava.png")
        self.Planet5.setTexture(tex, 1)


        self.Planet6 = self.loader.loadModel("./Assets/Planets/protoPlanet.x.obj")
        self.Planet6.reparentTo(self.render)
        self.Planet6.setPos(175, 5200, 90)
        self.Planet6.setScale(350)
        tex = self.loader.loadTexture("./Assets/Planets/iceWorld.jpg")
        self.Planet6.setTexture(tex, 1)

        self.Ship1 = self.loader.loadModel("./Assets/Spaceships/spaceship.obj")
        self.Ship1.reparentTo(self.render)
        self.Ship1.setPos(100, 3280, 100)
        self.Ship1.setScale(500)
        self.Ship1.setTexture(tex, 1)

        self.Station1 = self.loader.loadModel("./Assets/Space Station/SpaceStation1B/spaceStation.x")
        self.Station1.reparentTo(self.render)
        self.Station1.setPos(110, 3300, 120)
        self.Station1.setScale(500)
        self.Station1.setTexture(tex, 1)

        self.tex = self.loader.loadTexture("./Assets/Universe/starfield-in-blue.jpg")
        self.Universe.setTexture(self.tex, 1)





app = SpaceJam()
app.run()