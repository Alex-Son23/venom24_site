from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db.models.fields.files import ImageFieldFile
from .utils.images import compress_image


@receiver(pre_save)
def compress_all_images(sender, instance, **kwargs):
    """
    Глобальный сигнал: перед сохранением любой модели
    ищем у неё поля ImageField и сжимаем их.
    """
    # чтобы не трогать системные модели, можно отфильтровать по app_label при желании
    opts = getattr(instance, "_meta", None)
    if not opts:
        return

    for field in opts.get_fields():
        # нам нужны только реальные поля модели, а не реляционные many-to-many и т.п.
        if not hasattr(field, "attname"):
            continue

        value = getattr(instance, field.attname, None)

        # django хранит файл как ImageFieldFile
        if isinstance(value, ImageFieldFile):
            # если файл только что загружен / изменён
            if value and not value._committed:
                compressed = compress_image(value)
                if compressed:
                    setattr(instance, field.attname, compressed)
