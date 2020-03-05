from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
print(bob)

#
for i in range(200):
    fd(bob, 2*i)
    lt(bob)


#
wait_for_user()
