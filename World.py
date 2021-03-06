from Graphics import *
from Node import Node
from Robot import Robot
import Helpers

class World:
	def __init__(self):
		self.world = GraphWin("World", 500, 500)
		# List of nodes in world. May use other data type later
		self.nodes = []
		self.objects = []

	# Creates a node object and adds it to the world
	def add_node(self, p, name):
		new_node = Node(p, name)
		self.nodes.append(new_node)
		return new_node

	# Removes a node from the world
	def remove_node(self, node):
		for neighbor in node.get_neighbors():
			neighbor.remove_neighbor(node)
		self.nodes.remove(node)

	# Takes top left (p1) and bottom right (p2) points
	def remove_nodes_inside(self, p1, p2, mult):
		xlist = Helpers.get_multiples(p1.getX(), p2.getX(), mult)
		ylist = Helpers.get_multiples(p1.getY(), p2.getY(), mult)
		for x in xlist:
			for y in ylist:
				node = self.get_node(Point(x, y))
				if node is not None:
					self.remove_node(self.get_node(Point(x, y)))

	# Gets the node at a given point. Returns None if no node exists at point
	def get_node(self, p):
		for node in self.nodes:
			if node.getX() == p.getX() and node.getY() == p.getY():
				return node
		return None

	def find_node_from_string(self, string):
		nodes = self.get_nodes()
		for node in nodes:
			if string == node.get_name(): 
				return True, node
		return False, None

	# Adds a robot to the world. p should be a point
	def add_robot(self, p, world, r=20):
		new_robot = Robot(p, world, r)
		self.objects.append(new_robot)
		return new_robot

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

		print "Could not find path!"
		return []

	# Reconstructs the path taken to get to the goal node
	def reconstruct_path(self, current):
		total_path = [current]
		while current.get_parent() != None:
			current = current.get_parent()
			total_path.insert(0, current)
		return total_path

	# Navigates obj to goal. If show == True, prints info to terminal
	def nav(self, obj, goal, show=True):
		start = self.get_node(obj.get_location())
		path = self.find_path(start, goal)
		for node in path:
			while not obj.get_location().equals(node):
				if show:
					print "Robot at node: {0}, Next node: {1}, Goal: {2}, Distance traveled: {3}".format(
						self.get_node(obj.get_location()).get_name(), node.get_name(), goal.get_name(), node.get_gscore())
				obj.move(node)
				time.sleep(0.3)
		for node in self.nodes:
			node.set_parent(None)
			node.set_gscore(0)
			node.set_fscore(0)


	# Gets all nodes in world
	def get_nodes(self):
		return self.nodes

	# Gets the drawable world
	def get_world(self):
		return self.world

	# Draws all nodes on the screen
	def draw_nodes(self, draw_dist=True):
		for node in self.get_nodes():
			for neighbor in node.get_neighbors():
				road = Line(node.get_point(), neighbor.get_point())
				road.draw_once(self.get_world())
				if draw_dist:
					midpt = road.get_midpoint()
					dist = Text(midpt, "{0}".format(int(round(self.get_dist(node, neighbor)))))
					dist.draw_once(self.get_world())
		for node in self.get_nodes():
			c=Circle(node.get_point(), 10)
			c.setFill("aquamarine")
			c.draw_once(self.get_world())
			text = Text(node.get_point(), node.get_name())
			text.draw_once(self.get_world())

	def draw_option_2(self):
		for node in self.nodes:
			if node.get_name() == "start":
				c = Circle(node.get_point(), 3)
				c.setFill("green")
				c.draw_once(self.world)
			if node.get_name() == "goal":
				c = Circle(node.get_point(), 3)
				c.setFill("red")
				c.draw_once(self.world)

	# Draws all objects on the screen
	# TODO: Make robot move when the center updates
	def draw_objects(self):
		self.world.redraw()

	# Erases everything in world
	# Note: nodes never get erased in testing as nodes should never move!
	def reset(self):
		pass
