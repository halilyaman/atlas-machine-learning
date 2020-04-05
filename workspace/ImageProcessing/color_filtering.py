import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    frame = cv2.resize(frame, (640, 360))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # hsv hue-saturation-value
    # optimized for red color
    lower_red = np.array([170, 0, 0])
    upper_red = np.array([220, 255, 255])

    # generating mask
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # applying the mask to a frame
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", result)
    # exit if the user presses 'q'
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()