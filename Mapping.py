import numpy
from djitellopy import tello
import KeyPressModule as kp
from time import sleep
import math
import numpy as np
import cv2

##### PARAMETERS #####

#fspeed = 400
#aspeed = 400
fspeed = 21400/(2*246) # @ 50 = 86.99/2 cm/sec
aspeed = 360/(4.2*2) # @ 50 angular speed; 85.71/2 degrees/sec

rspeed = 45 # rate angle change due to roll
interval = 0.25

f_interval = fspeed * interval  #forward speed per interval
a_interval = aspeed * interval  #angular speed per interval
r_interval = rspeed * interval

x_coordinate = f_interval * (math.sin(a_interval))
y_coordinate = f_interval * (math.cos(a_interval))
########################


kp.init ()
me = tello.Tello ()
me.connect ()
print (me.get_battery())
x,y  = 500,500
a = 0
yaw = 0

points = [(0,0), (0,0)]

def getKeyboardInput ():     #setting the parameters for mvmt ctrl
    lr,fb,ud,yv= 0, 0, 0, 0 # initial... will be changed with key presss
    global x,y,yaw,a,d
    d= 0
    speed =50

    if kp.getKey("d"):
        lr = speed
        d = -f_interval
        a = -180
    elif kp.getKey("a"):
        lr = -speed
        d = f_interval
        a = 180
    if kp.getKey("w"):
        fb = speed
        d = f_interval
        a =270
    elif kp.getKey("s"):
        fb = -speed
        d = -f_interval
        a =-90
    if kp.getKey("d") and kp.getKey("w"):a =-45
    elif kp.getKey("a") and kp.getKey("w"): a =225
    if kp.getKey("d") and kp.getKey("s"): a =225
    elif kp.getKey("a") and kp.getKey("s"): a = -45

    if kp.getKey("LEFT"):
        yv = -speed
        yaw -= a_interval
    elif kp.getKey("RIGHT"):
        yv = speed
        yaw += a_interval

    if kp.getKey("UP"):ud = speed
    elif kp.getKey("DOWN"): ud = -speed

    if kp.getKey("SPACE"): me.takeoff()
    if kp.getKey("l"): me.land()

    sleep (interval)
    a += yaw
    x += int (d*math.cos(math.radians(a))) ###### SOLVE THE PROBLEM OF Northwest or north east movemenets
    y += int (d*math.sin(math.radians(a)))

    return [lr,fb,ud,yv,x,y]   #returns values for each mvmnt depending on key press

def drawPoints(img, points):
    for point in points:
        cv2.circle(img,point,8,(0,0,255),cv2.FILLED)     #color is (B,G,R)
    cv2.circle(img, points[-1], 11, (0, 255, 0), cv2.FILLED)
    cv2.putText(img,f'({(points[-1][0]-500)/100},{(points[-1][1]-500)/100})',
                (points [-1][0]+10,points [-1][1]+30),cv2.FONT_HERSHEY_PLAIN,1,(255,0,255),1)
while True:         #use while loop so keep keeps running and not just once
    vals = getKeyboardInput()
    me.send_rc_control(vals[0],vals[1],vals[2],vals[3])     #indexing value

    #Mapping: images are matrix of numbers-
    #step 1: create a matrix of all 0s
    #step2 : draw points
    img = np.zeros((1000,1000,3),np.uint8)    #3 is the color channels BGR
                                              # uint8 is unassignt integer of 8 bits
                                              # 8 bits = 2^8 = 256 = values (0 to 255)
    if (points[-1][0] !=vals [4] or points [-1][1] != vals [5]):
        points.append((vals[4],vals[5]))
    drawPoints(img, points)
    cv2.imshow('Output', img)
    cv2.waitKey(1)

