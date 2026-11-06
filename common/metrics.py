import numpy as np
from skimage.metrics import structural_similarity
import cv2


def psnr(a,b, mask=None):
    a = a.astype(float)
    b = b.astype(float)

    if mask is not None:
        a = a[mask]
        b = b[mask]

    mse = np.mean((a-b)**2)

    if mse == 0:
        return np.inf

    return 10*np.log10(255**2/mse)


def ssim(a,b,mask=None):
    a = a.astype(float)
    b = b.astype(float)
    score, smap = structural_similarity(a, b, data_range=255, full=True)

    if mask is None:
        return score
    
    smap = smap[mask]
    smap = np.mean(smap)
    return smap



if __name__ == '__main__':
    a = np.array([[100, 100], [100, 100]], dtype=np.uint8)
    b = np.array([[100, 100], [100, 110]], dtype=np.uint8)
    print(psnr(a, a))
    print(psnr(a, b))

    mask = np.array([[True, True], [True, False]])
    print(psnr(a, b, mask))   # inf

    img = cv2.imread(r'stages/0-tools/data/test.jpg', cv2.IMREAD_GRAYSCALE)
    bright = np.clip(img.astype(float)+ 10, 0, 255)

    print(ssim(img, img))       # 1.0
    print(ssim(img, bright))    # 0.990
    print(psnr(img, bright))    # 28.13

    mask = np.zeros(img.shape, dtype=bool)
    mask[:50, :] = True
    print(ssim(img, bright, mask))    

    q = img[:,:-1]
    w = img[:,1:]
    print(psnr(q,w), ssim(q,w))