# installs below
# pip install opencv-python
# pip install matplotlib
# pip install numpy

import cv2
from matplotlib import pyplot as plt
import numpy as np

# Opening image

# detection grid, use this to find where you are at
grid = cv2.imread("grid.jpeg", cv2.IMREAD_UNCHANGED)
# image you are detecting in the grid
detection = cv2.imread("Payload/4/4.1.jpg", cv2.IMREAD_UNCHANGED)

# the heat map, brighter spots means better
result = cv2.matchTemplate(detection, grid, cv2.TM_CCOEFF_NORMED)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# tells you where the location is in the image and confidence level
print('Best match top left position: %s' % str(max_loc))
print('Best match confidence: %s' % max_val)

# creates a rectangle if image is detected
threshold = .8
if max_val >= threshold:
    print('Found Grid')
    top_left = max_loc
    bottom_right = (top_left[0] + 58, top_left[1] + 58)
    cv2.rectangle(grid, top_left, bottom_right,
                  color=(0, 255, 0), thickness=2, lineType=cv2.LINE_4)
    cv2.imshow('Result', grid)
    cv2.imshow('data', result)
    cv2.waitKey()
else:
    print('Finding')

