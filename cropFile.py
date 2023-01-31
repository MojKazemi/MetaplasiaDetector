import cv2
import os
import numpy as np

class cropInpaint(): 
    
    def __init__(self) :

        self.lower = np.array([187,193,163])
        self.upper = np.array([265,265,295])
        self.flags = cv2.INPAINT_NS

    # def run(self, filePathBIN, filePathOR):
    def run(self, filePathOR, folderPat):

        nameFile = filePathOR.split("\\")[-1]

        dest = os.path.join(folderPat, "Results\\original", nameFile)
        
        # Reading image
        img = cv2.imread(filePathOR, cv2.IMREAD_COLOR)
        
        num_rows, num_cols = img.shape[:2]
        translation_matrix = np.float32([ [1,0,600], [0,1,20] ])
        img2 = cv2.warpAffine(img, translation_matrix, (num_cols,num_rows))

        gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        # Converting image to a binary image( black and white only image).
        _, threshold = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)

        # Detecting contours in image.
        contours, _= cv2.findContours(threshold, cv2.RETR_EXTERNAL,
                                        cv2.CHAIN_APPROX_SIMPLE)
        c = max(contours, key = cv2.contourArea)
        x,y,w,h = cv2.boundingRect(c)

        for i, cnt in enumerate(contours) :
                x2,y2,w2,h2 = cv2.boundingRect(cnt)
                if x2 < x: 
                    x = x2 
                if y2 < y: 
                    y = y2 
                if x2 > w + x: 
                    w = x2 
                if y2 > h + y: 
                    h = y2

        crop_imm = img2[y:y+h, x:x+w]

        mask = cv2.inRange(crop_imm,self.lower,self.upper)
        output = cv2.inpaint(crop_imm, mask, 3, flags=self.flags)

        cv2.imwrite(dest,output)

