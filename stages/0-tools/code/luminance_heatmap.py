import cv2
import matplotlib.pyplot as plt
img = cv2.imread("stages/0-tools/data/test.jpg")

B = img[0:2048,0:2048,0]
G = img[0:2048,0:2048,1]
R = img[0:2048,0:2048,2]

img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

brightness = 0.299 * R + 0.587 * G + 0.114 * B

plt.subplot(1,2,1)
plt.imshow(img2)
plt.title("original")

plt.subplot(1,2,2)
plt.imshow(brightness, cmap='inferno', vmax=255, vmin=0)
plt.colorbar(fraction = 0.046, pad = 0.04)
plt.title("luminance")

plt.tight_layout()
plt.savefig("stages/0-tools/results/luminance_heatmap.png")
plt.show()


