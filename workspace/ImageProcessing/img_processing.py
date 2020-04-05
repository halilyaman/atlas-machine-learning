import imutils
import cv2
import numpy as np
import matplotlib.pyplot as plt

"""
OpenCV uses BGR for color values instead of RGB. 
"""

# stream = cv2.VideoCapture(0)
#
# while True:
#     ret, frame = stream.read()
#     frame = imutils.resize(frame, width=400)
#     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     gaussian = cv2.adaptiveThreshold(frame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 105, 2)
#     cv2.imshow("gaussian", gaussian)
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break

# img = cv2.imread("images/book.jpg")
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gaussian = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 105, 2)
# ret2, threshold2 = cv2.threshold(gray, 12, 255, cv2.THRESH_BINARY)


# cv2.imshow("original", img)
# cv2.imshow("colored", threshold)
# cv2.imshow("gray", threshold2)
# cv2.imshow("original", img2)
# cv2.imshow("gaussian", gaussian)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# me = cv2.imread("images/me.jpg", cv2.IMREAD_COLOR)
# dog = cv2.imread("images/dog.jpg", cv2.IMREAD_COLOR)
# cat = cv2.imread("images/cat.jpg", cv2.IMREAD_COLOR)
#
# rows, cols, channels = dog.shape
# roi = dog[0: rows, 0:cols]
#
# img2gray = cv2.cvtColor(dog, cv2.COLOR_BGR2GRAY)
#
# ret, mask = cv2.threshold(img2gray, 45, 255, cv2.THRESH_BINARY_INV)


# cv2.imshow("Mask", mask)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# cv2.imshow("Image", mask)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# def black_white_converter(image):
#     row, col, _ = image.shape
#     for i in range(row):
#         for j in range(col):
#             sum_square = (image[i, j][0]**2 + image[i, j][1] ** 2 + image[i, j][2] ** 2)
#             magnitude = np.sqrt(sum_square)
#             if magnitude > 150:
#                 image[i, j] = [0, 0, 0]
#             else:
#                 image[i, j] = [255, 255, 255]
#
# black_white_converter(cat)


# img = cv2.imread("images/lamp.jpg", cv2.IMREAD_COLOR)
# img = imutils.resize(img, width=400)
# my_area = img[50:300, 20:370]
# img[200:450, 20:370] = my_area
# cv2.imshow("Modified Image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# cv2.line(img, (0, 0), (300, 300), (0, 50, 50), 5)
# cv2.rectangle(img, (100, 100), (200, 200), (0, 0, 0), 5)
# cv2.circle(img, (200, 200), 150, (100, 0, 0), 5)
#
# font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(img, "This is Lamp!", (5, 40), font, 1, (200, 255, 255), 3)

# plt.imshow(img, cmap="gray", interpolation="bicubic")
# plt.plot([0, 1000], [1000, 0], "c", linewidth=1)
# plt.show()

"""
Video Capturing
cv2.VideoCapture function takes one parameter
which specify the desired camera to be used.
0 means use first camera 1 means second camera etc...
"""

# cap = cv2.VideoCapture(0)
#
# while True:
#     ret, frame = cap.read()
#
#     if not ret:
#         break
#
#     frame = imutils.resize(frame, width=450)
#     cv2.circle(frame, (225, 125), 100, (100, 0, 0), 10)
#     cv2.imshow("colored", frame)
#
#     # Bitwise AND operator is used because of only taking the last
#     # 8 bits which is the ASCII character to be pressed.
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()
