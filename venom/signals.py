# signals.py
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db.models import FileField, ImageField
from .utils.images import compress_image  # твоя функция сжатия


@receiver(pre_save)
def compress_all_images(sender, instance, **kwargs):
    """
    Сжимаем только FileField / ImageField, не трогаем M2M, FK и прочее.
    """
    # у системных/абстрактных моделей может не быть _meta
    opts = getattr(instance, "_meta", None)
    if not opts:
        return

    # ВАЖНО: берём только реальные поля модели
    for field in opts.fields:
        # нас интересуют только file/image
        if not isinstance(field, (FileField, ImageField)):
            continue

        value = getattr(instance, field.name, None)
        # если файл только что загружен — он ещё не _committed
        if value and hasattr(value, "file") and not getattr(value, "_committed", True):
            new_file = compress_image(value)
            if new_file:
                setattr(instance, field.name, new_file)
