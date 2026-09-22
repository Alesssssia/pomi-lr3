"""
Скрипт для обработки изображений с использованием OpenCV.

Вариант 1: загрузка → grayscale → медианный фильтр → сохранение.
"""
import os
import cv2
import numpy as np


def load_image(file_path: str):
    """Загружает изображение с обработкой ошибок."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл не найден: {file_path}")

    img = cv2.imread(file_path)
    if img is None:
        raise ValueError(f"Не удалось загрузить изображение: {file_path}")

    print(f"  Загружено: {file_path}")
    print(f"    shape = {img.shape}")
    print(f"    dtype = {img.dtype}")
    print(f"    высота × ширина = {img.shape[0]} × {img.shape[1]}")
    if len(img.shape) == 3:
        print(f"    каналов = {img.shape[2]}")

    return img


def convert_to_grayscale(img):
    """Преобразует изображение в оттенки серого."""
    if len(img.shape) == 2:
        return img
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def apply_median_filter(img, kernel_size: int = 5):
    """Применяет медианный фильтр."""
    if kernel_size < 3 or kernel_size % 2 == 0:
        raise ValueError("kernel_size должен быть нечётным и >= 3")
    return cv2.medianBlur(img, kernel_size)


def extract_roi(img, size: int = 100):
    """Выделяет центральную область size × size."""
    h, w = img.shape[:2]
    if size > h or size > w:
        raise ValueError(f"Размер ROI ({size}) больше изображения ({h}×{w})")

    y_start = h // 2 - size // 2
    x_start = w // 2 - size // 2
    return img[y_start:y_start + size, x_start:x_start + size]


def invert_colors(img):
    """Инвертирует цвета изображения (255 - pixel)."""
    return 255 - img


def main():
    """Основная функция — вариант 1."""
    file_path = "test_image.jpg"

    print("=" * 60)
    print("ЛР4 — Вариант 1: grayscale + медианный фильтр")
    print("=" * 60)

    print("\n[1] Загрузка изображения")
    try:
        img = load_image(file_path)
    except (FileNotFoundError, ValueError) as e:
        print(f"  Ошибка: {e}")
        return

    print("\n[2] Преобразование в оттенки серого")
    gray = convert_to_grayscale(img)
    print(f"  shape = {gray.shape}")
    cv2.imwrite("result_gray.jpg", gray)
    print("  Сохранено: result_gray.jpg")

    print("\n[3] Медианный фильтр (kernel=5)")
    gray_median = apply_median_filter(gray, 5)
    cv2.imwrite("result_median.jpg", gray_median)
    print("  Сохранено: result_median.jpg")

    print("\n[4] Медианный фильтр на цветном изображении")
    color_median = apply_median_filter(img, 5)
    cv2.imwrite("result_color_median.jpg", color_median)
    print("  Сохранено: result_color_median.jpg")

    print("\n[5] Инверсия центральной области (ROI 100×100)")
    inv = img.copy()
    roi = extract_roi(inv, 100)
    h, w = inv.shape[:2]
    y_start = h // 2 - 50
    x_start = w // 2 - 50
    inv[y_start:y_start + 100, x_start:x_start + 100] = invert_colors(roi)
    cv2.imwrite("result_roi_invert.jpg", inv)
    print("  Сохранено: result_roi_invert.jpg")

    print("\n" + "=" * 60)
    print("ГОТОВО. Все файлы сохранены.")
    print("=" * 60)


if __name__ == "__main__":
    main()
