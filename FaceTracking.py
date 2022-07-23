import cv2
import numpy as np
from djitellopy import tello
import time

me = tello.Tello ()
me.connect ()
print (me.get_battery())

me.streamon()
me.takeoff()
#me.send_rc_control (0,0,10,0)
#time.sleep (0.5)

w,h = 360,240
fbRange = [6000,9000] #max and min area range before drone has to move
pid = [0.4,0.4,0]
pError =0

#Track/detect face
def findFace (img):
    faceCascade = cv2.CascadeClassifier (cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    imGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imGray, 1.2, 4)

    myFaceListC = []
    myFacelistArea = []


    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cx = x + w//2
        cy = y + h//2
        area = w*h
        myFaceListC.append ([cx,cy])
        myFacelistArea.append(area)
        cv2.circle (img,(cx,cy),5,(255,0,0),cv2.FILLED)

    if len (myFacelistArea) != 0:
        i = myFacelistArea.index (max(myFacelistArea))  #finding index of the max value (look for the closest face)
        return img, [myFaceListC[i],myFacelistArea[i]]
    else:
        return img, [[0,0],0]

#drone face tracking
def trackFace (info, w, pid, pError):
    area = info [1]
    x,y = info [0]
    fb = 0
# how far away is the object from the center aka error
    error = x - w/2
# changing sensitivity of error with pid
    speed = pid[0]* error + pid [1] * (error- pError)
    speed = int (np.clip(speed ,-100,100))

    if area >fbRange[0] and area < fbRange[1]: fb= 0
    elif area > fbRange [1]:fb =- 20
    elif area < fbRange[0] and area !=0: fb = 20

    if x == 0:
        speed = 0
        error = 0

    #print(speed, fb)


    me.send_rc_control (0,fb,0,speed)
    return error


#standard code for opencv to run a webcam
#cap = cv2.VideoCapture(0)
while True:
    #_, img = cap.read()
    img = me.get_frame_read().frame
    img = cv2.resize(img, (w,h))
    img, info = findFace(img)
    pError = trackFace( info, w, pid, pError)
   # print ('Center',info[0],'Area', info[1])
    cv2.imshow ('Output',img)
    if cv2.waitKey(1) and 0xFF == ord('l'):
        me.land()
        break
