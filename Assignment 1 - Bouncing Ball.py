#Assignment 1 - Bouncing Ball

from visual import *

ball = sphere(pos = (0,10,0), radius = 0.5, color = color.green)
floor = box(pos = (0,-5.0,0), size = (12, 0.2, 12), material = materials.wood)

ball.velocity = vector(0,0,0)

accelerationDueToGravity = vector(0, -9.8, 0)
timeStep = 0.0001

while(True):
    rate(5000)

    if (ball.pos.y < (floor.pos.y + 0.2)):
        ball.velocity = -ball.velocity
    
    ball.velocity = ball.velocity + accelerationDueToGravity * timeStep
    ball.pos = ball.pos + ball.velocity * timeStep

    
