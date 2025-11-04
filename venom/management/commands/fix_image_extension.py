import os

from django.apps import apps
from django.core.management.base import BaseCommand
from django.db.models import FileField, ImageField


class Command(BaseCommand):
    help = "Меняет расширения у ССЫЛОК на изображения в БД (например .webp/.png/.jpeg -> .jpg)"

    # что считаем именно изображениями (по расширению)
    IMAGE_EXTS = [".webp", ".png", ".jpeg", ".jpg"]
    # что будем заменять
    OLD_EXTS = [".webp", ".png", ".jpeg"]
    # на что меняем
    NEW_EXT = ".jpg"

    def handle(self, *args, **options):
        total_checked = 0
        total_updated = 0

        for model in apps.get_models():
            # берём только обычные поля модели
            file_fields = [
                f for f in model._meta.fields
                if isinstance(f, (FileField, ImageField))
            ]
            if not file_fields:
                continue

            qs = model.objects.all()
            for obj in qs.iterator():
                changed = False

                for field in file_fields:
                    field_file = getattr(obj, field.name)
                    if not field_file:
                        continue

                    rel_path = field_file.name
                    if not rel_path:
                        continue

                    total_checked += 1

                    root, ext = os.path.splitext(rel_path)
                    ext_lower = ext.lower()

                    # трогаем только если это вообще похоже на изображение
                    if ext_lower not in self.IMAGE_EXTS:
                        continue

                    # и только если это одно из расширений, которое надо сменить
                    if ext_lower in self.OLD_EXTS:
                        new_rel_path = root + self.NEW_EXT
                        setattr(obj, field.name, new_rel_path)
                        changed = True
                        self.stdout.write(
                            self.style.SUCCESS(
                                f"[{model.__name__} #{obj.pk}] {rel_path} -> {new_rel_path}"
                            )
                        )

                if changed:
                    obj.save()
                    total_updated += 1

        self.stdout.write(self.style.SUCCESS(
            f"Готово. Проверено полей: {total_checked}, обновлено объектов: {total_updated}"
        ))
