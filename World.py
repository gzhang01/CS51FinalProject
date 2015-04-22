from Graphics import *
from Node import Node

class World:
	def __init__(self):
		self.world = GraphWin("World", 500, 500)
		# List of nodes in world. May use other data type later
		self.nodes = []

	# Creates a node object and adds it to the world
	def add_node(self, p):
		new_node = Node(p)
		self.nodes.append(new_node)
		return new_node

	# Gets the node at a given point. Returns None if no node exists at point
	def get_node(self, p):
		for node in self.nodes:
			if node.get_point() == p:
				return node
		return None

	# Connects two nodes. i.e. sets each other as neighbors
	def link(self, n1, n2):
		n1.add_neighbor(n2)
		n2.add_neighbor(n1)

	# Gets the distance between two nodes
	def get_dist(self, n1, n2):
		return n1.get_dist(n2)

	# Draws all nodes on the screen
	# Used for testing purposes; will not draw nodes in final result
	def draw_nodes(self):
		for node in self.nodes:
			c = Circle(node.get_point(), 3)
			c.setFill("black")
			c.draw(self.world)
			for neighbor in node.get_neighbors():
				path = Line(node.get_point(), neighbor.get_point())
				path.draw(self.world)
				midpt = path.get_midpoint()
				text = Text(midpt, "{0}".format(int(round(self.get_dist(node, neighbor)))))
				text.draw(self.world)

	# Erases everything in world
	# Note: nodes never get erased in testing as nodes should never move!
	def reset(self):
		pass
