import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv

class shape(): 

    def __init__(self):
        self.lmask = np.array([-27 , 10  ,29])
        self.hmask = np.array([ 53, 277, 284])   
        
    def run(self, filePathOR):

        img =cv2.imread(filePathOR)         
        # create the Mask
        imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
       
        mask1 = cv2.inRange(imgHSV, self.lmask, self.hmask)
        # inverse mask
        mask = 255-mask1
        res = cv2.bitwise_and(img, img, mask=mask)
        filename = filePathOR.replace("original", "color")

        cv2.imwrite(filename, res)
