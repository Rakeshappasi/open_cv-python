
import cv2
cap = cv2.VideoCapture(0)
img = cv2.imread('1.png')
img_1= cv2.imread('2.png')
img_2= cv2.imread('3.png')
img_3= cv2.imread('4.png')
img_4= cv2.imread('5.png')
img_5= cv2.imread('6.png')
choice= int(input("any number under 6:"))
while cap.isOpened():
    flag, frame = cap.read()
    if flag:
        if choice == 1:
            image = cv2.resize(img, (frame.shape[1], frame.shape[0]))
            result = cv2.addWeighted(frame, 1, image, 0.3, gamma=1)
            cv2.imshow('blend1', result)
        elif choice == 2:
            image = cv2.resize(img_1, (frame.shape[1], frame.shape[0]))
            result = cv2.addWeighted(frame, 1, image, 0.3, gamma=1)
            cv2.imshow('blend2', result)
        elif choice == 3:
            image = cv2.resize(img_2, (frame.shape[1], frame.shape[0]))
            result = cv2.addWeighted(frame, 1, image, 0.3, gamma=1)
            cv2.imshow('blend3', result)
        elif choice == 4:
            image = cv2.resize(img_3, (frame.shape[1], frame.shape[0]))
            result = cv2.addWeighted(frame, 1, image, 0.3, gamma=1)
            cv2.imshow('blend4', result)
        elif choice == 5:
            image = cv2.resize(img_4, (frame.shape[1], frame.shape[0]))
            result = cv2.addWeighted(frame, 1, image, 0.3, gamma=1)
            cv2.imshow('blend5', result)
        elif choice == 6:
            image = cv2.resize(img_5, (frame.shape[1], frame.shape[0]))
            result = cv2.addWeighted(frame, 1, image, 0.3, gamma=1)
            cv2.imshow('blend6', result)

    else:
        print("can't access")
        break

    if cv2.waitKey(10) & 0xff == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()