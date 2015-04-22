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

	# Removes a node from the world
	def remove_node(self, node):
		for neighbor in node.get_neighbors():
			neighbor.remove_neighbor(node)
		self.nodes.remove(node)

	# Gets the node at a given point. Returns None if no node exists at point
	def get_node(self, p):
		for node in self.nodes:
			if node.getX() == p.getX() and node.getY() == p.getY():
				return node
		return None

	# Connects two nodes. i.e. sets each other as neighbors
	def link(self, n1, n2):
		n1.add_neighbor(n2)
		n2.add_neighbor(n1)

	# Gets the distance between two nodes
	def get_dist(self, n1, n2):
		return n1.get_dist(n2)

	# Calculates the best path from start node to goal node using A* algorithm
	def find_path(self, start, goal):
		closedset = []
		openset = [start]

		while len(openset) != 0:
			current = openset[0]
			for node in openset:
				if node.get_fscore() < current.get_fscore():
					current = node
			if current == goal:
				return self.reconstruct_path(goal)
			openset.remove(current)
			closedset.append(current)
			for neighbor in current.get_neighbors():
				if neighbor in closedset: continue
				tentative_gscore = current.get_gscore() + self.get_dist(current, neighbor)
				if neighbor not in openset or tentative_gscore < neighbor.get_gscore():
					neighbor.set_parent(current)
					neighbor.set_gscore(tentative_gscore)
					neighbor.set_fscore(neighbor.get_gscore() + self.get_dist(neighbor, goal))
					if neighbor not in openset:
						openset.insert(0, neighbor)

		return "Could not find path!"

	# Reconstructs the path taken to get to the goal node
	def reconstruct_path(self, current):
		total_path = [current]
		while current.get_parent() != None:
			current = current.get_parent()
			total_path.insert(0, current)
		for node in self.nodes:
			node.set_parent(None)
			node.set_gscore(0)
			node.set_fscore(0)
		return total_path

	# Gets all nodes in world
	def get_nodes(self):
		return self.nodes

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
