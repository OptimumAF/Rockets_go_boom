
# import required module
import os
import cv2 as cv

directory = 'Pictures'

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        print(f)
        image = cv.imread(f, cv.IMREAD_UNCHANGED)
        detection = cv.resize(image, (58, 58), interpolation=cv.INTER_AREA)

        cv.imshow('output', image)
        cv.imshow('resize', detection)
        cv.waitKeyEx(0)

