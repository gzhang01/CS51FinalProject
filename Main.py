import World
from Graphics import *
import random
import Helpers

robot_radius = 20

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

# Takes top left (p1) and bottom right (p2) points
def remove_nodes_inside(p1, p2):
	xlist = Helpers.get_multiples(p1.getX(), p2.getX(), 2*robot_radius)
	ylist = Helpers.get_multiples(p1.getY(), p2.getY(), 2*robot_radius)
	for x in xlist:
		for y in ylist:
			world.remove_node(world.get_node(Point(x, y)))

def create_map():
	n1= world.add_node(Point(100,50), "1")
	n2 = world.add_node(Point(200,25), "2")
	n3 = world.add_node(Point(200,115), "3")
	n4 = world.add_node(Point(300,50), "4")
	n5 = world.add_node(Point(400,50), "5")
	n6 = world.add_node(Point(400,115), "6")
	n7 = world.add_node(Point(450,400), "7")
	n8 = world.add_node(Point(375,385), "8")
	n9 = world.add_node(Point(375,450), "9")
	n10 = world.add_node(Point(300,400), "10")
	n11 = world.add_node(Point(275,450), "11")
	n12 = world.add_node(Point(175,385), "12")
	n13 = world.add_node(Point(100,315), "13")
	n14 = world.add_node(Point(50,450), "14")
	n15 = world.add_node(Point(50,150), "15")

	world.link(n1, n2)
	world.link(n1, n3)
	world.link(n1, n4)
	world.link(n1, n13)
	world.link(n1, n15)
	world.link(n2, n4)
	world.link(n3, n6)
	world.link(n4, n5)
	world.link(n5, n6)
	world.link(n6, n7)
	world.link(n6, n8)
	world.link(n7, n9)
	world.link(n7, n8)
	world.link(n8, n9)
	world.link(n8, n10)
	world.link(n9, n10)
	world.link(n9, n11)
	world.link(n10, n11)
	world.link(n10, n12)
	world.link(n11, n12)
	world.link(n11, n14)
	world.link(n12, n13)
	world.link(n13, n14)
	world.link(n14, n15)


	park = Rectangle(Point(150,150), Point(350,350))
	park.setFill("green")
	park.draw_once(world.get_world())
	lake = Circle(Point(250,250), 75)
	lake.setFill("blue")
	lake.draw_once(world.get_world())
	for node in world.get_nodes():
		for neighbor in node.get_neighbors():
			road = Line(node.get_point(), neighbor.get_point())
			road.draw_once(world.get_world())
			midpt = road.get_midpoint()
			dist = Text(midpt, "{0}".format(int(round(world.get_dist(node, neighbor)))))
			dist.draw_once(world.get_world())
	for node in world.get_nodes():
		c=Circle(node.get_point(), 10)
		c.setFill("aquamarine")
		c.draw_once(world.get_world())
		text = Text(node.get_point(), node.get_name())
		text.draw_once(world.get_world())

world = World.World()
#### OPTION 1: navigation world
# create_map()
# initialize_nodes()
# world.draw_nodes()
# robot = world.add_robot(world.get_nodes()[0].get_point(), world, robot_radius)
# world.draw_objects()
# 
# while True:
# 	while True:
# 		usrinput = raw_input("Select a node to navigate to: ")
# 		found, node = find_node(usrinput)
# 		if found:
# 			goal = node
# 			break
# 		print "Invalid Node!"
# 	world.nav(robot, goal)



#### OPTION 2: navigating obstacles
def link_nodes(node):
	SW = world.get_node(Point(node.getX() - 2 * robot_radius, node.getY() + 2 * robot_radius))
	W = world.get_node(Point(node.getX() - 2 * robot_radius, node.getY()))
	NW = world.get_node(Point(node.getX() - 2 * robot_radius, node.getY() - 2 * robot_radius))
	N = world.get_node(Point(node.getX(), node.getY() - 2 * robot_radius))
	if SW is not None: world.link(SW, node)
	if W is not None: world.link(W, node)
	if NW is not None: world.link(NW, node)
	if N is not None: world.link(N, node)

def create_nodes():
	for i in range(robot_radius, world.get_world().width - robot_radius, 2*robot_radius):
		for j in range(robot_radius, world.get_world().height - robot_radius, 2*robot_radius):
			node = world.add_node(Point(i, j), "node")
			link_nodes(node)

create_nodes()
nodes = world.get_nodes()
start = nodes[0]
start.set_name("start")
goal = nodes[len(nodes) - 1]
goal.set_name("goal")

world.draw_option_2()

while True:
	p = world.get_world().getMouse()
	name = "n" + str(node_number)
	n = world.add_node(p, name)
	node_number += 1
	print "Drawing node at {0}".format(p)
	world.draw_node(n)




