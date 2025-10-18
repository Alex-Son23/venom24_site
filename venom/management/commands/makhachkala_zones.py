import re
from django.core.management.base import BaseCommand
from django.db import transaction
from django.apps import apps

from venom.models import (
    Club,
    ClubZonesNew,
    ZonePriceBlock,
    ZonePriceItem,
    ZonesClubPics,
)

# старые модели: MahachkalaZoness, ZonesMahachkalaPics

class Command(BaseCommand):
    help = "Переносит игровые зоны клуба Махачкала в универсальные модели (ClubZonesNew/ZonePriceBlock/ZonePriceItem/ZonesClubPics)"

    @transaction.atomic
    def handle(self, *args, **options):
        # --- Клуб ---
        club, _ = Club.objects.get_or_create(slug="mahachkala", defaults={"name": "Махачкала"})
        self.stdout.write(self.style.SUCCESS(f"Клуб: {club.name}"))

        # Аккуратно получаем старые модели (если их нет — сообщим и выйдем)
        try:
            OldZone = apps.get_model("venom", "MahachkalaZoness")
        except LookupError:
            self.stderr.write("❌ Не найдена модель venom.MahachkalaZoness")
            return

        PicsModel = None
        try:
            PicsModel = apps.get_model("venom", "MahachkalaPicssMahachkalaPicss")
        except LookupError:
            self.stderr.write("⚠️ Не найдена модель venom.MahachkalaPicssMahachkalaPicss — переносим без фото.")

        migrated = 0

        for old in OldZone.objects.all():
            # 1) извлекаем кол-во ПК из названия (например «VIP 6ПК», «... 12 пк»)
            count = self._extract_pc_count(old.title)

            # 2) создаём/обновляем зону
            zone, _ = ClubZonesNew.objects.update_or_create(
                club=club,
                slug=old.slug,
                defaults={
                    "title": old.title,
                    "count": count,
                    "monitor": getattr(old, "monitor", ""),
                    "processor": getattr(old, "processor", ""),
                    "videocard": getattr(old, "videocard", ""),
                    "ozu": getattr(old, "ozu", ""),
                    "headset": getattr(old, "headset", ""),
                    "keyboard": getattr(old, "keyboard", ""),
                    "mouse": getattr(old, "mouse", ""),
                    "sort": getattr(old, "sort", ""),
                    "is_published": getattr(old, "is_published", True),
                },
            )

            # 3) очищаем старые блоки прайсов (чтобы не было дублей при повторном запуске)
            zone.price_blocks.all().delete()

            # 4) создаём блоки прайсов
            weekday_pairs = [
                (getattr(old, "timeone", ""),  getattr(old, "priceone", "")),
                (getattr(old, "timetwo", ""),  getattr(old, "prictwo", "")),
                (getattr(old, "timetri", ""),  getattr(old, "pricetri", "")),
                (getattr(old, "timefour", ""), getattr(old, "pricefour", "")),
                (getattr(old, "timefive", ""), getattr(old, "pricefive", "")),
                (getattr(old, "timesix", ""),  getattr(old, "pricesix", "")),
            ]
            self._create_price_block(zone, "ПН–ЧТ", weekday_pairs)

            weekend_pairs = [
                (getattr(old, "weekend_timeone", ""),  getattr(old, "weekend_priceone", "")),
                (getattr(old, "weekend_timetwo", ""),  getattr(old, "weekend_prictwo", "")),
                (getattr(old, "weekend_timetri", ""),  getattr(old, "weekend_pricetri", "")),
                (getattr(old, "weekend_timefour", ""), getattr(old, "weekend_pricefour", "")),
                (getattr(old, "weekend_timefive", ""), getattr(old, "weekend_pricefive", "")),
                (getattr(old, "weekend_timesix", ""),  getattr(old, "weekend_pricesix", "")),
            ]
            self._create_price_block(zone, "ПТ–ВС", weekend_pairs)

            # 5) переносим фото
            if PicsModel:
                pics = PicsModel.objects.filter(zone=old)
                for order, pic in enumerate(pics, start=1):
                    ZonesClubPics.objects.create(
                        club=club,
                        zone=zone,
                        photo=pic.photo,
                        photo_mobile=getattr(pic, "photo_mobile", None),
                        sort=order,
                        is_published=getattr(pic, "is_published", True),
                    )

            migrated += 1
            self.stdout.write(f"✅ Зона перенесена: {zone.title} (ПК: {count or '-'})")

        self.stdout.write(self.style.SUCCESS(f"\n🎉 Готово! Перенесено зон: {migrated}"))

    # ---------- helpers ----------
    def _extract_pc_count(self, title: str):
        """
        Ищем «<число> пк/ПК» в конце/внутри строки.
        Примеры: 'VIP 6ПК', 'COMFORT 27` 240HZ 32пк'
        """
        m = re.search(r"(\d+)\s*пк", title, flags=re.IGNORECASE)
        return int(m.group(1)) if m else None

    def _create_price_block(self, zone, title: str, pairs: list[tuple[str, str]]):
        """Создаёт блок прайса с элементами; пропускает, если всё пусто."""
        if not any((t or p) for t, p in pairs):
            return None
        block = ZonePriceBlock.objects.create(zone=zone, title=title, is_visible=True)
        for i, (t, p) in enumerate(pairs, start=1):
            if t or p:
                ZonePriceItem.objects.create(block=block, time=t or "", price=p or "", order=i)
        return block
