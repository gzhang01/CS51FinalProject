from Graphics import *

class Robot:
    def __init__(self, p, world, r):
        self.center = p
        self.r = r
        self.robot = Circle(self.center, self.r)
        self.robot.setFill("Purple")
        world.addItem(self)
        # Determines velocity of the robot. Can be changed
        self.vel = 10

    def get_center(self):
        return self.center

    def get_radius(self) :
        return self.r

    # TODO: move needs to alter the location of robot, not just center
    def move(self, destination):
        if self.center.get_distance(destination) < self.vel:
            self.center = destination
        else: 
            dsvec = self.center.get_direction(destination, self.vel)
            self.center.move(dsvec.getX(), dsvec.getY())
        self.robot.setCenter(self.center)

    def undraw(self):
        self.robot.undraw()

    def draw(self, window):
        self.robot.draw(window)

    def __str__(self):
        return "Robot at ({0}, {1})".format(self.center.getX(), self.center.getY())