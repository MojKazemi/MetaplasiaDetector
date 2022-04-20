import skimage.io
import skimage.filters
import numpy as np
from skimage import color
import os

class blurimage(object):
    def blurim(self,b):
        if not os.path.isdir('./data/results'):
            os.mkdir('./data/results')

        image = skimage.io.imread('./data/orig/'+str(b))

        sigma = 3.0

        # apply Gaussian blur, creating a new image
        blurred = skimage.filters.gaussian(
            image, sigma=(sigma, sigma), truncate=3.5, multichannel=True)

        filename = './data/results/res' + str(b)
        skimage.io.imsave(filename, (color.convert_colorspace(blurred, 'HSV', 'RGB') * 255).astype(np.uint8))

        result = np.random.randint(5, size=1)

        return result