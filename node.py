class Node:
    def _init_(self, x, y, neighbors):
        self.x = x
        self.y = y
        # neighbors is a list of other points near this node that are also nodes
        self.neighbors = neighbors
        
    def get_x(self) :
        return self.x
        
    def get_y(self):
        return self.y
        
    def get_dist(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
        
    def get_neighbors(self):
        return self.neighbors
        
    def add_neighbor(self, other):
        neighbors.append(other)
        
    def remove_neighbor(self, other):
        neighbors.remove(other)
        
    def obstacles(self):
        # returns whether there is an obstacle between two Nodes


