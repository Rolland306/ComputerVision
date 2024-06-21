import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow("Blank",blank)

# img = cv.imread("Photos/shuttleCock.jpg")
# cv.imshow("shuttleCock",img)

# 1. Paint the image a certain color
# blank[:] = 0,255,0
# cv.imshow("Green",blank)

# 2. Draw a rectangle
# cv.rectangle(blank,(0,0), (250,250), (0,255,0), thickness=cv.FILLED)
# cv.imshow("Rectangle",blank)

# 3. Draw a circle
# cv.circle(blank, (250,250), 40, (0,0,255))
# cv.imshow("Circle",blank)

# 4. Draw a line
# cv.line(blank, (100,250), (300,400),(255,255,255),thickness=4)
# cv.imshow("Line",blank)

# 5. Write text
cv.putText(blank,"Hello I'm Tony",(225,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0), thickness=2)
cv.imshow("Text",blank)

cv.waitKey(0)