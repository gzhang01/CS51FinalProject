import World
from Option_1 import option_1
from Option_2 import option_2
from Option_3 import option_3

robot_radius = 20

world = World.World()

print "Would you like to: "
print "1. Navigate a robot along roads"
print "2. Place obstacles for a robot to navigate around"
print "3. Create a random set of nodes for robot to navigate"
choice = raw_input("Selection: ")

if choice == "1":
	option_1(world, robot_radius)
elif choice == "2":
	option_2(world, robot_radius)
elif choice == "3":
	option_3(world, robot_radius)
else: print "Invalid selection!"