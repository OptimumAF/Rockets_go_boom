import cv2 as cv
import numpy as np
import os
import sys

directory = 'Pictures'


width = 102
height = 102
os.chdir(os.path.dirname(os.path.abspath(__file__)))
np.set_printoptions(threshold=sys.maxsize)
grid = cv.imread("grid.jpeg", cv.IMREAD_UNCHANGED)
display = cv.imread("grid.jpeg", cv.IMREAD_UNCHANGED)
detection_points = []
def image_resizer(image):
    locations = []




def findPossibleLocations(detection_image):
    rectangles = []
    #locations = image_resizer(detection_image)
    locations = []
    image = cv.imread(detection_image, cv.IMREAD_UNCHANGED)
    for i in range(348, 1, -1):
        print("test case " + str(i))
        detection = cv.resize(image, (i, i), interpolation=cv.INTER_AREA)
        detection_w = detection.shape[1]
        detection_h = detection.shape[0]
        result = cv.matchTemplate(grid, detection, cv.TM_CCOEFF_NORMED)

        threshold = .8
        locations = np.where(result >= threshold)
        locations = list(zip(*locations[::-1]))

        if len(locations):
            print("found")
            print(locations)
            break
    # print(locations)
    rectangles = []
    for loc in locations:
        rect = [int(loc[0]), int(loc[1]), detection_w, detection_h]
        center = (int(loc[0] + detection_w / 2), int(loc[1] + detection_h / 2))
        detection_points.append(center)
        rectangles.append(rect)
        rectangles.append(rect)

    rectangles, weights = cv.groupRectangles(rectangles, 1, .5)
    if len(rectangles):
        print("Found grid.")
        line_color = (0, 255, 0)
        line_type = cv.LINE_4
        for (x, y, w, h) in rectangles:
            top_left = (x, y)
            bottom_right = (x + w, y + h)
            cv.rectangle(display, top_left, bottom_right, line_color, line_type)
        for point in detection_points:
            cv.circle(display, point, 1, color=(0, 0, 255), thickness=-1)
    #cv.imshow("heatmap", result)
    cv.imshow("Found", display)
    cv.imshow("image", image)
    cv.waitKey(5000)

findPossibleLocations("Payload/2/2.1.jpg")

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        print(f)
        findPossibleLocations(f)
