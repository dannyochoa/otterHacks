import cv2
import numpy as np


def estimate_area(contour_array):
    """Returns a list of areas enclosed by contours
    """
    areas = []
    for cnt in contour_array:
        area = cv2.contourArea(cnt)
        areas.append(area)
    return areas


def find_contours(low, up, frame):
    """Returns a list of contours based on upper and lower hsv bounds
    """
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, low, up)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    # cv2.imshow('frame', frame)
    # cv2.imshow('mask', mask)
    # cv2.imshow('res', res)
   
    blurred = cv2.pyrMeanShiftFiltering(res, 30, 30)
    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    return contours


def getRotRatio(img):
    low_rot = np.array([1, 100, 70])
    up_rot = np.array([26, 255, 255])

    low_leaf = np.array([30, 100, 70])
    up_leaf = np.array([70, 255, 255])
    #
    grape_leaf = cv2.imread(img)

    gl_rot_edit = grape_leaf.copy()

    gl_leaf_edit = grape_leaf.copy()

    
    #gl_rot_edit = grape_leaf.copy()
    #gl_leaf_edit = grape_leaf.copy()

    rot_contours = find_contours(low_rot, up_rot, grape_leaf)
    cv2.drawContours(gl_rot_edit, rot_contours, -1, (0, 0, 255), 2)
    cv2.imwrite('static/rot.jpg', gl_rot_edit)

    leaf_contours = find_contours(low_leaf, up_leaf, grape_leaf)
    # cv2.drawContours(gl_leaf_edit, leaf_contours, -1, (0, 0, 255), 2)
    # cv2.imwrite('leaf.png', gl_leaf_edit)

    # cv2.imshow('orange', gl_rot_edit)
    # cv2.waitKey(0)
    # cv2.imshow('orange', gl_leaf_edit)
    # cv2.waitKey(0)
    #
    rot_areas = estimate_area(rot_contours)
    leaf_areas = estimate_area(leaf_contours)

    total_rot_area = sum(rot_areas)
    total_leaf_area = sum(leaf_areas)

    rot_ratio = float(total_rot_area / total_leaf_area) * 100.00
    return rot_ratio


if __name__ == "__main__":
    rot_ratio = getRotRatio("/hackathon/plant/static/7178ad19-5dbf-4836-a5e7-a729a0497630--concord-grape-leaves.jpg")
