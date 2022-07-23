from djitellopy import tello #importing library
from time import sleep #importing sleep fxn

me = tello.Tello ()  # creating tello object from imported files
me.connect ()
print (me.get_battery())  #fxn's in tello library
# above code nees fixing? or just connect drone properly

me.takeoff ()
# foward flight
me.send_rc_control(0,50,0,0)
sleep (2)  # delaying next cmd time AKA fly for 2 seconds
me.send_rc_control(0,-5,0,0)  # set forward velocity to -10  to brake
sleep (1)

#change yaw to right
me.send_rc_control (0,0,0,100) #over shoot
sleep (2)
#me.send_rc_control (0,0,0,-90)
#sleep (1) #correction

# foward flight
me.send_rc_control(0,50,0,0)
sleep (2)  # delaying next cmd time AKA fly for 2 seconds
me.send_rc_control(0,-2,0,0)  # set forward velocity to -10  to brake
sleep (1)

#turn right
#me.send_rc_control(30,0,0,0)
#sleep (1)
#sleep (2)  # delaying next cmd time AKA fly for 2 seconds
#me.send_rc_control(-5,0,0,0)  # brake
#sleep (1)
me.land()