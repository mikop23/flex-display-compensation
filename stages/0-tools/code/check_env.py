import numpy as np
import matplotlib as mpl
import cv2 as cv
import PIL as pl
import matplotlib.pyplot as plt

print(np.__version__)
print(mpl.__version__)
print(cv.__version__)
print(pl.__version__)

img = np.zeros((100,100))
plt.imshow(img, cmap='gray')
plt.show()


