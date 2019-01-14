from scipy.misc import imread, imsave, imresize

img = imread('cat.jpg')
print(img.dtype, img.shape)
print(img)
img_tinted = img * [1, 0.95, 0.9]
img_tinted = imresize(img_tinted, (300, 300))
imsave('cat_tined.jpg', img_tinted)
