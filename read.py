import cv2 as cv

# img = cv.imread('Photos/tennisBall.jpg')

# cv.imshow('tennisBall',img)
#cv.waitKey(0)

# Reading videos
capture = cv.VideoCapture('Videos/sendImageESPNow.gif')

while True:
    isTrue,frame = capture.read() #reads vid frame-by-frame. returns frame & bool if successful
    cv.imshow('Video',frame)#can display each frame

    if cv.waitKey(20) & 0xFF==ord('d'):#stops vid playing ...by pressing d
        break

capture.release()
cv.destroyAllWindows()

