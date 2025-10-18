# import re
# from django.core.management.base import BaseCommand
# from django.db import transaction
# from venom.models import (
#     Club,
#     ClubZonesNew,
#     ZonePriceBlock,
#     ZonePriceItem,
#     ZonesClubPics,
#     VdnhZonesNew,
#     ZonesVdnhPics,
# )


# class Command(BaseCommand):
#     help = "Переносит зоны ВДНХ в универсальные модели ClubZonesNew / ZonePriceBlock / ZonePriceItem / ZonesClubPics"

#     @transaction.atomic
#     def handle(self, *args, **options):
#         club, _ = Club.objects.get_or_create(
#             slug="vdnh",
#             defaults={"name": "ВДНХ"},
#         )
#         self.stdout.write(self.style.SUCCESS(f"Используется клуб: {club.name}"))

#         migrated = 0

#         for old_zone in VdnhZonesNew.objects.all():
#             # --- Извлекаем количество ПК из названия ---
#             count_match = re.search(r"(\d+)\s*пк", old_zone.title.lower())
#             count = int(count_match.group(1)) if count_match else None

#             # --- Создаём новую зону ---
#             zone, _ = ClubZonesNew.objects.update_or_create(
#                 club=club,
#                 slug=old_zone.slug,
#                 defaults={
#                     "title": old_zone.title,
#                     "count": count,
#                     "monitor": old_zone.monitor,
#                     "processor": old_zone.processor,
#                     "videocard": old_zone.videocard,
#                     "ozu": old_zone.ozu,
#                     "headset": old_zone.headset,
#                     "keyboard": old_zone.keyboard,
#                     "mouse": old_zone.mouse,
#                     "sort": old_zone.sort,
#                     "is_published": old_zone.is_published,
#                 },
#             )

#             # --- Удаляем старые прайсы перед созданием ---
#             zone.price_blocks.all().delete()

#             # --- Прайс (ПН–ЧТ) ---
#             weekday_pairs = [
#                 (old_zone.timeone, old_zone.priceone),
#                 (old_zone.timetwo, old_zone.prictwo),
#                 (old_zone.timetri, old_zone.pricetri),
#                 (old_zone.timefour, old_zone.pricefour),
#                 (old_zone.timefive, old_zone.pricefive),
#                 (old_zone.timesix, old_zone.pricesix),
#             ]
#             weekday_block = self.create_price_block(zone, "ПН–ЧТ", weekday_pairs)

#             # --- Прайс (ПТ–ВС) ---
#             weekend_pairs = [
#                 (old_zone.weekend_timeone, old_zone.weekend_priceone),
#                 (old_zone.weekend_timetwo, old_zone.weekend_prictwo),
#                 (old_zone.weekend_timetri, old_zone.weekend_pricetri),
#                 (old_zone.weekend_timefour, old_zone.weekend_pricefour),
#                 (old_zone.weekend_timefive, old_zone.weekend_pricefive),
#                 (old_zone.weekend_timesix, old_zone.weekend_pricesix),
#             ]
#             weekend_block = self.create_price_block(zone, "ПТ–ВС", weekend_pairs)

#             # --- Фото зоны ---
#             self.migrate_zone_pics(old_zone, zone, club)

#             migrated += 1
#             self.stdout.write(f"✅ {zone.title} (ПК: {count or '-'}), блоков: "
#                               f"{int(bool(weekday_block)) + int(bool(weekend_block))}")

#         self.stdout.write(self.style.SUCCESS(f"\n🎉 Перенос завершён! Всего зон: {migrated}"))

#     def create_price_block(self, zone, title, pairs):
#         """Создание блока прайса и его элементов"""
#         if not any(t or p for t, p in pairs):
#             return None

#         block = ZonePriceBlock.objects.create(zone=zone, title=title, is_visible=True)
#         for i, (time, price) in enumerate(pairs, start=1):
#             if time or price:
#                 ZonePriceItem.objects.create(block=block, time=time or "", price=price or "", order=i)
#         return block

#     def migrate_zone_pics(self, old_zone, new_zone, club):
#         """Перенос фото зоны"""
#         pics = ZonesVdnhPics.objects.filter(zone=old_zone)
#         for order, pic in enumerate(pics, start=1):
#             ZonesClubPics.objects.create(
#                 club=club,
#                 zone=new_zone,
#                 photo=pic.photo,
#                 photo_mobile=pic.photo_mobile,
#                 sort=order,
#                 is_published=pic.is_published,
#             )

import re
from django.core.management.base import BaseCommand
from django.db import transaction
from venom.models import (
    Club,
    ClubZonesNew,
    ZonePriceBlock,
    ZonePriceItem,
    ZonesClubPics,
    MitinoZones,
)


class Command(BaseCommand):
    help = "Переносит игровые зоны клуба Митино в универсальные модели ClubZonesNew / ZonePriceBlock / ZonePriceItem / ZonesClubPics"

    @transaction.atomic
    def handle(self, *args, **options):
        # --- Клуб ---
        club, _ = Club.objects.get_or_create(
            slug="mitino",
            defaults={"name": "Митино"},
        )
        self.stdout.write(self.style.SUCCESS(f"Используется клуб: {club.name}"))

        migrated = 0

        # --- Основной цикл по старым зонам ---
        for old_zone in MitinoZones.objects.all():
            # Извлекаем количество ПК из названия (например: "VIP 6ПК")
            count_match = re.search(r"(\d+)\s*пк", old_zone.title.lower())
            count = int(count_match.group(1)) if count_match else None

            # --- Создаём новую зону ---
            zone, _ = ClubZonesNew.objects.update_or_create(
                club=club,
                slug=old_zone.slug,
                defaults={
                    "title": old_zone.title,
                    "count": count,
                    "monitor": old_zone.monitor,
                    "processor": old_zone.processor,
                    "videocard": old_zone.videocard,
                    "ozu": old_zone.ozu,
                    "headset": old_zone.headset,
                    "keyboard": old_zone.keyboard,
                    "mouse": old_zone.mouse,
                    "sort": old_zone.sort,
                    "is_published": old_zone.is_published,
                },
            )

            # Удаляем старые блоки прайса перед созданием
            zone.price_blocks.all().delete()

            # --- Создаём блоки прайсов ---
            weekday_pairs = [
                (old_zone.timeone, old_zone.priceone),
                (old_zone.timetwo, old_zone.prictwo),
                (old_zone.timetri, old_zone.pricetri),
                (old_zone.timefour, old_zone.pricefour),
                (old_zone.timefive, old_zone.pricefive),
                (old_zone.timesix, old_zone.pricesix),
            ]
            self.create_price_block(zone, "ПН–ЧТ", weekday_pairs)

            weekend_pairs = [
                (old_zone.weekend_timeone, old_zone.weekend_priceone),
                (old_zone.weekend_timetwo, old_zone.weekend_prictwo),
                (old_zone.weekend_timetri, old_zone.weekend_pricetri),
                (old_zone.weekend_timefour, old_zone.weekend_pricefour),
                (old_zone.weekend_timefive, old_zone.weekend_pricefive),
                (old_zone.weekend_timesix, old_zone.weekend_pricesix),
            ]
            self.create_price_block(zone, "ПТ–ВС", weekend_pairs)

            # --- Добавляем изображения зоны ---
            if getattr(old_zone, "photo", None):
                ZonesClubPics.objects.update_or_create(
                    club=club,
                    zone=zone,
                    sort=1,
                    defaults={
                        "photo": old_zone.photo,
                        "photo_mobile": getattr(old_zone, "photo_mobile", None),
                        "is_published": True,
                    },
                )

            migrated += 1
            self.stdout.write(f"✅ Зона перенесена: {zone.title} (ПК: {count or '-'})")

        self.stdout.write(self.style.SUCCESS(f"\n🎉 Перенос завершён! Всего зон: {migrated}"))

    # --- Вспомогательная функция для блоков прайсов ---
    def create_price_block(self, zone, title, pairs):
        """Создание блока прайса и его элементов"""
        if not any(t or p for t, p in pairs):
            return None

        block = ZonePriceBlock.objects.create(zone=zone, title=title, is_visible=True)
        for order, (time, price) in enumerate(pairs, start=1):
            if time or price:
                ZonePriceItem.objects.create(block=block, time=time or "", price=price or "", order=order)
        return block
