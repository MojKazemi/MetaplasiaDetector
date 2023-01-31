import cv2

class GetBinariImag(object):

    def __init__(self):
        self.lower = 100
        self.upper = 150

    def main(self, image_src):

        if image_src is None:
            print ("the image read is None............")
            return

        image_mask = cv2.inRange(image_src,self.lower,self.upper)

        return image_mask
 