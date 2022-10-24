import skimage.io
import skimage.color
import skimage.filters
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from skimage import img_as_ubyte
import imutils
import os
import json

disc = {}

def image(file):
    image = skimage.io.imread(file)
    gray_image = skimage.color.rgb2gray(image)
    hsv_image = skimage.color.rgb2hsv(image)
    blurred_image = skimage.filters.gaussian(gray_image, sigma=1.0)
    hue_img = hsv_image[:, :, 0]
    sat_img = hsv_image[:, :, 1]
    value_img = hsv_image[:, :, 2]
    max_val = np.max(blurred_image)
    t = skimage.filters.threshold_otsu(value_img)
    thresholds = skimage.filters.threshold_multiotsu(gray_image, classes=3)
    regions = np.digitize(gray_image, bins=thresholds)
    binary_mask = gray_image < thresholds[0]
    binary_mask = skimage.morphology.remove_small_objects(binary_mask, 50)
    binary_mask = skimage.morphology.remove_small_holes(binary_mask, 50)
    save =  img_as_ubyte(image)
    cv_image = img_as_ubyte(binary_mask)
    contours, hierarchies = cv.findContours(cv_image, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    return contours



def makepoints(contured):
    if (len(contured) != 0):
        conture = []
        point = []
        for x in range(len(contured)):
            for i in  range(len(contured[x])):
                a=contured[x][i][0][0]
                b=contured[x][i][0][1]
                point.append([int(a),int(b)])
            conture.append(point)
        return conture

files = os.listdir(r"/Volumes/Transcend/ECHO Share/Ralf_Irmela-2")
path = "/Volumes/Transcend/ECHO Share/Ralf_Irmela-2/"
for file in files:
    disc.update({file:makepoints(image(path+file))})
    with open(file+'.json', 'w') as fp:
        json.dump(disc, fp)
