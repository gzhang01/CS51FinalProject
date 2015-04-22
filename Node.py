class Node:
    def __init__(self, p):
        self.point = p
        # neighbors is a list of other points near this node that are also nodes
        self.neighbors = []
        
    def getX(self) :
        return self.point.getX()
        
    def getY(self):
        return self.point.getY()
        
    def get_point(self):
        return self.point

    def get_dist(self, other):
        return ((self.getX() - other.getX()) ** 2 + (self.getY() - other.getY()) ** 2) ** 0.5
        
    def get_neighbors(self):
        return self.neighbors
        
    def add_neighbor(self, other):
        self.neighbors.append(other)
        
    def remove_neighbor(self, other):
        self.neighbors.remove(other)
        
    def is_obstacle(self, other):
        # returns whether there is an obstacle between two Nodes
        return False

    def __str__(self):
        return "({0}, {1})".format(self.getX(), self.getY())

    def print_neighbors(self):
        print "["
        for node in self.get_neighbors():
            print node
        print "]"

