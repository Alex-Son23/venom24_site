import re
from django.core.management.base import BaseCommand
from django.db import transaction
from venom.models import (
    Club,
    ClubZonesNew,
    ZonePriceBlock,
    ZonePriceItem,
    ZonesClubPics,
    VernadkaZonesNew,
    ZonesVernadkaPics,
)


class Command(BaseCommand):
    help = "Переносит игровые зоны клуба Вернадского в универсальные модели ClubZonesNew / ZonePriceBlock / ZonePriceItem / ZonesClubPics"

    @transaction.atomic
    def handle(self, *args, **options):
        # --- Находим или создаем клуб ---
        club, _ = Club.objects.get_or_create(
            slug="vernadka",
            defaults={"name": "Вернадского"},
        )
        self.stdout.write(self.style.SUCCESS(f"Используется клуб: {club.name}"))

        migrated = 0

        # --- Основной цикл по старым зонам ---
        for old_zone in VernadkaZonesNew.objects.all():
            # Извлекаем количество ПК из названия (например: "BOOTCAMP 6ПК")
            count_match = re.search(r"(\d+)\s*пк", old_zone.title.lower())
            count = int(count_match.group(1)) if count_match else None

            # --- Создаем новую зону ---
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

            # Удаляем старые блоки прайсов перед созданием
            zone.price_blocks.all().delete()

            # --- Создаем блоки прайсов ---
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

            # --- Переносим фото зоны ---
            self.migrate_zone_pics(old_zone, zone, club)

            migrated += 1
            self.stdout.write(f"✅ Зона перенесена: {zone.title} (ПК: {count or '-'})")

        self.stdout.write(self.style.SUCCESS(f"\n🎉 Перенос завершен! Всего зон: {migrated}"))

    # --- Создание блока прайса и его элементов ---
    def create_price_block(self, zone, title, pairs):
        """Создает блок прайса и его элементы"""
        if not any(t or p for t, p in pairs):
            return None

        block = ZonePriceBlock.objects.create(zone=zone, title=title, is_visible=True)
        for order, (time, price) in enumerate(pairs, start=1):
            if time or price:
                ZonePriceItem.objects.create(block=block, time=time or "", price=price or "", order=order)
        return block

    # --- Перенос фото зоны ---
    def migrate_zone_pics(self, old_zone, new_zone, club):
        """Перенос изображений зоны"""
        pics = ZonesVernadkaPics.objects.filter(zone=old_zone)
        for order, pic in enumerate(pics, start=1):
            ZonesClubPics.objects.create(
                club=club,
                zone=new_zone,
                photo=pic.photo,
                photo_mobile=pic.photo_mobile,
                sort=order,
                is_published=pic.is_published,
            )
