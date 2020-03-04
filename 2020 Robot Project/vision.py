#
# This is a demo program showing CameraServer usage with OpenCV to do image
# processing. The image is acquired from the USB camera, then a rectangle
# is put on the image and sent to the dashboard. OpenCV has many methods
# for different types of processing.
#
# NOTE: This code runs in its own process, so we cannot access the robot here,
#       nor can we create/use/see wpilib objects
#
# To try this code out locally (if you have robotpy-cscore installed), you
# can execute `python3 -m cscore vision.py:main`
#

import cv2
import numpy as np

from cscore import CameraServer


def main():
    cs = CameraServer.getInstance()
    cs.enableLogging()

    # camera = cs.startAutomaticCapture()

    # camera.setResolution(320, 240)

    # Get a CvSink. This will capture images from the camera
    # cvSink = cs.getVideo()
    cvSink2 = cv2.VideoCapture(1)

    # (optional) Setup a CvSource. This will send images back to the Dashboard
    outputStream = cs.putVideo("Rectangle", 320, 240)

    # Allocating new images is very expensive, always try to preallocate
    img = np.zeros(shape=(240, 320, 3), dtype=np.uint8)

    while True:
        # Tell the CvSink to grab a frame from the camera and put it
        # in the source image.  If there is an error notify the output.
        # time, img = cvSink.grabFrame(img)
        # print(img[0][0])
        # if time == 0:
        #     # Send the output the error.
        #     outputStream.notifyError(cvSink.getError())
        #     # skip the rest of the current iteration
        #     continue
        ret, img = cvSink2.read()
        print(img[0][0])

        # Put a rectangle on the image
        # cv2.rectangle(img, (100, 100), (300, 300), (255, 255, 255), 5)
        threshold_img = cv2.inRange(img, (220, 215, 190), (255, 255, 255))
        
        erode_dilate_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

        threshold_img = cv2.erode(threshold_img, erode_dilate_kernel, iterations= 3)

        threshold_img = cv2.dilate(threshold_img, erode_dilate_kernel, iterations= 3)

        contours, hierarchy = cv2.findContours(threshold_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        maximum_area = 0
        
        maximum_contour = np.array([[0,0],[0,0], [0,0]], dtype=np.int32)
        
        maximum_contour = np.array([])
        for cnt in contours:
            area = abs(cv2.contourArea(cnt))
            if area >= 500 and area > maximum_area:
                print("Contour Found", area)
                maximum_area = area
                maximum_contour = cnt

        thresholdFrame3Ch = np.zeros_like(img)
        for channel in range(img.shape[2]):
            thresholdFrame3Ch[:, :, channel] = threshold_img    
        
        if maximum_contour.size > 0:
            cv2.drawContours(thresholdFrame3Ch, [maximum_contour], 0, (0,0,255), 2)    
        
                




        
        
        numComponents, labledFrame, stats, centroids = cv2.connectedComponentsWithStats(threshold_img, ltype= cv2.CV_16U)
        
        
        
        # Give the output stream a new image to display
        
        outputStream.putFrame(thresholdFrame3Ch)
      
    