import cv2 as cv

img = cv.imread('Photos/tennisBall.jpg')
cv.imshow("tennisBall",img)

def rescaleFrame(frame, scale=0.75):
    #Images, Videoss and live video
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img,scale=0.15)
cv.imshow('Image',resized_image)

def changeRes(width,height):
    #live video eg straight from webcam
    capture.set(3,width)
    capture.set(4,height)

# Reading videos
capture = cv.VideoCapture('Videos/sendImageESPNow.gif')

while True:
    isTrue,frame = capture.read() #reads vid frame-by-frame. returns frame & bool if successful

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video',frame)#can display each frame
    cv.imshow('Video Resized',frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):#stops vid playing ...by pressing d
        break

capture.release()
cv.destroyAllWindows()