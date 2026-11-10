import numpy as np
import matplotlib.pyplot as plt
from cylinder import screen_to_view
import sys, pathlib
sys.path.append(str(pathlib.Path(__file__).resolve().parents[3]))
from common.interpolation import bilinear



def make_corrected(img, R, D):
    H, W = img.shape[:2]
    c = np.arange(W)
    r = np.arange(H)
    cols,rows = np.meshgrid(c, r)

    x = cols - (W-1)/2
    y = rows - (H-1)/2

    u, v = screen_to_view(x,y,R,D)

    map_x = u + (W-1)/2
    map_y = v + (H-1)/2

    corrected = np.round(bilinear(img, map_x, map_y)).astype(np.uint8)
    return corrected


if __name__ == "__main__":
    W, H = 400, 300
    R = 300
    D = 1000

    original = np.zeros((H,W))
    original[::40, :] = 255
    original[:,::40] = 255
    original = original.astype(np.uint8)
    plt.imshow(make_corrected(original,R,D), cmap='gray')
    plt.show()