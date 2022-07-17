import PIL.Image
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("/Users/rieke/Desktop/1.jpg")
image = cv2.GaussianBlur(img,(5,5),0)
#cv2.imshow('Filtered_original',image)

Lab = cv2.cvtColor(image, cv2.COLOR_LBGR2LAB)

#masking/thresholding
lower = np.array([130,146,70])
upper = np.array([255,255,180])

mask = cv2.inRange(Lab, lower, upper)
#cv2.imshow('Masked',mask)

masked = np.ones(image.shape[:2], dtype="uint8") * 255
masked2 = np.ones(image.shape[:2], dtype="uint8") * 255
masked3 = np.ones(image.shape[:2], dtype="uint8") * 255

#morphology
kernal = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal, iterations = 2)
final = cv2.dilate(opening,kernal,iterations = 3)
#cv2.imshow('Final',final)

# find contours
(_, contours, _) = cv2.findContours(final, cv2.RETR_EXTERNAL,
cv2.CHAIN_APPROX_SIMPLE)


blur = cv2.GaussianBlur(eq, (5,5), 0)
#edge = cv2.divide(gray,blur)
canny = cv2.Canny(blur,100,200)
plt.imshow(canny)
plt.show()
dilated = cv2.dilate(canny, (3, 3), iterations=1)
(cnt, hierarchy) = cv2.findContours(
    dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.drawContours(rgb, cnt, -1, (0, 255, 0), 2)
plt.imshow(rgb)
plt.show()
print("coins in the image : ", len(cnt))





#image = tf.image.decode_jpeg(tf.io.read_file("/Users/rieke/Desktop/0e038241-a30d-493d-95eb-4d1829c6e33f.jpg"), channels=3)
#image_bright = tf.image.adjust_brightness(image, delta=0.02)
#image_sat = tf.image.adjust_saturation(image_bright, 2)
#plt.imshow(image_sat,cmap='Greys_r')
#plt.show()
#image_grey = tf.image.rgb_to_grayscale(image_sat)
#image_contrast = tf.image.adjust_contrast(image_grey, contrast_factor=1.25)
#plt.imshow(image_contrast,cmap='Greys_r')
#plt.show()