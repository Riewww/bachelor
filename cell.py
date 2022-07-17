
import cv2
import numpy as np
from matplotlib import pyplot as plt
import skimage.io
import skimage.color
import skimage.filters
image = skimage.io.imread("/Users/rieke/Desktop/blood smears/Image_2510.tif")
# convert the image to grayscale
gray_image = skimage.color.rgb2gray(image)
hsv_image = skimage.color.rgb2hsv(image)

# blur the image to denoise
blurred_image = skimage.filters.gaussian(gray_image, sigma=1.0)

fig, ax = plt.subplots()
plt.imshow(blurred_image, cmap="gray")
plt.show()

#%%
# create a histogram of the blurred grayscale image
hue_img = hsv_image[:, :, 0]
sat_img = hsv_image[:,:,1]
value_img = hsv_image[:, :, 2]

fig, (ax0, ax1, ax2, ax3) = plt.subplots(ncols=4, figsize=(8, 2))
ax0.imshow(image)
ax0.set_title("RGB image")
ax0.axis('off')
ax1.imshow(hue_img, cmap='hsv')
ax1.set_title("Hue channel")
ax1.axis('off')
ax2.imshow(sat_img)
ax2.set_title('Saturation\nChannel')
ax2.axis('off')
ax3.imshow(value_img)
ax3.set_title("Value channel")
ax3.axis('off')
fig.tight_layout()
histogram, bin_edges = np.histogram(hue_img, bins=256, range=(0.0, 1.0))

fig, ax = plt.subplots()
plt.plot(bin_edges[0:-1], histogram)
plt.title("Grayscale Histogram")
plt.xlabel("grayscale value")
plt.ylabel("pixels")
plt.xlim(0, 1.0)
plt.show()

max_val = np.max(blurred_image)
print(max_val)
#%%
t = skimage.filters.threshold_otsu(value_img)
print(t)
binary_mask = blurred_image > t
binary_mask = skimage.morphology.remove_small_objects(binary_mask, 50)
binary_mask = skimage.morphology.remove_small_holes(binary_mask, 50)
fig, ax = plt.subplots()
plt.imshow(binary_mask, cmap="gray")
plt.show()


#%%


contours = skimage.measure.find_contours(binary_mask, 0.8)
fig, ax = plt.subplots()
ax.imshow(binary_mask, cmap=plt.cm.gray)

count = 0
for contour in contours:
    ax.plot(contour[:, 1], contour[:, 0], linewidth=1)
    count = count+1

print(count)
ax.axis('image')
ax.set_xticks([])
ax.set_yticks([])
plt.show()
array = np.array(binary_mask)
array = array.astype("float32")
edge = skimage.feature.canny(array)
plt.imshow(edge)
result = skimage.transform.hough_ellipse(edge)

for x in result:
    print(x)

print(len(result))

cy, cx = skimage.draw.ellipse_perimeter([int(round(x)) for x in result])
binary_mask[cy, cx] = (0, 0, 255)
# Draw the edge (white) and the resulting ellipse (red)
edges = skimage.color.gray2rgb(skimage.img_as_ubyte(binary_mask))

edges[cy, cx] = (250, 0, 0)

fig2, (ax1, ax2) = plt.subplots(ncols=2, nrows=1, figsize=(8, 4),
                                sharex=True, sharey=True)

ax1.set_title('Original picture')
ax1.imshow(image)

ax2.set_title('Edge (white) and result (red)')
ax2.imshow(edges)

plt.show()