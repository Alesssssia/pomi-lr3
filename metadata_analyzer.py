"""
Анализ метаданных через множества (Set).

Вариант 1: изображения (JPEG, PNG).
Собираем уникальные форматы, теги, модели камер.
Демонстрируем операции пересечения, объединения, разности.
"""
from typing import Dict, Any, Set, List


class MetadataAnalyzer:
    """Анализатор метаданных изображений с использованием множеств."""

    def __init__(self) -> None:
        self.file_formats: Set[str] = set()
        self.tags_used: Set[str] = set()
        self.camera_models: Set[str] = set()

    def analyze_file(self, file_path: str, metadata: Dict[str, Any]) -> None:
        """Анализирует метаданные одного файла."""
        # Формат файла
        ext = file_path.split('.')[-1].lower()
        self.file_formats.add(ext)

        # Теги
        tags = metadata.get('tags', [])
        for tag in tags:
            self.tags_used.add(tag)

        # Модель камеры
        camera = metadata.get('camera_model')
        if camera:
            self.camera_models.add(camera)

    def get_summary(self) -> Dict[str, int]:
        """Сводка по количеству уникальных значений."""
        return {
            'formats': len(self.file_formats),
            'tags': len(self.tags_used),
            'camera_models': len(self.camera_models),
        }

    def get_common_tags(self, other_tags: Set[str]) -> Set[str]:
        """Пересечение тегов (общие)."""
        return self.tags_used & other_tags

    def get_all_tags_union(self, other_tags: Set[str]) -> Set[str]:
        """Объединение тегов (все уникальные)."""
        return self.tags_used | other_tags

    def get_unique_tags(self, other_tags: Set[str]) -> Set[str]:
        """Разность тегов (только у нас)."""
        return self.tags_used - other_tags


if __name__ == "__main__":
    print("=" * 60)
    print("Анализ метаданных через множества")
    print("=" * 60)

    analyzer = MetadataAnalyzer()

    files = [
        ("photo1.jpg", {"tags": ["nature", "sunset"],
                        "camera_model": "Canon EOS 5D"}),
        ("photo2.png", {"tags": ["nature", "macro"],
                        "camera_model": "Nikon D850"}),
        ("photo3.jpg", {"tags": ["portrait", "studio"],
                        "camera_model": "Canon EOS 5D"}),
        ("scan.png",   {"tags": ["document"]}),
    ]

    for path, meta in files:
        analyzer.analyze_file(path, meta)

    print("\n  Сводка:")
    for key, value in analyzer.get_summary().items():
        print(f"    {key}: {value}")

    print(f"\n  Уникальные форматы:  {analyzer.file_formats}")
    print(f"  Уникальные теги:     {analyzer.tags_used}")
    print(f"  Уникальные камеры:   {analyzer.camera_models}")

    # Операции с множествами
    print("\n  --- Операции с множествами ---")
    other_tags = {"nature", "portrait", "wedding"}

    print(f"  Наши теги:        {analyzer.tags_used}")
    print(f"  Другие теги:      {other_tags}")
    print(f"  Пересечение (&):  {analyzer.get_common_tags(other_tags)}")
    print(f"  Объединение (|):  {analyzer.get_all_tags_union(other_tags)}")
    print(f"  Разность (-):     {analyzer.get_unique_tags(other_tags)}")
