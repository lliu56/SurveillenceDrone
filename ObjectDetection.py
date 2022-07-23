import cv2
from djitellopy import tello
import cvzone
import KeyPressModule as kp
from time import sleep

thres= 0.6   # threshold set at 60%
nmsThres = 0.2
#cap = cv2.VideoCapture(0)
#cap.set (3,640)
#cap.set (4,480)

classNames= []
classFile = ('Resources/Drone-Object-Detection/coco.names')
with open (classFile,'rt') as f:
    classNames = f.read(). split ('\n')
print (classNames)
configPath = ('Resources/Drone-Object-Detection/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt')
weightsPath = ('Resources/Drone-Object-Detection/frozen_inference_graph.pb')

#puting path into net
net = cv2.dnn_DetectionModel (weightsPath,configPath)
#setting parameters
net.setInputSize(320,320)
net.setInputScale(1.0/127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

kp.init()
me = tello.Tello()
me.connect ()
print (me.get_battery())
me.takeoff()
me.streamoff()
me.streamon ()


while True:
    #success, img = cap.read ()
    img = me.get_frame_read().frame
    classIds, confs, bbox = net.detect (img, confThreshold=thres,nmsThreshold = nmsThres)      #confThres: at what threshold you count something as an object

    try:
        for classId, conf, box  in zip (classIds.flatten(),confs.flatten (),bbox):
            cvzone.cornerRect(img,box,rt =1 )
            cv2.putText(img,f'{classNames[classId-1].upper()} {round(conf*100,2)}',
                        (box [0]+10,box[1]+30), cv2.FONT_HERSHEY_DUPLEX,1,(0,255,0),1)
    except:
        pass

    me.send_rc_control(0,0,0,0)
    cv2.imshow('Image', img)
    cv2.waitKey(1)

if kp.getKey("l"):me.land()



