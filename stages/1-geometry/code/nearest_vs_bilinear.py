import cv2
import matplotlib.pyplot as plt
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

xn = np.round(src[0]).astype(int)
yn = np.round(src[1]).astype(int)

ok_s = (xn >= 0) & (xn < w) & (yn >= 0) & (yn < h)

out_s= np.zeros_like(img)
out_s[y[ok_s], x[ok_s]] = img[yn[ok_s], xn[ok_s]]



ok_b = (src[0] >= 0) & (src[0] < w-1) & (src[1] >= 0) & (src[1] < h-1)

out_b = np.zeros(img.shape)

for k in range(len(x)):
    if ok_b[k]:
        out_b[y[k], x[k]] = round(bilinear(img, src[0][k], src[1][k]))


plt.subplot(1,2,1)
plt.title('nearest')
plt.imshow(out_s, cmap='gray', vmin=0, vmax=255)

plt.subplot(1,2,2)
plt.title('bilinear')
plt.imshow(out_b,cmap='gray', vmin=0, vmax=255)
plt.savefig('stages/1-geometry/results/nearest_vs_bilinear.png')
plt.show()