import numpy as np
import matplotlib.pyplot as plt
from cylinder import screen_to_view

def bilinear(img, x, y):
    i = np.floor(x).astype(int)
    j = np.floor(y).astype(int)
    txb = x-i
    tyb = y-j
    uleft = img[j,i]
    uright = img[j, i+1]
    up = uleft*(1-txb) + uright*txb
    dleft = img[j+1,i]
    dright = img[j+1, i+1]
    down = dleft*(1-txb) + dright*txb
    return up*(1-tyb)+down*tyb

W, H = 400, 300
R = 300
D = 1000

original = np.zeros((H,W))
original[::40, :] = 255
original[:,::40] = 255
original = original.astype(np.uint8)


c = np.arange(W)
r = np.arange(H)
cols,rows = np.meshgrid(c, r)

x = cols - (W-1)/2
y = rows - (H-1)/2

u, v = screen_to_view(x,y,R,D)

map_x = u + (W-1)/2
map_y = v + (H-1)/2

mask = ~np.isnan(map_x) & (map_x>=0) & (map_x<W-1) & (map_y>=0) & (map_y<H-1)

print(mask.shape)



# corrected = bilinear(original, map_x, map_y)

# plt.imshow(corrected, cmap='gray')
# plt.show()