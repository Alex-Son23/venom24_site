import os
import re
from io import BytesIO
from PIL import Image
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.apps import apps
from django.db import transaction
from venom.models import (
    Club,
    ClubNews,
    ClubPromo,
    ClubSeo,
    ClubGallery,
    PhotoClub,
    ClubZonesNew,
    ZonePriceBlock,
    ZonePriceItem,
    ZonesClubPics,
    ClubPageImages,  # новая модель
    NewsNew
)

# соответствие клубов и старых моделей
CLUB_MODEL_MAP = {
    "serpuhovskaya": {
        "name": "Серпуховская",
        "seo": "SerpuhovkayaSeo",
        "news": "SerpuhovskayaNews",
        "promo": "SerpuhovskayaPromo",
        "gallery": "SerpuhovskayaGallery",
        "photos": "PhotoSerpuhskaya",
        "zones": "SerpuhovskayaZonesNew",
        "zone_pics": "ZonesSerpuhovskayaPics",
    },
    "koptevo": {
        "name": "Коптево",
        "seo": "KoptevoSeo",
        "news": "KoptevoNews",
        "promo": "KoptevoPromo",
        "gallery": "KoptevoGallery",
        "photos": "PhotoKoptevo",
        "zones": "KoptevoZones",
        "zone_pics": "",
    },
    "zhulebino": {
        "name": "Жулебино",
        "seo": "ZulebinoSeo",
        "news": "ZulebinoNews",
        "promo": "ZulebinoPromo",
        "gallery": "ZulebinoGallery",
        "photos": "PhotoZhulebino",
        "zones": "ZulebinoZones",
        "zone_pics": "",
    },
    "zhukovsky": {
        "name": "Жуковский",
        "seo": "ZukovskySeo",
        "news": "ZukovskyNews",
        "promo": "ZukovskyPromo",
        "gallery": "ZukovskyGallery",
        "photos": "PhotoZhukovsky",
        "zones": "ZukovskyZones",
        "zone_pics": "",
    },
    "pushkino": {
        "name": "Пушкино",
        "seo": "PushkinoSeo",
        "news": "PushkinoNews",
        "promo": "PushkinoPromo",
        "gallery": "PushkinoGallery",
        "photos": "PhotoPushkino",
        "zones": "PushkinoZones",
        "zone_pics": "",
    },
}


class Command(BaseCommand):
    help = "Перенос данных всех клубов (SEO, новости, акции, галереи, зоны, изображения клубов) в новые модели Club*"

    def add_arguments(self, parser):
        parser.add_argument("--club", type=str, help="Slug клуба (например: koptevo, vdnh)")

    @transaction.atomic
    def handle(self, *args, **options):
        club_arg = options.get("club")
        if club_arg:
            clubs = {club_arg: CLUB_MODEL_MAP.get(club_arg)}
            if not clubs[club_arg]:
                self.stderr.write(f"❌ Неизвестный клуб: {club_arg}")
                return
        else:
            clubs = CLUB_MODEL_MAP

        for slug, models_map in clubs.items():
            self.migrate_one_club(slug, models_map)

        self.migrate_club_page_images()

    def migrate_one_club(self, slug, models_map):
        self.stdout.write(self.style.MIGRATE_HEADING(f"\n=== 📍 Перенос клуба: {slug.upper()} ==="))
        club, _ = Club.objects.get_or_create(slug=slug, defaults={"name": models_map["name"]})

        def safe_model(name):
            try:
                return apps.get_model("venom", name)
            except LookupError:
                return None

        SeoModel = safe_model(models_map.get("seo"))
        NewsModel = safe_model(models_map.get("news"))
        PromoModel = safe_model(models_map.get("promo"))
        GalleryModel = safe_model(models_map.get("gallery"))
        PhotosModel = safe_model(models_map.get("photos"))
        ZonesModel = safe_model(models_map.get("zones"))
        ZonesPicsModel = safe_model(models_map.get("zone_pics"))

        # --- SEO ---
        if SeoModel:
            seo = SeoModel.objects.last()
            if seo:
                ClubSeo.objects.update_or_create(
                    club=club,
                    defaults={"title": seo.title, "description": seo.description, "keywords": seo.keywords},
                )
                self.stdout.write("✅ SEO перенесено")

        # --- Новости ---
        if NewsModel:
            for item in NewsModel.objects.all():
                slug = item.slug

                # Проверяем, не занят ли slug другой новостью
                if NewsNew.objects.filter(slug=slug).exclude(club=club).exists():
                    # если уже есть, то добавляем префикс клуба
                    slug = f"{slug}-{club.slug}"

                NewsNew.objects.update_or_create(
                    club=club,
                    slug=slug,
                    defaults={
                        "title": item.title,
                        "photo": item.photo,
                        "photo_mobile": item.photo_mobile,
                        "short": item.short,
                        "descr": item.descr,
                        "sort": int(item.sort or 0),
                        "is_published": item.is_published,
                    },
                )
            self.stdout.write(f"✅ Новости: {NewsModel.objects.count()} шт.")
        # --- Акции ---
        if PromoModel:
            for item in PromoModel.objects.all():
                ClubPromo.objects.update_or_create(
                    club=club,
                    slug=item.slug,
                    defaults={
                        "title": item.title,
                        "photo": item.photo,
                        "photo_mobile": item.photo_mobile,
                        "short": item.short,
                        "descr": item.descr,
                        "sort": int(item.sort or 0),
                        "is_published": item.is_published,
                    },
                )
            self.stdout.write(f"✅ Акции: {PromoModel.objects.count()} шт.")

        # --- Галерея ---
        if GalleryModel:
            for g in GalleryModel.objects.all():
                ClubGallery.objects.create(club=club, photo=g.photo, photo_mobile=g.photo_mobile)
            self.stdout.write(f"✅ Галерея: {GalleryModel.objects.count()} шт.")

        # --- Фото клуба ---
        if PhotosModel:
            for p in PhotosModel.objects.all():
                PhotoClub.objects.create(club=club, photo=p.photo, photo_mobile=p.photo_mobile, order=p.order)
            self.stdout.write(f"✅ Фото верхней галереи: {PhotosModel.objects.count()} шт.")

        # --- Зоны ---
        if ZonesModel:
            for old_zone in ZonesModel.objects.all():
                count = self._extract_pc_count(old_zone.title)
                clean_title = re.sub(r"\s*\d+\s*пк", "", old_zone.title, flags=re.IGNORECASE).strip()

                zone, _ = ClubZonesNew.objects.update_or_create(
                    club=club,
                    slug=old_zone.slug,
                    defaults={
                        "title": clean_title,
                        "count": count,
                        "monitor": getattr(old_zone, "monitor", ""),
                        "processor": getattr(old_zone, "processor", ""),
                        "videocard": getattr(old_zone, "videocard", ""),
                        "ozu": getattr(old_zone, "ozu", ""),
                        "headset": getattr(old_zone, "headset", ""),
                        "keyboard": getattr(old_zone, "keyboard", ""),
                        "mouse": getattr(old_zone, "mouse", ""),
                        "sort": getattr(old_zone, "sort", ""),
                        "is_published": getattr(old_zone, "is_published", True),
                    },
                )

                # --- переносим фото ---
                if ZonesPicsModel:
                    self._migrate_zone_pics(ZonesPicsModel, old_zone, zone, club)
                else:
                    # ⚙️ если фото в самой модели зоны
                    if getattr(old_zone, "photo", None):
                        ZonesClubPics.objects.create(
                            club=club,
                            zone=zone,
                            photo=old_zone.photo,
                            photo_mobile=getattr(old_zone, "photo_mobile", None),
                            is_published=True,
                        )

                # --- создаем прайсы ---
                self._create_price_blocks(zone, old_zone)

            self.stdout.write(f"✅ Зоны клуба {club.name} перенесены ({ZonesModel.objects.count()} шт.)")

        self.stdout.write(self.style.SUCCESS(f"🎉 Клуб {club.name} успешно перенесён!"))

    def migrate_club_page_images(self):
        OldModel = apps.get_model("venom", "ClubPageZonesImages")
        if not OldModel:
            return

        count = 0
        for old in OldModel.objects.all():
            club = Club.objects.filter(name__iexact=old.type).first()
            if not club:
                continue

            ClubPageImages.objects.update_or_create(
                club=club,
                defaults={"image": old.image, "image_mobile": old.image_mobile},
            )
            count += 1
        self.stdout.write(self.style.SUCCESS(f"✅ Перенесено изображений клубов: {count}"))

    # === helpers ===
    def _extract_pc_count(self, title):
        match = re.search(r"(\d+)\s*пк", title.lower())
        return int(match.group(1)) if match else None

    def _create_price_blocks(self, zone, old_zone):
        weekday_pairs = [
            (getattr(old_zone, "timeone", ""), getattr(old_zone, "priceone", "")),
            (getattr(old_zone, "timetwo", ""), getattr(old_zone, "prictwo", "")),
            (getattr(old_zone, "timetri", ""), getattr(old_zone, "pricetri", "")),
            (getattr(old_zone, "timefour", ""), getattr(old_zone, "pricefour", "")),
            (getattr(old_zone, "timefive", ""), getattr(old_zone, "pricefive", "")),
            (getattr(old_zone, "timesix", ""), getattr(old_zone, "pricesix", "")),
        ]
        weekend_pairs = [
            (getattr(old_zone, "weekend_timeone", ""), getattr(old_zone, "weekend_priceone", "")),
            (getattr(old_zone, "weekend_timetwo", ""), getattr(old_zone, "weekend_prictwo", "")),
            (getattr(old_zone, "weekend_timetri", ""), getattr(old_zone, "weekend_pricetri", "")),
            (getattr(old_zone, "weekend_timefour", ""), getattr(old_zone, "weekend_pricefour", "")),
            (getattr(old_zone, "weekend_timefive", ""), getattr(old_zone, "weekend_pricefive", "")),
            (getattr(old_zone, "weekend_timesix", ""), getattr(old_zone, "weekend_pricesix", "")),
        ]

        if any(t or p for t, p in weekday_pairs):
            block = ZonePriceBlock.objects.create(zone=zone, title="ПН–ЧТ", is_visible=True)
            for order, (t, p) in enumerate(weekday_pairs, start=1):
                if t or p:
                    ZonePriceItem.objects.create(block=block, time=t, price=p, order=order)

        if any(t or p for t, p in weekend_pairs):
            block = ZonePriceBlock.objects.create(zone=zone, title="ПТ–ВС", is_visible=True)
            for order, (t, p) in enumerate(weekend_pairs, start=1):
                if t or p:
                    ZonePriceItem.objects.create(block=block, time=t, price=p, order=order)

    def _migrate_zone_pics(self, PicsModel, old_zone, new_zone, club):
        pics = PicsModel.objects.filter(zone=old_zone)
        for order, pic in enumerate(pics, start=1):
            ZonesClubPics.objects.create(
                club=club,
                zone=new_zone,
                photo=pic.photo,
                photo_mobile=getattr(pic, "photo_mobile", None),
                sort=order,
                is_published=getattr(pic, "is_published", True),
            )