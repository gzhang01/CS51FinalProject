import World
from Graphics import *
import random

world = World.World()

def initialize_nodes():
	for i in range(25):
		name = "n" + str(i + 1)
		n = world.add_node(Point(random.randint(5, 495), random.randint(5, 495)), name)
		nodes = world.get_nodes()
		for i in range(len(nodes)):
			if random.randint(0, (int) (n.get_dist(nodes[i]))) < 20:
				world.link(n, nodes[i])

# n1 = world.add_node(Point(50, 50), "n1")
# n2 = world.add_node(Point(50, 225), "n2")
# n3 = world.add_node(Point(200, 50), "n3")
# n4 = world.add_node(Point(200, 100), "n4")
# n5 = world.add_node(Point(300, 250), "n5")
# n6 = world.add_node(Point(250, 400), "n6")
# n7 = world.add_node(Point(175, 175), "n7")
# n8 = world.add_node(Point(138, 196), "n8")
# world.link(n1, n2)
# world.link(n1, n3)
# world.link(n3, n4)
# world.link(n2, n5)
# world.link(n4, n5)
# world.link(n2, n6)
# world.link(n5, n6)
# world.link(n1, n7)
# world.link(n7, n6)
# world.link(n3, n8)
# world.link(n5, n8)

def find_node(string):
	nodes = world.get_nodes()
	for node in nodes:
		if string == node.get_name(): 
			return True, node
	return False, None

# for i in range(100, 500, 100):
# 	for j in range(100, 500, 100):
# 		world.add_node(Point(i, j))
# for node in world.get_nodes():
# 	n1 = world.get_node(Point(node.getX()+100, node.getY()))
# 	n2 = world.get_node(Point(node.getX()+100, node.getY()+100))
# 	n3 = world.get_node(Point(node.getX(), node.getY()+100))
# 	n4 = world.get_node(Point(node.getX()-100, node.getY()+100))
# 	if n1 != None: world.link(node, n1)
# 	if n2 != None: world.link(node, n2)
# 	if n3 != None: world.link(node, n3)
# 	if n4 != None: world.link(node, n4)

# world.remove_node(world.get_node(Point(200, 200)))
# goal = world.get_node(Point(400, 400))
# start = world.get_node(Point(100, 100))
# path = world.find_path(start, goal)
# for node in path:
# 	print node

# path = world.find_path(n1, n6)
# for node in path:
# 	print node
# for node in world.get_nodes():
# 	assert node.get_parent() == None
# 	assert node.get_fscore() == 0
# 	assert node.get_gscore() == 0


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






