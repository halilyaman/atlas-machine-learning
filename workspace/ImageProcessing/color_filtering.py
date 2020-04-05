import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    frame = cv2.resize(frame, (640, 360))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # hsv hue-saturation-value
    # optimized for blue color
    lower_red = np.array([100, 50, 50])
    upper_red = np.array([150, 255, 255])

    # generating mask
    mask = cv2.inRange(hsv, lower_red, upper_red)
    # applying the mask to a frame
    result = cv2.bitwise_and(frame, frame, mask=mask)

    kernel = np.ones((15, 15), np.float32) / (15*15)
    smoothed = cv2.filter2D(result, -1, kernel)
    blur = cv2.GaussianBlur(result, (15, 15), 0)

    # best way for getting rid of noises
    median = cv2.medianBlur(result, 15)

    cv2.imshow("Frame", frame)
    cv2.imshow("Result", result)
    cv2.imshow("Blur", median)
    # cv2.imshow("Smoothed", smoothed)
    # cv2.imshow("Mask", mask)
    # exit if the user presses 'q'
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()