
import cv2
# import keyboard
import mediapipe
# import time
import pyautogui
import autopy
import numpy



# window_handle=FindWindow(None,'D')
cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,2020)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1050)
initHand = mediapipe.solutions.hands

mainHand = initHand.Hands(min_detection_confidence=0.9, min_tracking_confidence=0.7)
draw = mediapipe.solutions.drawing_utils
# wScr, hScr = autopy.screen.size()
pX, pY = 0, 0
cX, cY = 0, 0


def handLandmarks(colorImg):
    landmarkList = []

    landmarkPositions = mainHand.process(colorImg)
    landmarkCheck = landmarkPositions.multi_hand_landmarks
    if landmarkCheck:
        for hand in landmarkCheck:
            for index, landmark in enumerate(hand.landmark):
                draw.draw_landmarks(img, hand, initHand.HAND_CONNECTIONS)
                h, w, c = img.shape
                centerX, centerY = int(landmark.x * w), int(landmark.y * h)
                landmarkList.append([index, centerX, centerY])
                
    return landmarkList


def fingers(landmarks):
    fingerTips = []
    tipIds = [4, 8, 12, 16, 20]
    
    # Check if thumb is up
    if landmarks[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
        fingerTips.append(1)
    else:
        fingerTips.append(0)
    
    # Check if fingers are up except the thumb
    for id in range(1, 5):
        if landmarks[tipIds[id]][2] < landmarks[tipIds[id] - 3][2]:
            fingerTips.append(1)
        else:
            fingerTips.append(0)

    return fingerTips


while True:
    check, img = cap.read()  # Reads frames from the camera
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Changes the format of the frames from BGR to RGB
    lmList = handLandmarks(imgRGB)


    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]  # Gets index 8s x and y values (skips index value because it starts from 1)
        x2, y2 = lmList[12][1:]  # Gets index 12s x and y values (skips index value because it starts from 1)
        finger = fingers(lmList)  # Calling the fingers function to check which fingers are up
        print(finger)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
   
# Destroy all the windows
cv2.destroyAllWindows()

# import pyautogui
# import keyboard
# while True:
#     print(pyautogui.position())
#     if keyboard.is_pressed('q'):
#         break
