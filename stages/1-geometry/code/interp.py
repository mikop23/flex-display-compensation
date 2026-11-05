import numpy as np

# def lerp1d(f, x):
#     i = int(np.floor(x))
#     if(i == len(f)-1):
#         return f[i]
#     else:
#       t = x - i
#       left = f[i]
#       right = f[i + 1]
#       return left*(1-t) + right*t

# f = [10, 20, 30]
# print(lerp1d(f, 0.3))
# print(lerp1d(f, 1.5))
# print(lerp1d(f, 2.0))


def bilinear(img, x, y):
    i = int(np.floor(x))
    j = int(np.floor(y))
    tx = x-i
    ty = y-j
    uleft = img[j,i]
    uright = img[j, i+1]
    up = uleft*(1-tx) + uright*tx
    dleft = img[j+1,i]
    dright = img[j+1, i+1]
    down = dleft*(1-tx) + dright*tx
    return up*(1-ty)+down*ty

img = np.array([[10, 20],
                [30, 40]])
print(bilinear(img, 0.5, 0.5))
print(bilinear(img, 0.5, 0.0))
print(bilinear(img, 0.0, 0.5))