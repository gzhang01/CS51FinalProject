import World
from Graphics import *

world = World.World()
n1 = world.add_node(Point(50, 50))
n2 = world.add_node(Point(50, 225))
n3 = world.add_node(Point(200, 50))
n4 = world.add_node(Point(200, 100))
n5 = world.add_node(Point(300, 250))
world.link(n1, n2)
world.link(n1, n3)
world.link(n3, n4)
world.link(n2, n5)
world.link(n2, n4)
world.link(n4, n5)
world.draw_nodes()
while True:
	world.reset()