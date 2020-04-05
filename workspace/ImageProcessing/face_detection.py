import cv2
import numpy as np

cap = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier("cascades/face.xml")
eyeCascade = cv2.CascadeClassifier("cascades/eye.xml")

while True:
    _, frame = cap.read()
    frame = cv2.resize(frame, (640, 360))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, 1.1, 3)
    eyes = eyeCascade.detectMultiScale(gray, 1.1, 3)

    for (x, y, w, h) in eyes:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.putText(frame, "Enemy Detected!", (x, y - 10), cv2.QT_FONT_NORMAL, 1, (0, 0, 255), 1)

    cv2.imshow("Face Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
