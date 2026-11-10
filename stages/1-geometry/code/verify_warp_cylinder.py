import numpy as np
from simulate_cylinder import make_viewed, make_view_maps
import sys, pathlib
sys.path.append(str(pathlib.Path(__file__).resolve().parents[3]))
from common.interpolation import bilinear
from common.metrics import psnr
import cv2

H, W = 300, 400
R = 300
D = 1000

img = np.zeros((H,W))
img[::40, :] = 255
img[:,::40] = 255
img = img.astype(np.uint8)
map_x, map_y, mask = make_view_maps(H, W, R, D)

my_bilinear = np.round(bilinear(img, map_x, map_y))

cv = np.round(cv2.remap(img, map_x.astype(np.float32), map_y.astype(np.float32), cv2.INTER_LINEAR))

error = abs(my_bilinear[mask]-cv[mask])
max_error = error.max()

print((my_bilinear.astype(np.uint8) != cv.astype(np.uint8)).sum())
print(max_error)
print(psnr(my_bilinear.astype(np.uint8), cv.astype(np.uint8), mask))

