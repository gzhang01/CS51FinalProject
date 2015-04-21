class Node:
    def __init__(self, x, y, neighbors=[]):
        self.x = x
        self.y = y
        # neighbors is a list of other points near this node that are also nodes
        self.neighbors = neighbors
        
    def getX(self) :
        return self.x
        
    def getY(self):
        return self.y
        
    def get_point(self):
        return (self.getX(), self.getY())

    def get_dist(self, other):
        return ((self.x - other.getX()) ** 2 + (self.y - other.getY()) ** 2) ** 0.5
        
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
        return "({0}, {1})".format(self.get_x(), self.get_y())

node1 = Node(1, 1)
node2 = Node(2, 2)
print node1.get_dist(node2)
print node2.get_dist(node1)
node1.add_neighbor(node2)
for node in node1.get_neighbors():
    print node

