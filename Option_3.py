from Graphics import *
import random

# Returns True if no other node is within 30 units. False otherwise
def check_dist(world, n):
	for node in world.get_nodes():
		if node.equals(n):
			continue
		elif world.get_dist(node, n) < 50:
			world.remove_node(n)
			return False
	return True

def initialize_nodes(world, num_nodes):
	for i in range(num_nodes):
		while True:
			name = str(i + 1)
			n = world.add_node(Point(random.randint(20, 495), random.randint(20, 495)), name)
			if check_dist(world, n):
				break
		nodes = world.get_nodes()
		for i in range(len(nodes)):
			if random.randint(0, (int) (n.get_dist(nodes[i]))) < 20:
				world.link(n, nodes[i])

def option_3(world, robot_radius):
	# Restricting to between 25 and 50
	# Less than 25 -- too few links; Greater than 50 -- too messy
	num_nodes = 0
	while num_nodes < 25 or num_nodes > 50:
		num_nodes = (int)(raw_input("Enter number of nodes to draw (within 25 and 50): "))
	initialize_nodes(world, num_nodes)
	world.draw_nodes(False)
	for node in world.get_nodes():
		if len(node.get_neighbors()) != 0:
			start = node
			break
	robot = world.add_robot(start.get_point(), world, robot_radius)
	world.draw_objects()

	while True:
		while True:
			usrinput = raw_input("Enter a node to navigate to: ")
			found, node = world.find_node_from_string(usrinput)
			if found:
				goal = node
				break
			print "Invalid Node!"
		world.nav(robot, goal)