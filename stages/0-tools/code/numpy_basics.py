import matplotlib.pyplot as plt
import numpy as np

a = np.linspace(0,255,100)
b = a + 50
b = np.clip(b,0,255)
c = 2*(a-128)+128
c= np.clip(c,0,255)

img1 = np.zeros((100,100))+a
# img1[:,:]= a

img2 = np.zeros((100,100))+b
# img2[:,:]= b

img3 = np.zeros((100,100)) + c
# img3[:,:]= c

plt.subplot(1,3,1)
plt.imshow(img1, cmap='gray', vmax=255, vmin=0)
plt.title("original")

plt.subplot(1,3,2)
plt.imshow(img2, cmap='gray', vmax=255, vmin=0)
plt.title("bright + 50")

plt.subplot(1,3,3)
plt.imshow(img3, cmap='gray', vmax=255, vmin=0)
plt.title("contrast x2")

plt.tight_layout()
plt.savefig("stages/0-tools/results/brightness_contrast.png")
plt.show()
