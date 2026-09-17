"""
Финальный тест ЛР3.

Проверка:
1. Универсальных классов (MediaCollection, MediaMetadata)
2. ImageCollection: фильтрация и группировка
3. MetadataAnalyzer: анализ через множества
"""
from media_collection import MediaCollection, MediaMetadata
from image_collection import ImageCollection, ImageInfo
from metadata_analyzer import MetadataAnalyzer


def section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def main():
    # ---------- 1. Универсальная коллекция ----------
    section("1. MediaCollection (Generic[T])")

    col_str = MediaCollection()
    col_str.add("a.jpg")
    col_str.add("b.png")
    col_str.add("c.mp4")
    print(f"  Строк: {len(col_str)}, элементы: {col_str.get_all()}")

    col_int = MediaCollection()
    col_int.add(10)
    col_int.add(20)
    print(f"  Чисел: {len(col_int)}, элементы: {col_int.get_all()}")

    # Дубликат
    try:
        col_str.add("a.jpg")
    except ValueError as e:
        print(f"  Дубликат пойман: {e}")

    # ---------- 2. Метаданные ----------
    section("2. MediaMetadata")

    md = MediaMetadata("photo.jpg")
    md.set_metadata("width", 1920)
    md.set_metadata("height", 1080)
    md.set_metadata("camera_model", "Canon EOS 5D")
    md.set_metadata("tags", ["nature", "sunset"])
    print(f"  {md}")
    print(f"  width:  {md.get_metadata('width')}")
    print(f"  iso:    {md.get_metadata('iso', 'нет')}")

    # ---------- 3. ImageCollection: фильтрация и группировка ----------
    section("3. ImageCollection: filter_by_resolution и group_by_color_space")

    images = ImageCollection()
    images.add(ImageInfo("a.jpg", 1920, 1080, 3, ["nature"]))
    images.add(ImageInfo("b.jpg", 800, 600, 1, ["document"]))
    images.add(ImageInfo("c.png", 256, 256, 4, ["logo"]))
    images.add(ImageInfo("d.jpg", 3840, 2160, 3, ["nature", "4k"]))
    images.add(ImageInfo("e.jpg", 1280, 720, 3, ["nature"]))

    print(f"  Всего: {len(images)}")

    print("\n  filter_by_resolution(1280, 720):")
    for img in images.filter_by_resolution(1280, 720):
        print(f"    {img}")

    print("\n  group_by_color_space():")
    for cs, imgs in images.group_by_color_space().items():
        print(f"    {cs}: {len(imgs)} шт → {[i.filename for i in imgs]}")

    # ---------- 4. MetadataAnalyzer ----------
    section("4. MetadataAnalyzer: множества и их операции")

    analyzer = MetadataAnalyzer()
    files = [
        ("a.jpg", {"tags": ["nature", "sunset"], "camera_model": "Canon"}),
        ("b.jpg", {"tags": ["nature", "macro"], "camera_model": "Nikon"}),
        ("c.png", {"tags": ["logo"], "camera_model": "Canon"}),
    ]
    for path, meta in files:
        analyzer.analyze_file(path, meta)

    print(f"  Сводка: {analyzer.get_summary()}")
    print(f"  Форматы:   {analyzer.file_formats}")
    print(f"  Теги:      {analyzer.tags_used}")
    print(f"  Камеры:    {analyzer.camera_models}")

    other = {"nature", "portrait"}
    print(f"\n  Другие теги: {other}")
    print(f"  Пересечение: {analyzer.get_common_tags(other)}")
    print(f"  Объединение: {analyzer.get_all_tags_union(other)}")
    print(f"  Разность:    {analyzer.get_unique_tags(other)}")

    # ---------- 5. Комбинированный анализ ----------
    section("5. Комбинированный анализ")

    # Изображения в 4K
    hd = images.filter_by_resolution(3840, 2160)
    print(f"  4K изображений: {len(hd)}")

    # Группировка + подсчёт по группам
    groups = images.group_by_color_space()
    for cs, imgs in groups.items():
        avg_w = sum(i.width for i in imgs) / len(imgs)
        print(f"  {cs}: {len(imgs)} шт, средняя ширина = {avg_w:.0f}")

    section("ТЕСТ ЛР3 ЗАВЕРШЁН")


if __name__ == "__main__":
    main()
