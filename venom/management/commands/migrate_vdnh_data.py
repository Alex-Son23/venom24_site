from django.core.management.base import BaseCommand
from venom.models import (
    Club, ClubNews, ClubPromo, ClubZonesNew,
    ClubGallery, PhotoClub, ClubSeo
)

# импортируем старые модели
from venom.models import (
    VdnhNews, VdnhPromo, VdnhZonesNew,
    VdnhGallery, PhotoVdnx, VdnhSeo
)


class Command(BaseCommand):
    help = "Миграция данных из старых моделей ВДНХ в общие модели Club*"

    def handle(self, *args, **options):
        # 1️⃣ Создаем или находим клуб
        club, created = Club.objects.get_or_create(
            slug="vdnh",
            defaults={"name": "ВДНХ"}
        )
        self.stdout.write(self.style.SUCCESS(f"Используется клуб: {club.name}"))

        # 2️⃣ SEO
        seo_old = VdnhSeo.objects.last()
        if seo_old:
            ClubSeo.objects.update_or_create(
                club=club,
                defaults={
                    "title": seo_old.title,
                    "description": seo_old.description,
                    "keywords": seo_old.keywords
                }
            )
            self.stdout.write("✅ SEO перенесено")

        # 3️⃣ Новости
        for item in VdnhNews.objects.all():
            ClubNews.objects.update_or_create(
                club=club,
                slug=item.slug,
                defaults={
                    "title": item.title,
                    "photo": item.photo,
                    "photo_mobile": item.photo_mobile,
                    "short": item.short,
                    "descr": item.descr,
                    "sort": int(item.sort or 0),
                    "time_create": item.time_create,
                    "time_update": item.time_update,
                    "is_published": item.is_published,
                }
            )
        self.stdout.write(f"✅ Новости: {VdnhNews.objects.count()} шт.")

        # 4️⃣ Акции
        for item in VdnhPromo.objects.all():
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
                    "time_create": item.time_create,
                    "time_update": item.time_update,
                    "is_published": item.is_published,
                }
            )
        self.stdout.write(f"✅ Акции: {VdnhPromo.objects.count()} шт.")

        # 5️⃣ Галерея
        for g in VdnhGallery.objects.all():
            ClubGallery.objects.create(
                club=club,
                photo=g.photo,
                photo_mobile=g.photo_mobile,
                is_published=g.is_published
            )
        self.stdout.write(f"✅ Галерея: {VdnhGallery.objects.count()} шт.")

        # 6️⃣ Фотографии (верхняя галерея)
        for p in PhotoVdnx.objects.all():
            PhotoClub.objects.create(
                club=club,
                photo=p.photo,
                photo_mobile=p.photo_mobile,
                order=p.order
            )
        self.stdout.write(f"✅ Фото верхней галереи: {PhotoVdnx.objects.count()} шт.")

        # 7️⃣ Зоны (и их картинки)
        for z in VdnhZonesNew.objects.all():
            zone_new, _ = ClubZonesNew.objects.update_or_create(
                club=club,
                slug=z.slug,
                defaults={
                    "title": z.title,

                    # --- Оборудование ---
                    "monitor_tile": z.monitor_tile,
                    "monitor": z.monitor,
                    "processor_tile": z.processor_tile,
                    "processor": z.processor,
                    "videocard_tile": z.videocard_tile,
                    "videocard": z.videocard,
                    "ozu_tile": z.ozu_tile,
                    "ozu": z.ozu,
                    "headset_tile": z.headset_tile,
                    "headset": z.headset,
                    "keyboard_tile": z.keyboard_tile,
                    "keyboard": z.keyboard,
                    "mouse_tile": z.mouse_tile,
                    "mouse": z.mouse,

                    # --- ПН–ЧТ ---
                    "timeone": z.timeone,
                    "priceone": z.priceone,
                    "timetwo": z.timetwo,
                    "prictwo": z.prictwo,
                    "timetri": z.timetri,
                    "pricetri": z.pricetri,
                    "timefour": z.timefour,
                    "pricefour": z.pricefour,
                    "timefive": z.timefive,
                    "pricefive": z.pricefive,
                    "timesix": z.timesix,
                    "pricesix": z.pricesix,

                    # --- ПТ–ВС ---
                    "weekend_timeone": z.weekend_timeone,
                    "weekend_priceone": z.weekend_priceone,
                    "weekend_timetwo": z.weekend_timetwo,
                    "weekend_prictwo": z.weekend_prictwo,
                    "weekend_timetri": z.weekend_timetri,
                    "weekend_pricetri": z.weekend_pricetri,
                    "weekend_timefour": z.weekend_timefour,
                    "weekend_pricefour": z.weekend_pricefour,
                    "weekend_timefive": z.weekend_timefive,
                    "weekend_pricefive": z.weekend_pricefive,
                    "weekend_timesix": z.weekend_timesix,
                    "weekend_pricesix": z.weekend_pricesix,

                    # --- Служебные поля ---
                    "sort": z.sort,
                    "time_create": z.time_create,
                    "time_update": z.time_update,
                    "is_published": z.is_published,
                }
            )

            # --- переносим связанные картинки зоны ---
            for pic in getattr(z, "zone_pics", []).all():
                zone_new.zone_pics.create(
                    club=club,
                    photo=pic.photo,
                    photo_mobile=pic.photo_mobile,
                    sort=int(pic.sort or 0),
                    is_published=pic.is_published,
                )

        print(f"✅ Зоны клуба {club.name} перенесены ({VdnhZonesNew.objects.count()} шт.)")
        self.stdout.write(self.style.SUCCESS("🎉 Перенос данных для ВДНХ завершен!"))
