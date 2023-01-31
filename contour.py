from __future__ import print_function
from __future__ import division
import errno
import cv2 as cv
import numpy as np
import argparse
import matplotlib.pyplot as plt
import os
from math import atan2, cos, sin, sqrt, pi, dist

class shape(): 

    # def run(self, filePathBIN, filePathOR):
    def run(self, bn, filePathOR):

        src = cv.imread(filePathOR, cv.IMREAD_COLOR)

        # Check if image is loaded successfully
        if bn is None:
            print('Could not open BIN the image:')
            exit(0)
        if src is None:
            print('Could not open or the image:', filePathOR)
            exit(0)

        _, bw = cv.threshold(bn, 220, 255, cv.THRESH_BINARY) 
        contours, _ = cv.findContours(bw, cv.RETR_CCOMP, cv.CHAIN_APPROX_NONE)


        lmask = np.array([0, 0, 0])
        hmask = np.array([255, 255, 255])
        # create the Mask
        mask = cv.inRange(src, lmask, hmask)
        # inverse mask
        mask2 = 255-mask     
        srcCNN = cv.bitwise_and(src, src, mask =mask2)

        for i, c in enumerate(contours):
                # Calculate the area of each contour
                area = cv.contourArea(c)
                area_condition = area > 250
                area_condition2 = area < 120

                smallness = len(c) < 15
                # Ignore contours that are too small or too large
                if area_condition or smallness or area_condition2:
                    continue
                cv.drawContours(srcCNN, contours, i, (0, 180, 0))
                cv.drawContours(src, contours, i, (180, 0, 0))
        
        filenameCNN = filePathOR.replace("original", "shapeCNN")
        filenameGUI = filePathOR.replace("original", "shape")

        cv.imwrite(filenameCNN, srcCNN)
        cv.imwrite(filenameGUI, src)


