from Graphics import *

class Robot:
    def __init__(self, p, world, r):
        self.center = p
        self.r = r
        self.world = world
        self.robot = Circle(self.center, self.r)
        self.robot.setFill("Purple")
        world.get_world().addItem(self)
        self.name = "robot"

    def get_center(self):
        return self.center

    def get_radius(self) :
        return self.r

    # Destination must be a node!
    def move(self, destination):
        self.center = destination.get_point()
        self.robot.setCenter(self.center)
        self.world.draw_objects()

    def undraw(self):
        self.robot.undraw()

    def draw(self, window):
        self.robot.draw(window)

    def get_location(self):
        return self.get_center()

    def get_name(self):
        return self.name

    def __str__(self):
        return "Robot at ({0}, {1})".format(self.center.getX(), self.center.getY())