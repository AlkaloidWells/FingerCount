import cv2
import time
import mediapipe as mp

#craeting a hand detector module containing all the the defined methods
class HandDetect():
    
    #constructor to handel all defined varialble
    def __init__(self, mode=False, maxHand = 2, detectionCon = 0.5, trackCon =0.5 ):
        self.mode = mode
        self.maxHand = maxHand
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHand, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        
    #so we identify a hand from the frames or image
    def FindHands(self, img, draw = True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        #we can now process the hand to identify fingers
        self.results = self.hands.process(imgRGB)
        
        #print(results.multi_hand_landmarks)
        #now we display the landmarks of the fingers as dots then linking them together
        if self.results.multi_hand_landmarks:
            for handLims in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img,handLims, self.mpHands.HAND_CONNECTIONS)
                    
        return img    #return the modification we mad on the imge with the image
    
    #now we need the landmark cordinate of the individual landmark to better reffer to it  lather
    def Findcoord(self, img, handNo = 0, draw = True ):
        
        #we now need a list to store the cordinates along side the id 
         lmList = []
         if self.results.multi_hand_landmarks:
             myhand = self.results.multi_hand_landmarks[handNo]
             for id, lm in enumerate(myhand.landmark):
                 h, w, c = img.shape
                 cx, cy = int(lm.x*w), int(lm.y*h)
                 lmList.append([id,cx,cy])
                 if id  == id:
                     cv2.circle(img, (cx,cy), 10, (0, 0, 255), cv2.FILLED)
         return lmList
        
        

    





