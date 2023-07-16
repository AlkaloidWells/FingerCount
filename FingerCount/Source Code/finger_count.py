"__________________alkaoid_________________project________"
import cv2
import time
import os
import handcrack as hm

#this are to handel the fram time to display the the hand gesture
pTime, cTime = 0,0
#this are to handel the fram hight and with
wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4,hCam)

#we now handel the set up of the hand gesture 
folderpath = "img"
mylist = os.listdir(folderpath) #a list to handel the verious images withe the help of the os
print(mylist)
overlayl = []

#we use this to append images to the the new list after detection 
for impath in mylist:
    image = cv2.imread(f'{folderpath}/{impath}')
    overlayl.append(image)

#so we do create an object for bthe class
detector = hm.HandDetect(detectionCon=0.75)

#so now we can create a list contaning all the landmark cordinate nmber we may want to track their movement
tipIds = [4, 8, 12, 16, 20]

#we now handle realtime video processing
while True:
    
    success, img = cap.read()
    
    #we now use a method of the class to find or detect the presence of a hand on each fram
    img = detector.FindHands(img)
    
    #we collect the coordinate of the of each of the land marks
    lmlist = detector.Findcoord(img, draw= False)
    #print(lmlist)
    finger = []
    
    #making sure the is actulay a hand detected befor we we perfrom any display any landmark
    if len(lmlist) != 0:
       
        #we track the tump finger to know  if its up by compairing with the palm index #this are to 
        #handel the fram hight and with
        if lmlist[tipIds[0]][1] > lmlist[tipIds[0]-1][1]:
            finger.append(1)
        else:
            finger.append(0)
        
        #to check the rest of the the finger if the up or not and keep a not by appending one or zero
        #also this is wedin the range of the the five fingers
        for id in range(1,5):
            if lmlist[tipIds[id]][2] < lmlist[tipIds[id]-1][2]:
                finger.append(1)
            else:
                finger.append(0)

        print(finger)  
        #taking not of the number of fin gers up to know the total number of fingers up
        totalf = finger.count(1)
        #print(totalf)
           
        #now to append the the figure number image to the image 
        #and nulify the image size  diffrence by useing the shape meththod
        h, w, c = overlayl[totalf-1].shape
        img[0:h, 0:w] = overlayl[totalf-1]
        
        #the cv2 mthode below will alow us the crate a rectangel for which we shal display the coresponding 
        #number in corollation to the hand gesture 
        cv2.rectangle(img, (20,255), (170, 425), (255, 0, 0), cv2.FILLED)
        cv2.putText(img, str(int(totalf)), (45,375),cv2.FONT_HERSHEY_PLAIN,  10, (0, 255, 0), 25)
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (400,70),cv2.FONT_HERSHEY_PLAIN,  3, (255, 0, 0), 3)
    cv2.imshow('Alkaloid', img)
    k = cv2.waitKey(30) 
    if k==27:
        break
cap.release()
cv2.destroyAllWindows()