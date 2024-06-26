import cv2 as cv

img = cv.imread("Photos/texture.jpg")

cv.imshow("ShuttleCock",img)

# Converting to Grayscale
gray = cv.cvtColor(img,cv.COLOR_BGRA2GRAY)
cv.imshow("Gray",gray)

# Blur
blur = cv.GaussianBlur(img,(7,7), cv.BORDER_DEFAULT)
cv.imshow("Blur",blur)

# Edge Cascade
canny = cv.Canny(img,125,175)
cv.imshow("Canny Edges",canny)

# Dilating the image
dilated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow("Dilated", dilated)

# Eroding  -> going back to edge cascade after a dilation
eroded = cv.erode(dilated, (3,3),iterations=1)
cv.imshow("Eroded",eroded)

# resize
resized = cv.resize(img,(500,500))
cv.imshow("Resized",resized)

# Cropping
cropped = img[50:200,200:400]
cv.imshow("Cropped",cropped)

cv.waitKey(0)