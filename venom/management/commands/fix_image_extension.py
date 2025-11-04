import os

from django.apps import apps
from django.core.management.base import BaseCommand
from django.db.models import FileField, ImageField


class Command(BaseCommand):
    help = "Меняет расширения у ссылок на изображения в БД (например .webp/.png/.jpeg -> .jpg) без вызова save()"

    IMAGE_EXTS = [".webp", ".png", ".jpeg", ".jpg"]
    OLD_EXTS = [".webp", ".png", ".jpeg"]
    NEW_EXT = ".jpg"

    def handle(self, *args, **options):
        total_checked = 0
        total_updated = 0

        for model in apps.get_models():
            # только поля-файлы
            file_fields = [
                f for f in model._meta.fields
                if isinstance(f, (FileField, ImageField))
            ]
            if not file_fields:
                continue

            qs = model.objects.all()
            for obj in qs.iterator():
                updates = {}
                for field in file_fields:
                    file_field = getattr(obj, field.name)
                    if not file_field:
                        continue

                    rel_path = file_field.name
                    if not rel_path:
                        continue

                    total_checked += 1

                    root, ext = os.path.splitext(rel_path)
                    ext_lower = ext.lower()

                    # трогаем только если это картинка
                    if ext_lower not in self.IMAGE_EXTS:
                        continue

                    # и если нужно заменить
                    if ext_lower in self.OLD_EXTS:
                        new_rel_path = root + self.NEW_EXT
                        updates[field.name] = new_rel_path
                        self.stdout.write(
                            self.style.SUCCESS(
                                f"[{model.__name__} #{obj.pk}] {rel_path} -> {new_rel_path}"
                            )
                        )

                if updates:
                    # обновляем напрямую в БД, чтобы не вызывался obj.save()
                    model.objects.filter(pk=obj.pk).update(**updates)
                    total_updated += 1

        self.stdout.write(self.style.SUCCESS(
            f"Готово. Проверено полей: {total_checked}, обновлено объектов: {total_updated}"
        ))
