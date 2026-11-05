import cv2
import matplotlib.pyplot as plt
import numpy as np


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



xn = np.round(src[0]).astype(int)
yn = np.round(src[1]).astype(int)

ok = (xn >= 0) & (xn < w) & (yn >= 0) & (yn < h)

out = np.zeros_like(img)
out[y[ok], x[ok]] = img[yn[ok], xn[ok]]


plt.imshow(out, cmap='gray')
plt.savefig('stages/1-geometry/results/inverse_warp_nearest.png')
plt.show()