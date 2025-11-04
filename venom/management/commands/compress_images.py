import os
from io import BytesIO

from django.conf import settings
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from PIL import Image


class Command(BaseCommand):
    help = "Сжать все изображения в MEDIA до <500Кб и привести к .jpg"

    IMG_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.webp')

    def handle(self, *args, **options):
        media_root = settings.MEDIA_ROOT
        max_size_kb = 500

        if not media_root or not os.path.isdir(media_root):
            self.stderr.write(self.style.ERROR("MEDIA_ROOT не найден или это не директория"))
            return

        for root, dirs, files in os.walk(media_root):
            for filename in files:
                if filename.lower().endswith(self.IMG_EXTENSIONS):
                    full_path = os.path.join(root, filename)
                    self.process_image(full_path, max_size_kb)

    def process_image(self, file_path: str, max_size_kb: int):
        try:
            # Открываем исходник
            img = Image.open(file_path)

            # JPEG не дружит с альфой, поэтому приводим к RGB
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")

            # Можно ограничить физический размер (на всякий случай)
            max_side = 2400
            if max(img.size) > max_side:
                img.thumbnail((max_side, max_side))

            # Сначала пробуем нормальное качество
            quality = 85

            buffer = BytesIO()
            img.save(buffer, format="JPEG", quality=quality, optimize=True)
            size_kb = buffer.getbuffer().nbytes / 1024

            # Если всё ещё больше 500Кб — понижаем качество
            while size_kb > max_size_kb and quality > 20:
                quality -= 5
                buffer = BytesIO()
                img.save(buffer, format="JPEG", quality=quality, optimize=True)
                size_kb = buffer.getbuffer().nbytes / 1024

            # Пишем обратно в тот же путь с .jpg
            new_path = file_path.rsplit('.', 1)[0] + '.jpg'
            with open(new_path, 'wb') as f:
                f.write(buffer.getvalue())

            # Если новое имя отличается от старого — можно удалить старый
            if new_path != file_path:
                os.remove(file_path)

            self.stdout.write(self.style.SUCCESS(f"OK: {new_path} ({size_kb:.0f} Кб, q={quality})"))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Ошибка {file_path}: {e}"))
