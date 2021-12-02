import cv2
from random import randrange
#haarcascadealgo

trained_face_data = cv2.CascadeClassifier(r"C:\\Users\\Charles\\Documents\\GitHub\\opencv\\data\\haarcascades\\haarcascade_frontalface_default.xml")
#rob = r"C:\Users\Charles\Desktop\PHP\imageprojects\rob.png"
#img = cv2.cvtColor(cv2.imread(rob), cv2.COLOR_BGR2GRAY)
#0 for default, quotes to specify another file path. 
#remember cv2 color conversion function
#face_coordinates = trained_face_data.detectMultiScale(img)
#parameters here are coordinates from scale detection
#for (x, y, w, h) in face_coordinates:
#    cv2.rectangle(img, (x, y), (x+w, y+h), (randrange(255), randrange(255), randrange(255)), 2)
    
#cv2.imshow('check this photo out', img)
##cv2.waitKey(0)
#print("i ran", face_coordinates)

webcam = cv2.VideoCapture(0)

while True: 
    successful_frame_read, frame = webcam.read()
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (randrange(255), randrange(255), randrange(255)), 2)
    
    cv2.imshow('hello', frame)
    cv2.waitKey(1)