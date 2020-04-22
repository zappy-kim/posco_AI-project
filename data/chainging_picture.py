from PIL import Image
import numpy as np
import os.path, sys 

# for i in range(0,124):
#     im=Image.open('/home/pirl/test/project1/night_frame_resize/frame{}.png'.format(i))
#     Image.eval(im, lambda x:x+50).save("/home/pirl/test/project1/night_frame_resize_new/newframe{}.png".format(i))





## checking image size
from scipy import misc
import glob

import imageio
# for i in range(1,319):
#     im = imageio.imread('/home/pirl/test/frame/dayframe/day_gps_/dgps_crop{}.png'.format(i))
# im2 = imageio.imread('newframe0.png')
    # print(im.shape)
# print(im2.shape)
path = '/home/pirl/test/frame/nightframe/night_rist_crop'
dirs = os.listdir(path) 
for item in dirs: 
        fullpath = os.path.join(path,item)   #corrected 
        if os.path.isfile(fullpath): 
            im = imageio.imread(fullpath) 
            print(im.shape)
