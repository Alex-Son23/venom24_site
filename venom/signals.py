# signals.py
import os
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db.models import FileField, ImageField
from .utils.images import compress_image  # твоя функция

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp"}  # можно расширить


@receiver(pre_save)
def compress_all_images(sender, instance, **kwargs):
    opts = getattr(instance, "_meta", None)
    if not opts:
        return

    # берем только ОДНОПОЛЬНЫЕ поля модели (без m2m)
    for field in opts.fields:
        if not isinstance(field, (FileField, ImageField)):
            continue

        value = getattr(instance, field.name, None)
        if not value:
            continue

        # проверяем расширение — если .mp4/.pdf/.zip — пропускаем
        ext = os.path.splitext(value.name)[1].lower()
        if ext not in IMAGE_EXTS:
            continue

        # сжимаем только если файл новый (только что загружен)
        if hasattr(value, "_committed") and not value._committed:
            new_file = compress_image(value)
            if new_file:
                setattr(instance, field.name, new_file)
