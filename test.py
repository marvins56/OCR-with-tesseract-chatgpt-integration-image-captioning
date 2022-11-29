import cv2

cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 500)

while(True):
    ret, frame = cap.read()
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break