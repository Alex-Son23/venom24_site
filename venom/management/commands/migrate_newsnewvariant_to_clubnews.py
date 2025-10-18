from django.core.management.base import BaseCommand
from django.db import transaction
from venom.models import (
    Club,
    NewsNew,
    NewsNewVariant,
    CategorynewsNewVariant,
)


class Command(BaseCommand):
    help = "Перенос данных из NewsNewVariant в новую модель NewsNew"

    @transaction.atomic
    def handle(self, *args, **options):
        total = NewsNewVariant.objects.count()
        migrated = 0
        skipped = 0

        self.stdout.write(f"🔄 Начинаем миграцию {total} новостей...\n")

        # Словарь клубов для быстрого доступа
        clubs_by_slug = {c.slug.lower(): c for c in Club.objects.all()}
        self.stdout.write(f"🔗 Найдено клубов: {len(clubs_by_slug)}\n")

        for old_news in NewsNewVariant.objects.prefetch_related("catnews").all():
            categories = list(old_news.catnews.all())

            if not categories:
                skipped += 1
                self.stdout.write(f"⚠️  Пропущена новость без категорий: {old_news.title}")
                continue

            # Определяем клуб или главную страницу
            club = None
            is_main = False

            for cat in categories:
                slug = cat.slug.lower().strip()
                if slug in ["main", "glavnaya", "главная", "home"]:
                    is_main = True
                elif slug in clubs_by_slug:
                    club = clubs_by_slug[slug]

            # Создаём новую запись в NewsNew
            NewsNew.objects.update_or_create(
                slug=old_news.slug,
                defaults={
                    "club": club,
                    "is_main_page": is_main,
                    "title": old_news.title,
                    "photo": old_news.photo,
                    "photo_mobile": old_news.photo_mobile,
                    "short": old_news.short,
                    "descr": old_news.descr,
                    "sort": old_news.sort,
                    "time_create": old_news.time_create,
                    "time_update": old_news.time_update,
                    "is_published": old_news.is_published,
                },
            )

            migrated += 1
            if is_main:
                self.stdout.write(f"🌍 {old_news.title} → главная")
            elif club:
                self.stdout.write(f"🏙️ {old_news.title} → клуб {club.name}")
            else:
                self.stdout.write(f"⚠️ {old_news.title} без клуба/категории")

        self.stdout.write("\n📦 Миграция завершена")
        self.stdout.write(f"Всего найдено: {total}")
        self.stdout.write(f"Успешно перенесено: {migrated}")
        self.stdout.write(f"Пропущено без категорий: {skipped}")
        self.stdout.write(self.style.SUCCESS("🎉 Готово! Все новости перенесены в NewsNew."))
