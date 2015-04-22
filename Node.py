class Node:
    def __init__(self, p):
        self.point = p
        # Neighbors is a list of other points near this node that are also nodes
        self.neighbors = []
        # The follow are used in the A* algorithm
        self.g_score = 0
        self.f_score = 0
        self.parent = None
        
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
        if other in self.neighbors:
            self.neighbors.remove(other)
        else: print "Trying to remove non-existent neighbor!"
        
    def get_gscore(self):
        return self.g_score

    def set_gscore(self, i):
        self.g_score = i

    def get_fscore(self):
        return self.f_score

    def set_fscore(self, i):
        self.f_score = i

    def get_parent(self):
        return self.parent

    def set_parent(self, node):
        self.parent = node

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

