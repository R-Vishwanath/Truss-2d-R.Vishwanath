class MyTurtle(turtle.RawTurtle): # here we subclass the turtle to allow us to call statusbar updates after each movement
    def __init__(self, canvas):
        turtle.RawTurtle.__init__(self, canvas)
        self.bbox = [0,0,0,0]

    def _update_bbox(self): # keep a record of the furthers points visited
        pos = self.position()
        if pos[0] < self.bbox[0]:
            self.bbox[0] = pos[0]
        elif pos[0] > self.bbox[2]:
            self.bbox[2] = pos[0]
        if pos[1] < self.bbox[1]:
            self.bbox[1] = pos[1]
        elif pos[1] > self.bbox[3]:
            self.bbox[3] = pos[1]

    def forward(self, *args):
        turtle.RawTurtle.forward(self, *args)
        self._update_bbox()

    def backward(self, *args):
        turtle.RawTurtle.backward(self, *args)
        self._update_bbox()

    def right(self, *args):
        turtle.RawTurtle.right(self, *args)
        self._update_bbox()

    def left(self, *args):
        turtle.RawTurtle.left(self, *args)
        self._update_bbox()

    def goto(self, *args):
        turtle.RawTurtle.goto(self, *args)
        self._update_bbox()

    def setx(self, *args):
        turtle.RawTurtle.setx(self, *args)
        self._update_bbox()

    def sety(self, *args):
        turtle.RawTurtle.sety(self, *args)
        self._update_bbox()

    def setheading(self, *args):
        turtle.RawTurtle.setheading(self, *args)
        self._update_bbox()

    def home(self, *args):
        turtle.RawTurtle.home(self, *args)
        self._update_bbox()