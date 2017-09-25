from visual import *
import random

deltat = 0.005  #Delta Time
t = 0           #Start Time

#Setup base objects
xBall = sphere(pos=(-5,0,0), radius=0.5, color=color.white)
yBall = sphere(pos=(0,-5,0), radius=0.5, color=color.white)
zBall = sphere(pos=(0,0,5), radius=0.5, color=color.white)
balls = [xBall, yBall, zBall]

for ball in balls:
    #ball.trail = curve(color=ball.color)
    ball.velocity = vector(random.randint(1,25), random.randint(1,25), random.randint(1,25))
    

wallR = box(pos=(6,0,0), size=(0.2,12,12), color=color.green)
wallL = box(pos=(-6,0,0), size=(0.2,12,12), color=color.green)
wallTop = box(pos=(0,6,0), size=(12,.2,12), color=color.blue)
wallBot = box(pos=(0,-6,0), size=(12,.2,12), color=color.blue)
wallBack = box(pos=(0,0,-6), size=(12,12,.2), color=color.red)
wallFront = box(pos=(0,0,6), size=(12,12,.2), opacity=0)

#Setup base rates and positions
for ball in balls:
    ball.pos = ball.pos + ball.velocity*deltat

#Aesthetic objects
vscale = 0.1
#varr = arrow(pos=xBall.pos, axis=vscale*xBall.velocity, color=color.cyan)
#ball.trail = curve(color=ball.color)

#Loop and Scene Properties
scene.autoscale = False

ChangeColor = 0

while true:
    rate(100)
    for ball in balls:
        ChangeColor += 1
        if ChangeColor == 20:
            ball.color = (random.randint(0,1), random.randint(0,1), random.randint(0,1))
            ChangeColor = 0

        #X axis - wallR and wallL
        if ball.pos.x >= wallR.pos.x or ball.pos.x <= wallL.pos.x:
            ball.velocity.x = ball.velocity.x * -1
            #varr.axis=vscale*ball.velocity

        #Y axis - wallTop and wallBot
        if ball.pos.y >= wallTop.pos.y or ball.pos.y <= wallBot.pos.y:
            ball.velocity.y = ball.velocity.y * -1
            #varr.axis=vscale*ball.velocity

        #Z axis - wallBack and wallFront
        if ball.pos.z >= wallFront.pos.z or ball.pos.z <= wallBack.pos.z:
            ball.velocity.z = ball.velocity.z * -1
            #varr.axis=vscale*ball.velocity
            
        
        ball.pos = ball.pos + ball.velocity * deltat
        #varr.pos = ball.pos
        #ball.trail.append(pos=ball.pos)
    t += deltat

    
