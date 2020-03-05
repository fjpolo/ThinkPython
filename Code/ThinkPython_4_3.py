from swampy.TurtleWorld import *
import math

"""
world = TurtleWorld()
bob = Turtle()
print(bob)

#
for i in range(200):
    fd(bob, 2*i)
    lt(bob)


#
wait_for_user()
"""

#
# square
#
def square(t, length):
    for i in range(4):
        fd(bob, length)
        lt(bob)

#
# polyline
#
"""Draws n line segments with the given length and
angle (in degrees) between them. t is a turtle.
"""
def polyline(t, n, length, angle):
    for i in range(n):
        fd(t, length)
        lt(t, angle)


#
# polygon
#
"""Draws a n sided polygon with the given length.
t is a turtle.
"""
def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

#
# circle
#
"""Draws a circle with radius r. t is a turtle."""
def circle(t, r):
    arc(t, r, 360)

#
# arc
#
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)


#
# Main
#
if __name__ == '__main__':

    world = TurtleWorld()
    bob = Turtle()
    bob.delay = 0.01
    #square(bob, 25)
    #polygon(bob, 15, 100)
    circle(bob, 50)
    #arc(bob, 50, 180)
