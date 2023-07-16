# FingerCount
implimentation real time figer count system using openCv an ML project

![image](https://github.com/AlkaloidWells/FingerCount/assets/55930366/07155ddf-f58e-434d-be43-615c52104897)


  # INCHNTEC TECH-CAM  REPORT 2020-2021
BY
ENMBE VERINE ICHUMBEI
                                                                        06-10-2021

INTRUDUCTION
The year was an exciting one as i had mainly two objectives as model 1 of the techcam  offered by inchtec . AI and Data Analysis both interesting sections  the program was scheduled for two weeks  in which were to be in attendance twice each week  Tuesdays and Thursdays  8am to 12am. The program was distributed among three instructors. Data analysis. bellow we shall look at content of work

 CONTENT OF WORK
Our content was not so tight but essential  cause i would say the content gave me a lot of grounds to be able to take on bigger projects. to the best of my knowledge our instructors try to make us see in each of our lesson the relationship between the working concept and it real life applications in solving problems. After a briefer introduction of the history of Ai and data analysis we went on to the work proper


	AI
•	Opencv
An intoduction to opencv as one of best libraries fo vision(detection, recondition and tracking)
only draw backs is it use cascade which is found of false negative(picking up unneeded background object ) but never the less it quit fast

•	Image reading with opencv and python
Our case study was phase detection.
Here we were to see we could use opencv to get and imge from the computer (read) we could also do the same for a video in the computer using the VideoCapture("Video.mp4") 
face detection on an image :                                  face detection on a video:

![image](https://github.com/AlkaloidWells/FingerCount/assets/55930366/e2830946-8037-4546-b37f-cfda3f864366)


•	Real life image capture with opencv and python
here we made use of accessing an image through our webcam  to identify a phase by analyzing the different farms so the phase detection was don using a webcam 
Face detection real time:

![image](https://github.com/AlkaloidWells/FingerCount/assets/55930366/5bd5d288-2859-4c53-beb4-7ccf86118e79)


•	IPwebcam with opencv and python 
The challenge here was to capture an image detect a phace and save the image maybe  this was done by routing the  signal though a link pick up by the  VideoCapture("link") also with ip webcam in the mobile phone device



	Project
This is practically my best part
design a program to detect a hand, detect the number of fingers up, and display on the screen the number to do so .
Well the project  was cool 

Challenges:
my main goal was how i would tell the computer  that when my one finger was up it means  one so i made some research  and found out opencv  had a function and an assistant library for that "mediapipe"  i mean that was actual the solution.

Plane:
•	Create a module called handcrack.py it had thre main methods 
1.	A constructor to handle all the constants
2.	HandFinder to detect the presence of a hand perform processing to identify the fingers
3.	Findcoord.To draw up a hand done by processing we need land mark but only the processing function had that but i need to tell if a finger is up by comparing it the other so that is why we needed to know the coordinate position  of each land mark at any time this coordinate are to be stored in a list for later use


•	Create the main file called finger_count.py to handell all operation of our  program with the help of our handcrack.py imported.

![image](https://github.com/AlkaloidWells/FingerCount/assets/55930366/4f4f5333-6f95-4ed7-8421-deb818533cf4)

Conclusions
In all i would say we accomplish a grate task and dou they fully meet my expectation the sure did offer me a lotto that i say thank you  

