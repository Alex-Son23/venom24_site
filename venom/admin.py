from django import forms
from django.contrib import admin
from django.forms import SelectMultiple
from django.urls import reverse
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from ckeditor.widgets import CKEditorWidget
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import *

class PhotoVenumAdmin(admin.ModelAdmin):
    def gphoto(self, object):
        return mark_safe(f"<img src='{object.photo.url}' width=120>")
    list_display = ('id', 'gphoto', 'order')
    list_display_links = ('id', 'gphoto', 'order')
    
    gphoto.short_description = 'Картинка'

    
admin.site.register(PhotoVenum,PhotoVenumAdmin)

class AdminTournament(admin.ModelAdmin):
    def gphoto(self, object):
        return mark_safe(f"<img src='{object.photo.url}' width=120>")
    list_display = ('id', 'gphoto', 'order')
    list_display_links = ('id', 'gphoto', 'order')
    gphoto.short_description = 'Картинка'
admin.site.register(Tournament, AdminTournament)

class ClubPageZonesImagesAdmin(admin.ModelAdmin):
    def gphoto(self, object):
        return mark_safe(f"<img src='{object.image.url}' width=120>")
    list_display = ('id', 'type', 'gphoto')
    list_display_links = ('id', 'type', 'gphoto')
    
    gphoto.short_description = 'Картинка'
    
admin.site.register(ClubPageZonesImages, ClubPageZonesImagesAdmin)

class CharacteristicsInline(admin.TabularInline):
    model = Characteristics
    extra = 1

@admin.register(ZonePlay)
class ZonePlayAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_display_links = ('name', 'order')
    inlines = [CharacteristicsInline]  # Используйте список классов, а не строк







class PromoPageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'short', 'get_html_photo', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'title', 'short', )
    search_fields = ('id', 'title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title', )}
    fields = ('title', 'slug', 'short', 'descr', 'photo', 'get_html_photo', 'photo_mobile', 'get_html_mobilephoto', 'time_create', 'time_update',  'is_published')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo', 'get_html_mobilephoto')
    save_on_top = True

    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }


    def get_html_photo(self, object):
        return mark_safe(f"<img src='{object.photo.url}' width=120>")

    def get_html_mobilephoto(self, object):
        return mark_safe(f"<img src='{object.photo_mobile.url}' width=120>")

    get_html_photo.short_description = 'Картинка'
    get_html_mobilephoto.short_description = 'Картинка для мобильных устройств'




class NewsAdminForm(forms.ModelForm):

    class Meta:
        model = News
        fields = '__all__'
        widgets = {
            'catnews': SelectMultiple(attrs={'size': 10})
        }

class NewsAdmin(admin.ModelAdmin):

    form = NewsAdminForm
    list_display = ('id', 'title', 'short', 'get_html_photo', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'title', 'short',)
    search_fields = ('title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    readonly_fields = ('time_create', 'time_update')
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True

    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }

    def get_html_photo(self, object):
        return mark_safe(f"<img src='{object.photo.url}' width=120>")

    get_html_photo.short_description = 'Картинка'


class CategorynewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)
    prepopulated_fields = {'slug': ('name', )}
    save_on_top = True








#################### news new variant
# @admin.register(NewsNewVariant)
class NewsNewVariantAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'sort', 'get_categories', 'time_create', 'is_published')
    list_display_links = ('id', 'title')
    list_filter = ('is_published', 'time_create')
    search_fields = ('title', 'descr')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('time_create', 'time_update')
    save_on_top = True

    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }

    def get_categories(self, obj):
        return ", ".join(
            [category.name for category in obj.catnews.all()])  # Получаем все категории и объединяем их через запятую

    get_categories.short_description = 'Категории'  # Название колонки в админке

# @admin.register(CategorynewsNewVariant)
class CategorynewsNewVariantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    save_on_top = True


class HomePageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'keywords')
    list_display_links = ('id', 'title', 'description',)
    search_fields = ('id', 'title',)
    fields = ('title', 'description', 'keywords')


class ClubPageSeoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'keywords')
    list_display_links = ('id', 'title', 'description',)
    search_fields = ('id', 'title',)
    fields = ('title', 'description', 'keywords')



class PromoPageSeoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'keywords')
    list_display_links = ('id', 'title', 'description',)
    search_fields = ('id', 'title',)
    fields = ('title', 'description', 'keywords')


class FranchisePageSeoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'keywords')
    list_display_links = ('id', 'title', 'description',)
    search_fields = ('id', 'title',)
    fields = ('title', 'description', 'keywords')


class ContactPageSeoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'keywords')
    list_display_links = ('id', 'title', 'description',)
    search_fields = ('id', 'title',)
    fields = ('title', 'description', 'keywords')


class HomeGalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_html_photo', 'is_published',)
    list_display_links = ('id', 'get_html_photo', )
    search_fields = ('id', )
    list_editable = ('is_published',)
    list_filter = ('is_published', )
    fields = ('photo', 'get_html_photo', 'photo_mobile', 'get_html_mobilephoto', 'is_published',)
    readonly_fields = ('get_html_photo', 'get_html_mobilephoto',)
    save_on_top = True

    def get_html_photo(self, object):
        return mark_safe(f"<img src='{object.photo.url}' width=120>")

    def get_html_mobilephoto(self, object):
        return mark_safe(f"<img src='{object.photo_mobile.url}' width=120>")

    get_html_photo.short_description = 'Картинка'
    get_html_mobilephoto.short_description = 'Картинка для мобильных устройств'








admin.site.register(ContactPageZonesImages)
admin.site.register(HomePage, HomePageAdmin)
admin.site.register(ClubPageSeo, ClubPageSeoAdmin)
admin.site.register(PromoPageSeo, PromoPageSeoAdmin)
admin.site.register(FranchisePageSeo, FranchisePageSeoAdmin)
admin.site.register(ContactPageSeo, ContactPageSeoAdmin)
admin.site.register(HomeGallery, HomeGalleryAdmin)
admin.site.register(PromoPage, PromoPageAdmin)

admin.site.site_title = 'Venom24 DashBoard'
admin.site.site_header = 'Админка Venom24'



def image_preview(obj):
    if obj.photo:
        return format_html('<img src="{}" width="100" style="border-radius:6px;" />', obj.photo.url)
    return "—"
image_preview.short_description = "Превью"


# --- 📸 Фото клуба (верхняя галерея) ---
class PhotoClubInline(admin.TabularInline):
    model = PhotoClub
    extra = 1
    fields = ("photo", "photo_mobile", "order", image_preview)
    readonly_fields = (image_preview,)
    ordering = ("order",)


# --- 🖼 Нижняя галерея клуба ---
class ClubGalleryInline(admin.TabularInline):
    model = ClubGallery
    extra = 1
    fields = ("photo", "photo_mobile", "is_published", image_preview)
    readonly_fields = (image_preview,)
    ordering = ("id",)


class ClubRouteInline(admin.StackedInline):
    model = ClubRoute
    extra = 0
    max_num = 1
    can_delete = True
    verbose_name = "Как найти клуб"
    verbose_name_plural = "Как найти клуб"
    fieldsets = (
        (None, {
            "fields": (
                "is_published",
                "title",
                "address",
                "landmark",
                "metro_info",
                "phone",
                "lottie_file",
            )
        }),
    )

class ClubBottomAboutInline(admin.StackedInline):
    model = ClubBottomAbout
    extra = 0
    max_num = 1
    can_delete = True
    verbose_name = "Нижнее описание"
    verbose_name_plural = "Нижнее описание"
    fieldsets = (
        (None, {
            "fields": ("is_published", "title", "txt"),
        }),
    )

class ClubPageImagesInline(admin.StackedInline):
    model = ClubPageImages
    extra = 0
    max_num = 1
    verbose_name = "Изображение зон"
    verbose_name_plural = "Изображение зон"
    fieldsets = (
        (None, {"fields": ("image", "image_mobile")}),
    )


# --- 📰 Новости клуба ---
# @admin.register(ClubNews)
class ClubNewsAdmin(admin.ModelAdmin):
    list_display = ("title", "club", "is_published", "time_create", "time_update")
    list_filter = ("club", "is_published")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "short", "descr")
    list_editable = ("is_published",)
    readonly_fields = ("time_create", "time_update", image_preview)
    fields = (
        "club",
        "title",
        "slug",
        "photo",
        "photo_mobile",
        image_preview,
        "short",
        "descr",
        "sort",
        "is_published",
        "time_create",
        "time_update",
    )


# --- 🎟 Промо-акции клуба ---
class ClubPromoRelationInline(admin.TabularInline):
    """
    Inline для связи акции и клубов.
    Позволяет выбирать, к каким клубам относится акция.
    """
    model = ClubPromoRelation
    extra = 1
    autocomplete_fields = ["club"]


@admin.register(ClubPromo)
class ClubPromoAdmin(admin.ModelAdmin):
    """
    Админка для акций, которые могут быть у нескольких клубов.
    """
    list_display = ("title", "get_clubs", "is_published", "sort", "time_create")
    list_filter = ("is_published",)
    search_fields = ("title", "short", "descr")
    ordering = ("-time_create",)
    inlines = [ClubPromoRelationInline]

    readonly_fields = ("time_create", "time_update", "preview_image")

    fieldsets = (
        ("Основная информация", {
            "fields": ("title", "slug", "is_published", "sort", "is_main_page")
        }),
        ("Контент", {
            "fields": ("short", "descr")
        }),
        ("Изображения", {
            "fields": ("photo", "photo_mobile", "preview_image")
        }),
        ("Системное", {
            "fields": ("time_create", "time_update")
        }),
    )

    def get_clubs(self, obj):
        """
        Возвращает список клубов, связанных с акцией.
        """
        clubs = obj.clubs.all().values_list("name", flat=True)
        return ", ".join(clubs) if clubs else "—"
    get_clubs.short_description = "Клубы"

    def preview_image(self, obj):
        """
        Показывает превью основного изображения в админке.
        """
        if obj.photo:
            return format_html('<img src="{}" width="120" style="border-radius:6px;">', obj.photo.url)
        return "—"
    preview_image.short_description = "Превью"


@admin.register(ClubPromoRelation)
class ClubPromoRelationAdmin(admin.ModelAdmin):
    """
    Отдельная админка для промежуточной связи (на случай ручного управления).
    """
    list_display = ("club", "promo")
    search_fields = ("club__name", "promo__title")
    autocomplete_fields = ["club", "promo"]

    class Meta:
        verbose_name = "Связь клуба и акции"
        verbose_name_plural = "Связи клубов и акций"

# --- 🌐 SEO клуба ---
class ClubSeoInline(admin.StackedInline):
    model = ClubSeo
    extra = 0
    max_num = 1
    fieldsets = (
        (None, {"fields": ("title", "description", "keywords")}),
    )


# --- 🏛 Основная модель клуба ---
@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
        "get_photos_count",
        "get_news_count",
        "get_promos_count",
    )
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("name",)

    # Подключаем связанные блоки
    inlines = [ClubPageImagesInline, ClubSeoInline, PhotoClubInline, ClubGalleryInline, ClubRouteInline, ClubBottomAboutInline,]

    # Группировка полей на странице клуба
    fieldsets = (
        (
            "Основная информация",
            {
                "fields": (
                    "name",
                    "full_name",
                    "slug",
                    "is_open",
                    "video",
                    "phone",
                    "map_link",
                    "is_open_24",
                    "image_of_zones",
                )
            },
        ),
        (
            "Игры клуба",
            {
                "fields": (
                    "pc_games",
                    "tv_games",
                ),
                "description": "Списки игр указываются через запятую без пробелов (например: CS2,Dota 2,Valorant)",
            },
        ),
    )

    # Методы для отображения количества связанных объектов
    def get_photos_count(self, obj):
        return obj.photos.count()

    get_photos_count.short_description = "Фото (верх)"

    def get_news_count(self, obj):
        return obj.news.count()

    get_news_count.short_description = "Новости"

    def get_promos_count(self, obj):
        return obj.promos.count()

    get_promos_count.short_description = "Акции"


@admin.register(NewsNew)
class NewsNewAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_clubs', 'is_main_page', 'is_published', 'time_create')
    list_filter = ('is_published', 'is_main_page', 'clubs')
    search_fields = ('title',)
    filter_horizontal = ('clubs',)  # Позволяет выбирать несколько клубов

    def get_clubs(self, obj):
        clubs = obj.clubs.all()
        if clubs.exists():
            return ", ".join([club.name for club in clubs])
        return "Общая новость"
    get_clubs.short_description = "Клубы"

    def get_list_display_links(self, request, list_display):
        """Чтобы можно было кликнуть по названию для редактирования."""
        return ("title",)

    # def save_model(self, request, obj, form, change):
    #     """
    #     Автоматически отключает 'is_main_page', если выбраны клубы.
    #     Это исключает логическую ошибку: новость не может быть и клубной, и главной.
    #     """
    #     # Проверяем: есть ли выбранные клубы
    #     if obj.is_main_page and obj.pk:
    #         if obj.clubs.exists():
    #             obj.is_main_page = False

    #     super().save_model(request, obj, form, change)

# --- Inline для фото зоны ---
class ZonePhotoInline(admin.TabularInline):
    model = ZonesClubPics
    extra = 1
    fields = ("photo", "photo_mobile", "sort", "is_published")
    readonly_fields = ()
    ordering = ("sort",)
    verbose_name = "Фото зоны"
    verbose_name_plural = "Фото зоны"


# --- Inline для элементов прайса ---
class ZonePriceItemInline(admin.TabularInline):
    model = ZonePriceItem
    extra = 1
    fields = ("time", "price", "order")
    ordering = ("order",)
    verbose_name = "Элемент прайса"
    verbose_name_plural = "Элементы прайса"


# --- Inline для блоков прайсов ---
class ZonePriceBlockInline(admin.StackedInline):
    model = ZonePriceBlock
    extra = 1
    fields = ("title", "is_visible")
    show_change_link = True
    verbose_name = "Блок прайса"
    verbose_name_plural = "Блоки прайса"


# --- Админка для ZonePriceBlock ---
@admin.register(ZonePriceBlock)
class ZonePriceBlockAdmin(admin.ModelAdmin):
    list_display = ("title", "zone", "is_visible", "get_club_name")
    list_filter = ("is_visible", "zone__club")
    search_fields = ("title", "zone__title")
    ordering = ("zone__club", "zone__title")
    inlines = [ZonePriceItemInline]

    def get_club_name(self, obj):
        return obj.zone.club.name
    get_club_name.short_description = "Клуб"

    def get_changeform_initial_data(self, request):
        initial = super().get_changeform_initial_data(request)
        zone_id = request.GET.get("zone")
        if zone_id:
            initial["zone"] = zone_id
        return initial


# --- Главная админка для ClubZonesNew ---
@admin.register(ClubZonesNew)
class ClubZonesNewAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "club",
        "count",
        "is_published",
        "get_total_price_blocks",
        "get_total_photos",
        "add_price_block_link",
        "is_tv"
    )
    list_filter = ("club", "is_published", "is_tv")
    search_fields = ("title", "club__name")
    ordering = ("club", "title")
    inlines = [ZonePhotoInline, ZonePriceBlockInline]

    fieldsets = (
        ("Основное", {
            "fields": ("club", "title", "slug", "count", "sort", "is_published", "is_tv"),
        }),
        ("Оборудование", {
            "fields": ("monitor", "processor", "videocard", "ozu", "headset", "keyboard", "mouse"),
            "classes": ("collapse",),
        }),
        ("Служебные", {
            "fields": ("time_create", "time_update"),
            "classes": ("collapse",),
        }),
    )
    readonly_fields = ("time_create", "time_update")

    def get_total_price_blocks(self, obj):
        return obj.price_blocks.count()
    get_total_price_blocks.short_description = "Блоков прайса"

    def get_total_photos(self, obj):
        return obj.zone_pics.count()
    get_total_photos.short_description = "Фото"

    def add_price_block_link(self, obj):
        url = reverse("admin:venom_zonepriceblock_add") + f"?zone={obj.id}"
        return format_html('<a class="button" href="{}">➕ Добавить блок прайса</a>', url)
    add_price_block_link.short_description = "Добавить блок прайса"

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in instances:
            if isinstance(obj, ZonesClubPics):
                if obj.zone and not obj.club_id:
                    obj.club = obj.zone.club
            obj.save()
        formset.save_m2m()


@admin.register(MainPage)
class MainPageAdmin(admin.ModelAdmin):
    """Админка для единственного экземпляра главной страницы."""

    def has_add_permission(self, request):
        """Запрещаем добавлять больше одной записи."""
        if MainPage.objects.exists():
            return False
        return True

    def changelist_view(self, request, extra_context=None):
        """Если запись уже есть — сразу переходим на страницу её редактирования."""
        obj = MainPage.get_solo()
        return self.change_view(
            request,
            object_id=str(obj.pk),
            extra_context=extra_context,
        )

    def __str__(self):
        return "Главная страница"


@admin.register(FranchisePage)
class FranchisePageAdmin(admin.ModelAdmin):
    """Админка для единственного экземпляра главной страницы."""

    def has_add_permission(self, request):
        """Запрещаем добавлять больше одной записи."""
        if FranchisePage.objects.exists():
            return False
        return True

    def changelist_view(self, request, extra_context=None):
        """Если запись уже есть — сразу переходим на страницу её редактирования."""
        obj = FranchisePage.get_solo()
        return self.change_view(
            request,
            object_id=str(obj.pk),
            extra_context=extra_context,
        )

    def __str__(self):
        return "Страница Франшизы"

@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    """Админка для единственного экземпляра главной страницы."""

    def has_add_permission(self, request):
        """Запрещаем добавлять больше одной записи."""
        if Logo.objects.exists():
            return False
        return True

    def changelist_view(self, request, extra_context=None):
        """Если запись уже есть — сразу переходим на страницу её редактирования."""
        obj = Logo.get_solo()
        return self.change_view(
            request,
            object_id=str(obj.pk),
            extra_context=extra_context,
        )

    def __str__(self):
        return "Лого"