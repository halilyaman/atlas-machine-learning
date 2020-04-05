import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    frame = cv2.resize(frame, (640, 360))

    laplacian = cv2.Laplacian(frame, cv2.CV_8UC1)
    sobelx = cv2.Sobel(frame, cv2.CV_8UC1, 1, 0, ksize=5)
    sobely = cv2.Sobel(frame, cv2.CV_8UC1, 0, 1, ksize=5)

    edges = cv2.Canny(frame, 100, 150)

    # cv2.imshow("Original", frame)
    # cv2.imshow("Laplacian", laplacian)
    # cv2.imshow("sobelx", sobelx)
    # cv2.imshow("sobely", sobely)
    cv2.imshow("Edges", edges)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()