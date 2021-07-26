# Created by kor_a at 26/07/2021
from cvzone.HandTrackingModule import HandDetector
import cv2
from pyfirmata import Arduino, util

#Choose Serial Port
board = Arduino('COM11')

iter8 = util.Iterator(board)
iter8.start()

#Choose pin that you attach servo cable
pin9 = board.get_pin('d:9:s')

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.5, maxHands=2)

#move function
def move_servo(a):
    pin9.write(a)


while True:
    # Get image frame
    success, img = cap.read()

    # Find the hand and its landmarks
    img = detector.findHands(img)
    lmList, bboxInfo = detector.findPosition(img)
    if lmList:
        bbox = bboxInfo['bbox']

        # Find Distance Between Two Fingers
        distance, img, info = detector.findDistance(4, 8, img) #You can choose which finger points to find distance
        cv2.putText(img, f'Dist:{int(distance)}', (bbox[0] + 400, bbox[1] - 30),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
        move_servo(int(distance)) #Move Servo

    # Display
    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()