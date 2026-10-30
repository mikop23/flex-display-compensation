import matplotlib.pyplot as plt
import numpy as np

a = np.linspace(0, 255, 100)
a = a.reshape((100,1))

img = np.zeros((100,100))
img[:,:] = a

plt.imshow(img, cmap='gray', vmax=255, vmin=0)
plt.show()