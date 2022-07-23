from djitellopy import tello
import KeyPressModule as kp
from time import sleep

kp.init ()
me = tello.Tello ()
me.connect ()
print (me.get_battery())


def getKeyboardInput ():     #setting the parameters for mvmt ctrl

    lr,fb,ud,yv= 0, 0, 0, 0 # initial... will be changed with key press
    speed = 100

    if kp.getKey("d"): lr = speed
    elif kp.getKey("a"): lr = -speed

    if kp.getKey("UP"): ud =  speed
    elif kp.getKey("DOWN"): ud = -speed

    if kp.getKey("w"): fb =  speed
    elif kp.getKey("s"): fb = -speed

    if kp.getKey("LEFT"): yv =  -speed
    elif kp.getKey("RIGHT"): yv = speed

    if kp.getKey("SPACE"): me.takeoff()
    if kp.getKey("l"):me.land()

    return [lr,fb,ud,yv]   #returns values for each mvmnt depending on key press

while True:         #use while loop so keep keeps running and not just once
    vals = getKeyboardInput()
    me.send_rc_control(vals[0],vals[1],vals[2],vals[3])     #indexing value
    sleep (0.05)    #make sure it's stable

#if dictionaryname['Index_Up']: print('something')
