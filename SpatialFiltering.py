import cv2
import numpy as np
import matplotlib.pyplot as plt


def sp(Pic, Ser, Size):
    w, h = Pic.shape

    new_pic = np.zeros((w - 2, h - 2))

    Identity = np.zeros((Size, Size))
    Identity[int(Size / 2), int(Size / 2)] = 1

    blur = np.ones((Size, Size)) * 1 / Size ** 2

    for x in range(int(Size / 2), w - int(Size / 2)):
        for y in range(int(Size / 2), h - int(Size / 2)):
            pix = Pic[x - int(Size / 2):x + int(Size / 2) + 1, y - int(Size / 2):y + int(Size / 2) + 1]
            rPix = ((Ser + 1) * Identity * pix) - (Ser * blur * pix)
            sPix = np.sum(rPix)
            new_pic[x - 1, y - 1] = np.clip(sPix, 0, 255)
    return new_pic


img = cv2.imread("Goldhill.tif")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

filter_size = int(input("Enter filter size: "))
k_value = int(input("Enter k value: "))
filtered_img = sp(img, k_value, filter_size)

fig, ax = plt.subplots(1, 2, figsize=(10, 5))
ax[0].imshow(img, cmap='gray')
ax[0].set_title('Input Image')
ax[1].imshow(filtered_img, cmap='gray')
ax[1].set_title('Spatial Linear Filtered Image')
plt.show()

print(np.sum(filtered_img))