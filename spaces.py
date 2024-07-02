import cv2 as cv
import matplotlib.pyplot as plt

# openCV reads images in BGR format. Outside of openCV, we use the RGB format
img = cv.imread("Photos/texture.jpg")
cv.imshow("texture",img)

#bgr to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

# bgr to HSV - HUE SATURATION VALUE
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("HSV",hsv)

# bgr to L*a*b
lab = cv.cvtColor(img,cv.COLOR_BGR2Lab)
cv.imshow("Lab",lab)

# BGR TO RGB
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("RGB",rgb)


cv.waitKey(0)