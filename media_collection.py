"""
Модуль с универсальными классами для мультимедийных данных.

Вариант 1: Изображения (JPEG, PNG).
"""

from typing import TypeVar, Generic, List, Dict, Optional, Set, Any


T = TypeVar('T')


class MediaCollection(Generic[T]):
    """Универсальная коллекция для медиаобъектов."""

    def __init__(self) -> None:
        self._items: List[T] = []

    def add(self, item: T) -> None:
        """Добавляет элемент в коллекцию с проверкой на дубликаты."""
        if item is None:
            raise ValueError("Нельзя добавить None в коллекцию")
        if item in self._items:
            raise ValueError(f"Элемент уже есть в коллекции: {item}")
        self._items.append(item)

    def get_all(self) -> List[T]:
        """Возвращает копию списка всех элементов."""
        return self._items.copy()

    def filter_by_type(self, media_type: type) -> List[T]:
        """Фильтрует элементы по типу (isinstance)."""
        return [item for item in self._items if isinstance(item, media_type)]

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __str__(self) -> str:
        return f"<MediaCollection: {len(self._items)} элементов>"


class MediaMetadata:
    """Класс для хранения метаданных медиафайла."""

    def __init__(self, file_path: str) -> None:
        self.file_path: str = file_path
        self.metadata: Dict[str, Any] = {}

    def set_metadata(self, key: str, value: Any) -> None:
        """Устанавливает значение метаданных."""
        self.metadata[key] = value

    def get_metadata(self, key: str, default: Any = None) -> Any:
        """Возвращает значение метаданных или default."""
        return self.metadata.get(key, default)

    def has_metadata(self, key: str) -> bool:
        """Проверяет наличие ключа в метаданных."""
        return key in self.metadata

    def __str__(self) -> str:
        return f"<MediaMetadata({self.file_path}): {len(self.metadata)} ключей>"


if __name__ == "__main__":
    print("=" * 60)
    print("Проверка универсальных классов")
    print("=" * 60)

    # Коллекция строк
    col = MediaCollection()
    col.add("photo1.jpg")
    col.add("photo2.png")
    print(f"  Коллекция строк: {col}")
    print(f"  Все элементы: {col.get_all()}")

    # Проверка дубликата
    try:
        col.add("photo1.jpg")
    except ValueError as e:
        print(f"  Дубликат: {e}")

    # Проверка None
    try:
        col.add(None)
    except ValueError as e:
        print(f"  None: {e}")

    # Метаданные
    md = MediaMetadata("photo.jpg")
    md.set_metadata("width", 1920)
    md.set_metadata("height", 1080)
    md.set_metadata("camera", "Canon EOS")
    print(f"  Метаданные: {md}")
    print(f"    width  = {md.get_metadata('width')}")
    print(f"    iso    = {md.get_metadata('iso', 'нет данных')}")
    print(f"    camera в метаданных? {md.has_metadata('camera')}")
