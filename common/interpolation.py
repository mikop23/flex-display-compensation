import numpy as np

def bilinear(img, x, y):
    """x, y: 픽셀 좌표 배열. 0 ≤ x < W−1, 0 ≤ y < H−1 이어야 함(범위 검사 안 함)."""
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