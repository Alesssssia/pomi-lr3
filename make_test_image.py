"""Генерирует тестовое изображение с шумом «соль и перец»."""
import cv2
import numpy as np

h, w = 400, 400
img = np.zeros((h, w, 3), dtype=np.uint8)

for i in range(h):
    img[i, :] = (i * 255 // h, 100, 200)

rng = np.random.default_rng(42)
salt = rng.random((h, w)) < 0.03
pepper = rng.random((h, w)) < 0.03
img[salt] = 255
img[pepper] = 0

cv2.circle(img, (200, 200), 80, (0, 255, 0), -1)
cv2.circle(img, (120, 120), 40, (255, 0, 0), -1)
cv2.putText(img, "TEST", (140, 340),
            cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 3)

cv2.imwrite("test_image.jpg", img)
print("Создан: test_image.jpg", img.shape)
