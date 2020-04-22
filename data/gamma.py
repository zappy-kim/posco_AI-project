# import the necessary packages
from __future__ import print_function
import numpy as np
import cv2
import os
 
def adjust_gamma(image,gamma=2.5):
	# build a lookup table mapping the pixel values [0, 255] to
	# their adjusted gamma values
	invGamma = 1.0 / gamma
	table = np.array([((i / 255.0) ** invGamma) * 255
		for i in np.arange(0, 256)]).astype("uint8")
 
	# apply gamma correction using the lookup table
	return cv2.LUT(image, table)
gamma=2.5
# load the original image
for i in range(0,124):
	imagepath='/home/pirl/test/project1/night_frame_resize/frame{}.png'.format(i)
	original = cv2.imread(imagepath)
	adjusted = adjust_gamma(original,gamma=gamma)
	directory='/home/pirl/test/project1/gamma'
	os.chdir(directory)
	cv2.imwrite('new_frame{}.png'.format(i),adjusted)




