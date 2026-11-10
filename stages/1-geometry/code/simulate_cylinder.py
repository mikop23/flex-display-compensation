import numpy as np
import matplotlib.pyplot as plt
from cylinder import view_to_screen
from correct_cylinder import make_corrected
import sys, pathlib
sys.path.append(str(pathlib.Path(__file__).resolve().parents[3]))
from common.interpolation import bilinear


def make_viewed(img, R, D):
    H,W = img.shape[:2]
    c = np.arange(W)
    r = np.arange(H)
    cols,rows = np.meshgrid(c, r)

    u = cols - (W-1)/2
    v = rows - (H-1)/2

    x, y = view_to_screen(u,v,R,D)

    map_x = x + (W-1)/2
    map_y = y + (H-1)/2

    mask = ~np.isnan(map_x) & (map_x>=0) & (map_x<W-1) & (map_y>=0) & (map_y<H-1)

    map_x[~mask] = 0
    map_y[~mask] = 0

    viewed = np.round(bilinear(img, map_x, map_y)).astype(np.uint8)

    viewed[~mask] = 0
    return viewed, mask



if __name__ == '__main__':

    W, H = 400, 300
    R = 300
    D = 1000

    original = np.zeros((H,W))
    original[::40, :] = 255
    original[:,::40] = 255
    original = original.astype(np.uint8)

    corrected = make_corrected(original,R,D)

    viewed, mask = make_viewed(original, R, D)
    corrected_viewed, mask = make_viewed(corrected, R, D)

    plt.subplot(1,2,1)
    plt.title('orginal_viewed')
    plt.imshow(viewed, cmap='gray')

    plt.subplot(1,2,2)
    plt.title('corrected_viewed')
    plt.imshow(corrected_viewed, cmap='gray')
    plt.show()
