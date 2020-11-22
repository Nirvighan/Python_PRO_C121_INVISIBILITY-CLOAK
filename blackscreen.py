## IMPORT THE MODULES
import cv2
import numpy as np
import time

## START THE CAMERA

# PREPARATION FOR WRITING THE OUTPUT VIDEO

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

# START READING THE VIDEO FROM WEBCAM

cap = cv2.VideoCapture(0)

count = 0
background = 0

# CAPTURE THE BACKGROUND IN RANGE OF 60

for i in range(60):
    ret,background = cap.read()

# FLIP THE BACKGROUND

background = np.flip(background,axis = 1)

# READ EVERY FRAME FROM THE WEBCAM UNTIL IT IS ON

while(cap.isOpened()):
    ret,img = cap.read()
    if not ret:
        break 

    count+=1
    img = np.flip(img,axis = 1)

    # RESIZE THE IMAGE AND THE FRAMES

    img = cv2.resize(img,(640,480))
    count = cv2.resize(count,(640,480))

    # CONVERT THE COLORS SPACE FROM GBR TO HSV
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    # CREATE ARRAY OF RGB's FAINT BLACK AND DARK BLACK COLOR

    l_black = np.array([30,30,0])
    d_black = np.array([104,153,70])

    # CREATE THE MASK FOR BLACK COLOR AREA

    mask = cv2.inRange(hsv,l_black,d_black)
    result = cv2.bitwise_and(count,count,mask = mask)

    

    # CREATE THE INVERTED MASK TO SEGMENT OUT THE BLACK COLOR FROM THE FRAME

    mask2 = cv2.bitwise_not(mask)
    image = cv2.bitwise_and(img,img,mask = mask2)

    # CREATE IMAGE SHOWING STATIC BACKGROUNDFRAME PIXELS ONLY FOR THE MASK REGION

    image2 = cv2.bitwise_and(background,background,mask = mask)

    

    # GENERATE THE FINAL OUTPUT

    final_res = cv2.addWeighted(image,1,image2,1,0)
    out.write(final_res)
    cv2.imshow("MAGIC",final_res)
    cv2.waitKey(1)

    
# CLOSE THE WEBCAM
# YOU CAN USE KILL TERMINAL OPTION TO CLOSE IT WHEN YOU ARE RUNNING THE PROJECT IN VS CODE
cap.release()
out.release()

cv2.destroyAllWindows()
    
    


