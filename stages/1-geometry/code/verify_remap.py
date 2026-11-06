import sys
sys.path.append('common')
from metrics import psnr

import cv2
import numpy as np

def bilinear(img, x, y):
    i = int(np.floor(x))
    j = int(np.floor(y))
    txb = x-i
    tyb = y-j
    uleft = img[j,i]
    uright = img[j, i+1]
    up = uleft*(1-txb) + uright*txb
    dleft = img[j+1,i]
    dright = img[j+1, i+1]
    down = dleft*(1-txb) + dright*txb
    return up*(1-tyb)+down*tyb

img = cv2.imread(r'stages/0-tools/data/test.jpg', cv2.IMREAD_GRAYSCALE)

img = cv2.resize(img,(200,150))

h, w= img.shape

xs = np.arange(w)
ys = np.arange(h)

X, Y = np.meshgrid(xs,ys)
x = X.ravel()
y = Y.ravel()
ones = np.ones(x.size)

pts = np.vstack([x,y,ones])

tx, ty = w/2,h/2
T_to_origin = np.array([[1,0,-tx],
                        [0,1,-ty],
                        [0,0,1]])

T_back =  np.array([[1,0,tx],
                    [0,1,ty],
                    [0,0,1]])

cos = np.cos(np.pi/6)
sin = np.sin(np.pi/6)

R = np.array([[cos,-sin,0],
              [sin,cos,0],
              [0,0,1]])

H = T_back@R@T_to_origin

H_inv =np.linalg.inv(H)

src = H_inv@pts

ok_b = (src[0] >= 0) & (src[0] < w-1) & (src[1] >= 0) & (src[1] < h-1)

out_b = np.zeros(img.shape)

for k in range(len(x)):
    if ok_b[k]:
        out_b[y[k], x[k]] = round(bilinear(img, src[0][k], src[1][k]))


map_x = src[0].reshape(h,w).astype(np.float32)
map_y = src[1].reshape(h,w).astype(np.float32)
out_cv = cv2.remap(img, map_x, map_y, cv2.INTER_LINEAR)

mask = ok_b.reshape(h, w)
diff = np.abs(out_b - out_cv)
print(np.sum(diff[mask] > 0))   # 다른 칸 개수
print(diff[mask].max())         # 최대 차이
print(psnr(out_b, out_cv, mask))
