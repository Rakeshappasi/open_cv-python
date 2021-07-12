import cv2

cap= cv2.VideoCapture(0)

while cap.isOpened():
    sucess,frame = cap.read()
    if sucess:
        gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("grey",gray)
        cv2.imshow("Frame",frame)
    else:
        break
    if cv2.waitKey(10) & 0xff == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()