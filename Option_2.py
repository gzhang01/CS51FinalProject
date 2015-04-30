from Graphics import *

def option_2(world, robot_radius):
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
		for i in range(2*robot_radius, world.get_world().width - robot_radius, 2*robot_radius):
			for j in range(2*robot_radius, world.get_world().height - robot_radius, 2*robot_radius):
				node = world.add_node(Point(i, j), "node")
				link_nodes(node)

	def draw_buttons():
		# draw "start button" for user to click once they're done adding obstacles
		button = Rectangle(Point(5, 450), Point(100, 500))
		button.setFill("aquamarine")
		button.draw_once(world.get_world())
		words1 = Text(Point(50, 465), "Click to begin")
		words2 = Text(Point(50, 485), "Navigation")
		words1.draw_once(world.get_world())
		words2.draw_once(world.get_world())

		# draw a reset button so they can start the obstacle course from scratch
		reset = Rectangle(Point(400, 0), Point(495, 50))
		reset.setFill("aquamarine")
		reset.draw_once(world.get_world())
		words = Text(Point(450, 25), "Reset")
		words.draw_once(world.get_world())

		return button, reset

	create_nodes()
	nodes = world.get_nodes()
	start = nodes[0]
	start.set_name("start")
	goal = nodes[len(nodes) - 1]
	goal.set_name("goal")
	robot = world.add_robot(start.get_point(), world, robot_radius)

	world.draw_option_2()
	world.draw_objects()
	button, reset = draw_buttons()

	print "Robot will attempt to navigate to red dot"
	print "Click anywhere to place an obstacle"
	print "Click lower left button to begin navigation"
	print "Click reset button to clear all obstacles and move robot to start location"

	# get coordinates of where user has clicked and check if they've hit start button
	while True:
		p = world.get_world().getMouse()
		# if they clicked the start button
		if (button.getP1().getX()<=p.getX()<=button.getP2().getX() and button.getP1().getY()<=p.getY()<=button.getP2().getY()):
			world.nav(robot, goal, False)

		# if they clicked the reset button
		elif (reset.getP1().getX()<=p.getX()<=reset.getP2().getX() and reset.getP1().getY()<=p.getY()<=reset.getP2().getY()): 
			world.get_world().remove_all()
			world.get_world().delItem(robot)
			white = Rectangle(Point(0,0), Point(600,600))
			white.setFill("white")
			white.draw_once(world.get_world())
			world.remove_nodes_inside(Point(0,0), Point(500,500), 2*robot_radius)	
			option_2(world, robot_radius)

		# if they didn't click either button and they're just trying to add an obstacle
		else:
			obst = Rectangle(Point(p.getX()-robot_radius, p.getY()-robot_radius), Point(p.getX()+robot_radius, p.getY()+robot_radius))
			obst.setFill("black")
			obst.draw_once(world.get_world())
			# remove the nodes that are inside the new obstacle 
			world.remove_nodes_inside(Point(obst.getP1().getX()-robot_radius, obst.getP1().getY()-robot_radius), Point(obst.getP2().getX()+robot_radius, obst.getP2().getY()+robot_radius), 2*robot_radius)