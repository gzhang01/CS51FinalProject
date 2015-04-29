import World
from Graphics import *

world = World.World()

n1 = world.add_node(Point(50, 50), "n1")
n2 = world.add_node(Point(50, 225), "n2")
n3 = world.add_node(Point(200, 50), "n3")
n4 = world.add_node(Point(200, 100), "n4")
n5 = world.add_node(Point(300, 250), "n5")
n6 = world.add_node(Point(250, 400), "n6")
n7 = world.add_node(Point(175, 175), "n7")
world.link(n1, n2)
world.link(n1, n3)
world.link(n3, n4)
world.link(n2, n5)
world.link(n4, n5)
world.link(n2, n6)
world.link(n5, n6)
world.link(n1, n7)
world.link(n7, n6)

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
world.draw_nodes()
# path = world.find_path(n1, n6)
# for node in path:
# 	print node
# for node in world.get_nodes():
# 	assert node.get_parent() == None
# 	assert node.get_fscore() == 0
# 	assert node.get_gscore() == 0

robot = world.add_robot(n1.get_point(), world)
world.draw_objects()
while True:
	while True:
		usrinput = raw_input("Select a node to navigate to: ")
		if usrinput in ["n1", "n2", "n3", "n4", "n5", "n6", "n7"]:
			if usrinput == "n1": goal = n1
			if usrinput == "n2": goal = n2
			if usrinput == "n3": goal = n3
			if usrinput == "n4": goal = n4
			if usrinput == "n5": goal = n5
			if usrinput == "n6": goal = n6
			if usrinput == "n7": goal = n7
			break
	world.nav(robot, goal)






