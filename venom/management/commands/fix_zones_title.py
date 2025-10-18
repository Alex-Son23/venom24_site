import re
from django.core.management.base import BaseCommand
from venom.models import ClubZonesNew


class Command(BaseCommand):
    help = "Извлекает количество ПК из названия зоны и сохраняет в поле count"

    def handle(self, *args, **options):
        pattern = re.compile(r'(\d+)\s*пк', re.IGNORECASE)
        updated = 0

        for zone in ClubZonesNew.objects.all():
            title = zone.title.strip()
            match = pattern.search(title)

            if match:
                count = int(match.group(1))
                # удаляем "5ПК" из названия
                new_title = pattern.sub('', title).strip()
                new_title = re.sub(r'\s{2,}', ' ', new_title)  # убираем двойные пробелы

                zone.count = count
                zone.title = new_title
                zone.save(update_fields=["count", "title"])
                updated += 1
                self.stdout.write(f"✅ {zone.club.name}: «{title}» → «{new_title}» ({count} ПК)")

        self.stdout.write(self.style.SUCCESS(f"\n🎉 Обновлено {updated} записей!"))
