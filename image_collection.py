"""
Коллекция изображений с фильтрацией и группировкой.

Вариант 1: filter_by_resolution(), group_by_color_space().
"""
from typing import List, Dict, Tuple
from dataclasses import dataclass, field

from media_objects import Image


@dataclass
class ImageInfo:
    """Расширенная информация об изображении для коллекции.

    Атрибуты:
        filename: имя файла
        width, height: размеры
        channels: число каналов
        tags: список тегов
    """
    filename: str
    width: int
    height: int
    channels: int
    tags: List[str] = field(default_factory=list)

    @property
    def resolution(self) -> Tuple[int, int]:
        """Разрешение в виде кортежа (ширина, высота)."""
        return (self.width, self.height)

    @property
    def color_space(self) -> str:
        """Цветовое пространство по числу каналов."""
        mapping = {1: "Grayscale", 3: "RGB", 4: "RGBA"}
        return mapping.get(self.channels, "Unknown")

    def __str__(self) -> str:
        return (f"{self.filename} ({self.width}x{self.height}, "
                f"{self.color_space})")


class ImageCollection:
    """Коллекция изображений с методами фильтрации и группировки."""

    def __init__(self) -> None:
        self._images: List[ImageInfo] = []

    def add(self, image: ImageInfo) -> None:
        """Добавляет изображение в коллекцию."""
        if not isinstance(image, ImageInfo):
            raise TypeError("Можно добавлять только ImageInfo")
        self._images.append(image)

    def get_all(self) -> List[ImageInfo]:
        """Возвращает все изображения."""
        return self._images.copy()

    # ---------- ВАРИАНТ 1: фильтрация по разрешению ----------
    def filter_by_resolution(self, min_width: int = 0,
                             min_height: int = 0) -> List[ImageInfo]:
        """Фильтрует изображения по минимальному разрешению.

        Возвращает те, у которых width >= min_width И height >= min_height.
        """
        return [
            img for img in self._images
            if img.width >= min_width and img.height >= min_height
        ]

    # ---------- ВАРИАНТ 1: группировка по цветовому пространству ----------
    def group_by_color_space(self) -> Dict[str, List[ImageInfo]]:
        """Группирует изображения по цветовому пространству.

        Возвращает словарь {цветовое пространство: [изображения]}.
        """
        groups: Dict[str, List[ImageInfo]] = {}
        for img in self._images:
            cs = img.color_space
            groups.setdefault(cs, []).append(img)
        return groups

    def __len__(self) -> int:
        return len(self._images)

    def __str__(self) -> str:
        return f"<ImageCollection: {len(self._images)} изображений>"


if __name__ == "__main__":
    print("=" * 60)
    print("Проверка ImageCollection")
    print("=" * 60)

    col = ImageCollection()
    col.add(ImageInfo("photo1.jpg", 1920, 1080, 3, ["nature", "sunset"]))
    col.add(ImageInfo("photo2.jpg", 1280, 720, 3, ["nature"]))
    col.add(ImageInfo("scan.png", 800, 600, 1, ["document"]))
    col.add(ImageInfo("logo.png", 256, 256, 4, ["branding"]))
    col.add(ImageInfo("hd.jpg", 3840, 2160, 3, ["nature", "4k"]))

    print(f"\n  Всего: {len(col)}")

    print("\n  --- filter_by_resolution(min_width=1280, min_height=720) ---")
    for img in col.filter_by_resolution(1280, 720):
        print(f"    {img}")

    print("\n  --- group_by_color_space() ---")
    for cs, imgs in col.group_by_color_space().items():
        print(f"    {cs}: {len(imgs)} изображений")
        for img in imgs:
            print(f"       {img.filename}")
