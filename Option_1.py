from Graphics import *

def create_map(world):
	n1= world.add_node(Point(100,50), "1")
	n2 = world.add_node(Point(200,25), "2")
	n3 = world.add_node(Point(200,115), "3")
	n4 = world.add_node(Point(300,50), "4")
	n5 = world.add_node(Point(400,50), "5")
	n6 = world.add_node(Point(400,115), "6")
	n7 = world.add_node(Point(450,400), "7")
	n8 = world.add_node(Point(375,385), "8")
	n9 = world.add_node(Point(375,450), "9")
	n10 = world.add_node(Point(300,350), "10")
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

	park = Rectangle(Point(150, 150), Point(350, 300))
	park.setFill("green")
	park.draw_once(world.get_world())
	lake = Oval(Point(175, 175), Point(325, 275))
	lake.setFill("blue")
	lake.draw_once(world.get_world())
	world.draw_nodes()

def option_1(world, robot_radius):
	create_map(world)
	robot = world.add_robot(world.get_nodes()[0].get_point(), world, robot_radius)
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