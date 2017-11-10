#!/usr/bin/python
# drivenpend.py
# Physics 338:  The Damped Driven Pendulum.
# Integrate Newton's laws for the damped, driven pendulum and illustrate
# the results with a simulation and a phase space plot.
# This version includes sliders for controlling the various parameters
# $Id: drivenpend.py,v 1.8 2003/11/26 15:51:36 doughera Exp $
#	-- Andrew Dougherty

from visual.graph import *
from visual.controls import *

#####################################################################
# DISPLAY SETTINGS:
# Set fancy_display to '0' to show only the phase space window.  This
# runs faster, but you have to manually stop, edit, and restart the
# program to change the constants.  Set it to '1' to show everything.
fancy_display = 1

# Another way to speed up or slow things down is with the rate()
# command in the main loop near the bottom.

# Set these to the Horizontal and vertical resolution of your screen.
hres = 1024
vres = 768
#####################################################################

# Physical Constants, but in convenient computational form
omega0 = 1.0		# Natural angular frequency of undamped oscillator
Q      = 2.0
a0     = 1.4		# Convenient shorthand for external forcing F0/m
omega  = 0.67 * omega0 	# Driving frequency

# Derived physical constants
T0 = 2 * pi / omega0	# Natural period of undamped oscillator
gamma =  omega0 / Q	# Damping coefficient
T_driving = 2 * pi / omega  # Period of the external forcing.
# Initial conditions
t = 0.0
x = 0.0
v = 0.0

# Time step.  Adjust as needed to achieve the desired precision
# and smoothness of plot.
dt = 0.01 #  smaller than about T0/200, but rounded for nice display.
T_transient = 0 # 10.0 * Q * T0     # Adjust this to skip plotting
				    # initial transient.
T_stop = T_transient + 5000 * T0
ntrail = 4000  # Length of trail of 'dots' to leave behind.
npoincare = 40

# Acceleration function.
def accel(x, v, t):
    "accel(x,v,t): acceleration for the damped driven pendulum."
    a = -omega0**2 * sin(x) - gamma * v + a0 * cos(omega * t)
    return a

# 4th Order Runge-Kutta
def rk4(x, v, t, dt):
    "rk4(x,v,t,dt): Advance one time step using 4th-order Runge Kutta."
    xk1 = dt * v
    vk1 = dt * accel(x, v, t)
    xk2 = dt * (v + vk1/2.0)
    vk2 = dt * accel(x + xk1/2.0, v + vk1/2.0, t + dt/2)
    xk3 = dt * (v + vk2/2.0)
    vk3 = dt * accel(x + xk2/2.0, v + vk2/2.0, t + dt/2)
    xk4 = dt * (v + vk3)
    vk4 = dt * accel(x + xk3, v + vk3, t + dt)
    xnew = x + (xk1 + 2.0 * xk2 + 2.0 * xk3 + xk4) / 6.0
    vnew = v + (vk1 + 2.0 * vk2 + 2.0 * vk3 + vk4) / 6.0
    return [xnew, vnew]

# Call-back routines -- these are called when the various buttons in
# the control window are pressed.

def sets_step(ss):
    s_stepbox.text = 'step size: %f' % ss.value

def increments_step(ss, amt):
    ss.value = ss.value * amt
    sets_step(ss)

def setdrivingforce(sf):
    global a0
    a0 = sf.value
    a0box.text = 'a0: %f' % a0

def incrementdrivingforce(sf, fstep):
    sf.value = sf.value + fstep
    setdrivingforce(sf)

def setdrivingfrequency(sw):
    global omega
    global T_driving
    omega = sw.value
    T_driving = 2 * pi / omega
    omegabox.text = 'omega: %f' % omega

def incrementdrivingfrequency(sw, fstep):
    sw.value = sw.value + fstep
    setdrivingfrequency(sw)

def cleartrail():
    for n in arange(ntrail):
        myplot.dots[n].pos[0] = 0
        myplot.dots[n].pos[1] = 0
    for n in arange(npoincare):
        poincare.dots[n].pos[0] = 0
        poincare.dots[n].pos[1] = 0

def finishup():
    global t
    t = T_stop

#################################
# Set up for the various windows.
#################################
###########
# First, the pendulum visualization:
###########
if fancy_display == 1:
    window1 = display(title='Chaotic Pendulum',
			width= vres/2, height=vres/2, x=0, y=0)
    pivot = sphere(display=window1, pos=(0,0,0), radius = 0.01,
			color=color.yellow)
    # Here's the pendulum.
    bob = sphere(display=window1, radius = 0.05, pos=(0,-1,0),
			color = color.red)
    pendulum = cylinder(display=window1, pos=(0,0,0), axis=bob.pos,
			radius=0.005, color=color.cyan)
    # Make a small dot to show the forcing
    driver = sphere(display=window1, radius = 0.02, pos=(0,-1,0),
			color = color.yellow)
    print 'The yellow dot indicates the forcing.'
    # Finally, an invisible box just to keep Visual from autoscaling
    # unintelligently
    box(display=window1, pos=(0,0,0), length=2.2, width=0, height=2.2,
			color=color.black)

###########
# Second, the phase space plot:
###########
window2 = gdisplay(title="Phase Space Plot", xtitle='position',
                   ytitle='velocity',width= hres/2, height= vres/2,
                   x=0, y=vres/2,
                   xmin = -3.2, xmax = 3.2, ymin = -3.2, ymax = 3.2)
myplot = gdots(display=window2, color=color.cyan)
if fancy_display == 1:
    window3 = gdisplay(title="Poincare Section", xtitle='position',
                   ytitle='velocity',width=hres/2, height=vres/2,
                   x = hres/2, y = vres/2,
                   xmin = -3.2, xmax = 3.2, ymin = -3.2, ymax = 3.2)
    poincare = gdots(display=window3, color=color.cyan)

# Put a time ticker in the upper-right-hand corner of the graph.
clk = label(pos=(3,2), text='0', display=window2.display)

# Generate an initial plot (This allocates all the points for the plot
# correctly.  We'll later just reuse these same points over and over again.)
print "Initializing plot ... "
for n in arange(ntrail):
    myplot.plot(pos=(x, v))

if fancy_display == 1:
    for n in arange(npoincare):
        poincare.plot(pos=(x,v))

print "Done."

##########
# Lastly, the control window.  (Coordinates in this window go from
# (-100,-100) to (100,100)
##########
if fancy_display == 1:
    ctrl = controls(title="Pendulum Controls", width=vres/2, height = vres/2,
		     x = hres/2, y = 0)

    # Each click on the slider increments the variable by ss.value.
    # Step size slider
    yctl = -10  # y-coordinate of control slider
    ss = slider(min = 0, max = 1, pos=(-50, yctl), length = 100,
		axis=(1,0,0), action=lambda: sets_step(ss))
    # ... and up and down buttons
    bssup = button(pos=(60, yctl), text = '>', width = 10, height = 10,
		    action = lambda: increments_step(ss, 10))
    bssdown = button(pos=(-60, yctl), text = '<', width = 10, height = 10,
		    action = lambda: increments_step(ss, 0.10))
    s_stepbox = label(pos=(0, yctl+15), text = 'step size',
		    display=ctrl.display)
    ss.value = 0.01

    # Driving force slider
    yctl = 30
    sf = slider(min = 0, max = 5, pos=(-50, yctl), length = 100,
		axis=(1,0,0), action=lambda: setdrivingforce(sf))
    # ... and up and down buttons
    bsfup = button(pos=(60, yctl), text = '>', width = 10, height = 10,
		    action = lambda: incrementdrivingforce(sf, ss.value))
    bsfdown = button(pos=(-60, yctl), text = '<', width = 10, height = 10,
		    action = lambda: incrementdrivingforce(sf, -ss.value))
    a0box = label(pos=(0, yctl+15), text = 'a0', display=ctrl.display)
    sf.value = a0

    # Driving frequency slider
    yctl = 70
    sw = slider(min = 0, max = 5, pos=(-50, yctl), length = 100,
		    axis=(1,0,0), action=lambda: setdrivingfrequency(sw))
    # ... and up and down buttons
    bswup = button(pos=(60, yctl), text = '>', width = 10, height = 10,
                action = lambda: incrementdrivingfrequency(sw, ss.value))
    bswdown = button(pos=(-60, yctl), text = '<', width = 10, height = 10,
                action = lambda: incrementdrivingfrequency(sw, -ss.value))
    omegabox = label(pos=(0, yctl+15), text = 'omega', display=ctrl.display)
    sw.value = omega

    # Clear existing phase space "trail"
    bct = button(pos=(-70, -70), text='Clear', action=lambda: cleartrail())

    # STOP button.
    bstop = button(pos=(70, -70), text = 'Stop', action=lambda: finishup())

#### End of control window

######################
# Calculations
######################

# Skip initial transient
while t < T_transient:
    [x, v] = rk4(x, v, t, dt)
    if x < (-pi):
        x = x + 2.0 * pi
    if x > (pi):
        x = x - 2.0 * pi
    clk.text = '%7.2f' % t      # Update the clock.
    t = t + dt

# Integrate forward.
n = 0   # Counts which of our 'ntrail' dots to use for the plot
np = 0
while t < T_stop:
    # Comment out or adjust the next line if things are running too slowly.
    rate(1000)
    if fancy_display == 1:
	ctrl.interact()   # Check if any controls have been pressed.
    [x, v] = rk4(x, v, t, dt)
    if x < (-pi):
        x = x + 2.0 * pi
    if x > (pi):
        x = x - 2.0 * pi
    if fancy_display == 1:
	# Pendulum picture.
	bob.pos = (sin(x), -cos(x), 0)
	pendulum.axis = bob.pos
	# Position of indicator of driving force.  Make it at an
	# angle theta_driver
	theta_driver = a0 * cos(omega * t)
	driver.pos = (sin(theta_driver), -cos(theta_driver), 0)
	#
	# Plot a point for the Poincare section once per driving period.
	if (t % T_driving) < 0.01:
	    if np % npoincare == 0:
		np = 0
	    poincare.dots[np].pos[0] = x
	    poincare.dots[np].pos[1] = v
	    np = np + 1

    # Phase space plot
    if n % ntrail == 0:
        n = 0
    myplot.dots[n].pos[0] = x
    myplot.dots[n].pos[1] = v
    n = n + 1

    clk.text = '%7.2f' % t      # Update the clock.
    t = t + dt			# Advance to the next time step.

print "Done."

#
# $Log: drivenpend.py,v $
# Revision 1.8  2003/11/26 15:51:36  doughera
# Don't make the Poincare section plot window unless fancy_display == 1.
#
# Revision 1.7  2003/11/17 16:39:05  doughera
# Changed Poincare section color to cyan -- white was getting lost
# on the graph axes.
#
# Revision 1.6  2003/11/17 13:58:26  doughera
# Added Poincare section plot.
# Made window positioning contingent upon resolution of screen
# (but you must set hres and vres manually).
#
# Revision 1.5  2003/11/14 14:08:18  doughera
# Add small yellow dot to show amplitude and phase of forcing.
#
# Revision 1.4  2003/11/13 16:51:09  doughera
# Fixed initial constants to reasonable values for this assignment.
# Added additional comments.
# Set rate initially at a value suitable for interpreting the graphs.
# Users will want to speed things up after a while.
#
# Revision 1.3  2003/11/13 14:50:35  doughera
# Make fancy display optional.
# Improve comments.
#
# Revision 1.2  2003/11/13 14:15:24  doughera
# Cleaned up ; rearranged controls.
#
# Revision 1.1  2003/11/12 18:32:19  doughera
# Initial revision
#
#
