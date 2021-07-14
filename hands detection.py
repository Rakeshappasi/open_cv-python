import cv2
import mediapipe as mp


#for drawing
mp_drawing = mp.solutions.drawing_utils
# for detecting hands
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

with mp_hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
    	success, image = cap.read()
    	if not success:
      		print("Ignoring empty camera frame.")
      		# If loading a video, use 'break' instead of 'continue'.
      		continue

    	results = hands.process(image)
    	if results.multi_hand_landmarks:
    		for hand_landmarks in results.multi_hand_landmarks:
    			mp_drawing.draw_landmarks(
    				image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    			cv2.imshow('MediaPipe Hands', image)
    	if cv2.waitKey(10) & 0xFF == ord("q"):
        	break
      
cap.release()
