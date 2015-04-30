import World
from Graphics import *
import random

def initialize_nodes():
	for i in range(25):
		name = "n" + str(i + 1)
		n = world.add_node(Point(random.randint(5, 495), random.randint(5, 495)), name)
		nodes = world.get_nodes()
		for i in range(len(nodes)):
			if random.randint(0, (int) (n.get_dist(nodes[i]))) < 20:
				world.link(n, nodes[i])

def find_node(string):
	nodes = world.get_nodes()
	for node in nodes:
		if string == node.get_name(): 
			return True, node
	return False, None

world = World.World()
initialize_nodes()
world.draw_nodes()
robot = world.add_robot(world.get_nodes()[0].get_point(), world)
world.draw_objects()

while True:
	while True:
		usrinput = raw_input("Select a node to navigate to: ")
		found, node = find_node(usrinput)
		if found:
			goal = node
			break
		print "Invalid Node!"
	world.nav(robot, goal)



## Example of mouse interaction!
# node_number = 1
# while True:
# 	p = world.get_world().getMouse()
# 	name = "n" + str(node_number)
# 	n = world.add_node(p, name)
# 	node_number += 1
# 	print "Drawing node at {0}".format(p)
# 	world.draw_node(n)




