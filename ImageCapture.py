from djitellopy import tello
import cv2
me = tello.Tello ()
me.connect ()
print (me.get_battery())

me.streamon() #turn on video stream frame by frame

while True:
    img = me.get_frame_read().frame  #me.get_frame_read() get the object from drone
                                     # me.get_frame_read().frame gets the actual frames
    img = cv2.resize (img,(360,240)) # resize so it processes faster
    cv2.imshow ("Image", img)        # create window to display frames
    cv2.waitKey (1)                  #giving frames a 1ms delay before it shuts off


