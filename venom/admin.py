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
# admin.site.register(PhotoMahachkala, PhotoVenumAdmin)
# admin.site.register(PhotoMitino, PhotoVenumAdmin)
# admin.site.register(PhotoSerpuhskaya, PhotoVenumAdmin)
# admin.site.register(PhotoVdnx, PhotoVenumAdmin)
# admin.site.register(PhotoVernadka, PhotoVenumAdmin)

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
    # list_display = ('id', 'title', 'short', 'get_html_photo', 'time_create', 'time_update', 'is_published')
    # list_display_links = ('id', 'title', 'short',)
    # search_fields = ('title',)
    # list_editable = ('is_published',)
    # list_filter = ('is_published', 'time_create')
    # readonly_fields = ('time_create', 'time_update')
    # prepopulated_fields = {'slug': ('title',)}
    # save_on_top = True

    # form = NewsAdminForm
    # list_display = ('id', 'title', 'short', 'get_html_photo', 'time_create', 'time_update', 'is_published')
    # list_display_links = ('id', 'title', 'short',)
    # search_fields = ('title',)
    # list_editable = ('is_published',)
    # list_filter = ('is_published', 'time_create')
    # readonly_fields = ('time_create', 'time_update')
    # prepopulated_fields = {'slug': ('title',)}
    # save_on_top = True

    # form = NewsAdminForm
    # list_display = ('id', 'title', 'short', 'get_html_photo', 'time_create', 'time_update', 'is_published')
    # list_display_links = ('id', 'title', 'short',)
    # search_fields = ('title',)
    # list_editable = ('is_published',)
    # list_filter = ('is_published', 'time_create')
    # readonly_fields = ('time_create', 'time_update')
    # prepopulated_fields = {'slug': ('title',)}
    # save_on_top = True




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





#VDNH
########################
class VdnhNewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'short', 'get_html_photo', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'title', 'short',)
    search_fields = ('id', 'title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}
    fields = (
    'title', 'slug', 'short', 'descr', 'photo', 'get_html_photo', 'photo_mobile', 'get_html_mobilephoto', 'time_create',
    'time_update', 'is_published')
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





class VdnhPromoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'short', 'get_html_photo', 'sort', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'title', 'short',)
    search_fields = ('id', 'title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}
    fields = (
    'title', 'slug', 'short', 'descr', 'photo', 'get_html_photo', 'photo_mobile', 'get_html_mobilephoto', 'sort', 'time_create',
    'time_update', 'is_published')
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




class VdnhZonesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_html_photo', 'sort', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'title', )
    search_fields = ('id', 'title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}

    fields = (
        'title', 'slug',
        'photo', 'get_html_photo', 'photo_mobile', 'get_html_mobilephoto',

        'timeone', 'priceone',
        'timetwo', 'prictwo',
        'timetri', 'pricetri',
        'timefour', 'pricefour',
        'timefive', 'pricefive',
        'timesix', 'pricesix',

        'weekend_timeone', 'weekend_priceone',
        'weekend_timetwo', 'weekend_prictwo',
        'weekend_timetri', 'weekend_pricetri',
        'weekend_timefour', 'weekend_pricefour',
        'weekend_timefive', 'weekend_pricefive',
        'weekend_timesix', 'weekend_pricesix',

        'monitor_tile', 'monitor',
        'processor_tile', 'processor',
        'videocard_tile', 'videocard',
        'ozu_tile', 'ozu',
        'headset_tile', 'headset',
        'keyboard_tile', 'keyboard',
        'mouse_tile', 'mouse',

        'sort',
        'time_create',
        'time_update', 'is_published')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo', 'get_html_mobilephoto')
    save_on_top = True

    def get_html_photo(self, object):
        return mark_safe(f"<img src='{object.photo.url}' width=120>")

    def get_html_mobilephoto(self, object):
        return mark_safe(f"<img src='{object.photo_mobile.url}' width=120>")

    get_html_photo.short_description = 'Картинка'
    get_html_mobilephoto.short_description = 'Картинка для мобильных устройств'




# new version of zones


class VdnhZonesNewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'sort', 'is_published')
    list_display_links = ('id', 'title',)
    search_fields = ('id', 'title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}

    # fields = (
    #     'title', 'slug',
    #     'sort',
    #     'time_create',
    #     'time_update', 'is_published')

    fields = (
        'title', 'slug',

        'timeone', 'priceone',
        'timetwo', 'prictwo',
        'timetri', 'pricetri',
        'timefour', 'pricefour',
        'timefive', 'pricefive',
        'timesix', 'pricesix',

        'weekend_timeone', 'weekend_priceone',
        'weekend_timetwo', 'weekend_prictwo',
        'weekend_timetri', 'weekend_pricetri',
        'weekend_timefour', 'weekend_pricefour',
        'weekend_timefive', 'weekend_pricefive',
        'weekend_timesix', 'weekend_pricesix',

        'monitor_tile', 'monitor',
        'processor_tile', 'processor',
        'videocard_tile', 'videocard',
        'ozu_tile', 'ozu',
        'headset_tile', 'headset',
        'keyboard_tile', 'keyboard',
        'mouse_tile', 'mouse',

        'sort',
        'time_create',
        'time_update', 'is_published')

    readonly_fields = ('time_create', 'time_update')
    save_on_top = True




class ZonesVdnhPicsAdmin(admin.ModelAdmin):
    list_display = ('id', 'zone', 'photo_display', 'photo_mobile_display')
    list_display_links = ('id', 'zone',)
    search_fields = ('id', 'zone__title',)
    list_filter = ('zone',)

    fields = ('zone', 'photo', 'photo_mobile')
    save_on_top = True

    def photo_display(self, obj):
        return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />',
                           obj.photo.url) if obj.photo else ''

    photo_display.short_description = 'Photo'

    def photo_mobile_display(self, obj):
        return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />',
                           obj.photo_mobile.url) if obj.photo_mobile else ''

    photo_mobile_display.short_description = 'Mobile Photo'
    
    


# admin.site.register(MahachkalaPicssMahachkalaPicss)

# admin.site.register(VdnhZonesNew, VdnhZonesNewAdmin)
# admin.site.register(ZonesVdnhPics, ZonesVdnhPicsAdmin)









#Vernadka
########################
class VernadkaNewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'short', 'get_html_photo', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'title', 'short',)
    search_fields = ('id', 'title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}
    fields = (
    'title', 'slug', 'short', 'descr', 'photo', 'get_html_photo', 'photo_mobile', 'get_html_mobilephoto', 'time_create',
    'time_update', 'is_published')
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





class VernadkaPromoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'short', 'get_html_photo', 'sort', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'title', 'short',)
    search_fields = ('id', 'title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}
    fields = (
    'title', 'slug', 'short', 'descr', 'photo', 'get_html_photo', 'photo_mobile', 'get_html_mobilephoto', 'sort', 'time_create',
    'time_update', 'is_published')
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






class VernadkaZonesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_html_photo', 'sort', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'title', )
    search_fields = ('id', 'title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}

    fields = (
        'title', 'slug',
        'photo', 'get_html_photo', 'photo_mobile', 'get_html_mobilephoto',

        'timeone', 'priceone',
        'timetwo', 'prictwo',
        'timetri', 'pricetri',
        'timefour', 'pricefour',
        'timefive', 'pricefive',
        'timesix', 'pricesix',

        'weekend_timeone', 'weekend_priceone',
        'weekend_timetwo', 'weekend_prictwo',
        'weekend_timetri', 'weekend_pricetri',
        'weekend_timefour', 'weekend_pricefour',
        'weekend_timefive', 'weekend_pricefive',
        'weekend_timesix', 'weekend_pricesix',

        'monitor_tile', 'monitor',
        'processor_tile', 'processor',
        'videocard_tile', 'videocard',
        'ozu_tile', 'ozu',
        'headset_tile', 'headset',
        'keyboard_tile', 'keyboard',
        'mouse_tile', 'mouse',

        'sort',
        'time_create',
        'time_update', 'is_published')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo', 'get_html_mobilephoto')
    save_on_top = True

    def get_html_photo(self, object):
        return mark_safe(f"<img src='{object.photo.url}' width=120>")

    def get_html_mobilephoto(self, object):
        return mark_safe(f"<img src='{object.photo_mobile.url}' width=120>")

    get_html_photo.short_description = 'Картинка'
    get_html_mobilephoto.short_description = 'Картинка для мобильных устройств'







# new version of zones


class VernadkaZonesNewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'sort', 'is_published')
    list_display_links = ('id', 'title',)
    search_fields = ('id', 'title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}

    # fields = (
    #     'title', 'slug',
    #     'sort',
    #     'time_create',
    #     'time_update', 'is_published')

    fields = (
        'title', 'slug',

        'timeone', 'priceone',
        'timetwo', 'prictwo',
        'timetri', 'pricetri',
        'timefour', 'pricefour',
        'timefive', 'pricefive',
        'timesix', 'pricesix',

        'weekend_timeone', 'weekend_priceone',
        'weekend_timetwo', 'weekend_prictwo',
        'weekend_timetri', 'weekend_pricetri',
        'weekend_timefour', 'weekend_pricefour',
        'weekend_timefive', 'weekend_pricefive',
        'weekend_timesix', 'weekend_pricesix',

        'monitor_tile', 'monitor',
        'processor_tile', 'processor',
        'videocard_tile', 'videocard',
        'ozu_tile', 'ozu',
        'headset_tile', 'headset',
        'keyboard_tile', 'keyboard',
        'mouse_tile', 'mouse',

        'sort',
        'time_create',
        'time_update', 'is_published')

    readonly_fields = ('time_create', 'time_update')
    save_on_top = True




class ZonesVernadkaPicsAdmin(admin.ModelAdmin):
    list_display = ('id', 'zone', 'photo_display', 'photo_mobile_display')
    list_display_links = ('id', 'zone',)
    search_fields = ('id', 'zone__title',)
    list_filter = ('zone',)

    fields = ('zone', 'photo', 'photo_mobile')
    save_on_top = True

    def photo_display(self, obj):
        return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />',
                           obj.photo.url) if obj.photo else ''

    photo_display.short_description = 'Photo'

    def photo_mobile_display(self, obj):
        return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />',
                           obj.photo_mobile.url) if obj.photo_mobile else ''

    photo_mobile_display.short_description = 'Mobile Photo'


# admin.site.register(VernadkaZonesNew, VernadkaZonesNewAdmin)
# admin.site.register(ZonesVernadkaPics, ZonesVernadkaPicsAdmin)









#Mitino

########################
class MitinoNewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'short', 'get_html_photo', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'title', 'short',)
    search_fields = ('id', 'title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}
    fields = (
    'title', 'slug', 'short', 'descr', 'photo', 'get_html_photo', 'photo_mobile', 'get_html_mobilephoto', 'time_create',
    'time_update', 'is_published')
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





class MitinoPromoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'short', 'get_html_photo', 'sort', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'title', 'short',)
    search_fields = ('id', 'title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}
    fields = (
    'title', 'slug', 'short', 'descr', 'photo', 'get_html_photo', 'photo_mobile', 'get_html_mobilephoto', 'sort', 'time_create',
    'time_update', 'is_published')
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







class MitinoZonesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_html_photo', 'sort', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'title', )
    search_fields = ('id', 'title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}

    fields = (
        'title', 'slug',
        'photo', 'get_html_photo', 'photo_mobile', 'get_html_mobilephoto',

        'timeone', 'priceone',
        'timetwo', 'prictwo',
        'timetri', 'pricetri',
        'timefour', 'pricefour',
        'timefive', 'pricefive',
        'timesix', 'pricesix',

        'weekend_timeone', 'weekend_priceone',
        'weekend_timetwo', 'weekend_prictwo',
        'weekend_timetri', 'weekend_pricetri',
        'weekend_timefour', 'weekend_pricefour',
        'weekend_timefive', 'weekend_pricefive',
        'weekend_timesix', 'weekend_pricesix',

        'monitor_tile', 'monitor',
        'processor_tile', 'processor',
        'videocard_tile', 'videocard',
        'ozu_tile', 'ozu',
        'headset_tile', 'headset',
        'keyboard_tile', 'keyboard',
        'mouse_tile', 'mouse',

        'sort',
        'time_create',
        'time_update', 'is_published')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo', 'get_html_mobilephoto')
    save_on_top = True

    def get_html_photo(self, object):
        return mark_safe(f"<img src='{object.photo.url}' width=120>")

    def get_html_mobilephoto(self, object):
        return mark_safe(f"<img src='{object.photo_mobile.url}' width=120>")

    get_html_photo.short_description = 'Картинка'
    get_html_mobilephoto.short_description = 'Картинка для мобильных устройств'



# new version of zones


class MitinoZonesNewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'sort', 'is_published')
    list_display_links = ('id', 'title',)
    search_fields = ('id', 'title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}

    # fields = (
    #     'title', 'slug',
    #     'sort',
    #     'time_create',
    #     'time_update', 'is_published')

    fields = (
        'title', 'slug',

        'timeone', 'priceone',
        'timetwo', 'prictwo',
        'timetri', 'pricetri',
        'timefour', 'pricefour',
        'timefive', 'pricefive',
        'timesix', 'pricesix',

        'weekend_timeone', 'weekend_priceone',
        'weekend_timetwo', 'weekend_prictwo',
        'weekend_timetri', 'weekend_pricetri',
        'weekend_timefour', 'weekend_pricefour',
        'weekend_timefive', 'weekend_pricefive',
        'weekend_timesix', 'weekend_pricesix',

        'monitor_tile', 'monitor',
        'processor_tile', 'processor',
        'videocard_tile', 'videocard',
        'ozu_tile', 'ozu',
        'headset_tile', 'headset',
        'keyboard_tile', 'keyboard',
        'mouse_tile', 'mouse',

        'sort',
        'time_create',
        'time_update', 'is_published')

    readonly_fields = ('time_create', 'time_update')
    save_on_top = True




class ZonesMitinoPicsAdmin(admin.ModelAdmin):
    list_display = ('id', 'zone', 'photo_display', 'photo_mobile_display')
    list_display_links = ('id', 'zone',)
    search_fields = ('id', 'zone__title',)
    list_filter = ('zone',)

    fields = ('zone', 'photo', 'photo_mobile')
    save_on_top = True

    def photo_display(self, obj):
        return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />',
                           obj.photo.url) if obj.photo else ''

    photo_display.short_description = 'Photo'

    def photo_mobile_display(self, obj):
        return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />',
                           obj.photo_mobile.url) if obj.photo_mobile else ''

    photo_mobile_display.short_description = 'Mobile Photo'


# admin.site.register(MitinoZonesNew, MitinoZonesNewAdmin)
# admin.site.register(ZonesMitinoPics, ZonesMitinoPicsAdmin)









#Koptevo

########################
class KoptevoNewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'short', 'get_html_photo', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'title', 'short',)
    search_fields = ('id', 'title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}
    fields = (
    'title', 'slug', 'short', 'descr', 'photo', 'get_html_photo', 'photo_mobile', 'get_html_mobilephoto', 'time_create',
    'time_update', 'is_published')
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





class KoptevoPromoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'short', 'get_html_photo', 'sort', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'title', 'short',)
    search_fields = ('id', 'title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}
    fields = (
    'title', 'slug', 'short', 'descr', 'photo', 'get_html_photo', 'photo_mobile', 'get_html_mobilephoto', 'sort', 'time_create',
    'time_update', 'is_published')
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






class KoptevoZonesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_html_photo', 'sort', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'title', )
    search_fields = ('id', 'title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}

    fields = (
        'title', 'slug',
        'photo', 'get_html_photo', 'photo_mobile', 'get_html_mobilephoto',

        'timeone', 'priceone',
        'timetwo', 'prictwo',
        'timetri', 'pricetri',
        'timefour', 'pricefour',
        'timefive', 'pricefive',
        'timesix', 'pricesix',

        'weekend_timeone', 'weekend_priceone',
        'weekend_timetwo', 'weekend_prictwo',
        'weekend_timetri', 'weekend_pricetri',
        'weekend_timefour', 'weekend_pricefour',
        'weekend_timefive', 'weekend_pricefive',
        'weekend_timesix', 'weekend_pricesix',

        'monitor_tile', 'monitor',
        'processor_tile', 'processor',
        'videocard_tile', 'videocard',
        'ozu_tile', 'ozu',
        'headset_tile', 'headset',
        'keyboard_tile', 'keyboard',
        'mouse_tile', 'mouse',

        'sort',
        'time_create',
        'time_update', 'is_published')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo', 'get_html_mobilephoto')
    save_on_top = True

    def get_html_photo(self, object):
        return mark_safe(f"<img src='{object.photo.url}' width=120>")

    def get_html_mobilephoto(self, object):
        return mark_safe(f"<img src='{object.photo_mobile.url}' width=120>")

    get_html_photo.short_description = 'Картинка'
    get_html_mobilephoto.short_description = 'Картинка для мобильных устройств'











#Zelebino

########################
class ZulebinoNewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'short', 'get_html_photo', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'title', 'short',)
    search_fields = ('id', 'title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}
    fields = (
    'title', 'slug', 'short', 'descr', 'photo', 'get_html_photo', 'photo_mobile', 'get_html_mobilephoto', 'time_create',
    'time_update', 'is_published')
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





class ZulebinoPromoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'short', 'get_html_photo', 'sort', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'title', 'short',)
    search_fields = ('id', 'title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}
    fields = (
    'title', 'slug', 'short', 'descr', 'photo', 'get_html_photo', 'photo_mobile', 'get_html_mobilephoto', 'sort', 'time_create',
    'time_update', 'is_published')
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





class ZulebinoZonesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_html_photo', 'sort', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'title', )
    search_fields = ('id', 'title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}

    fields = (
        'title', 'slug',
        'photo', 'get_html_photo', 'photo_mobile', 'get_html_mobilephoto',

        'timeone', 'priceone',
        'timetwo', 'prictwo',
        'timetri', 'pricetri',
        'timefour', 'pricefour',
        'timefive', 'pricefive',
        'timesix', 'pricesix',

        'weekend_timeone', 'weekend_priceone',
        'weekend_timetwo', 'weekend_prictwo',
        'weekend_timetri', 'weekend_pricetri',
        'weekend_timefour', 'weekend_pricefour',
        'weekend_timefive', 'weekend_pricefive',
        'weekend_timesix', 'weekend_pricesix',

        'monitor_tile', 'monitor',
        'processor_tile', 'processor',
        'videocard_tile', 'videocard',
        'ozu_tile', 'ozu',
        'headset_tile', 'headset',
        'keyboard_tile', 'keyboard',
        'mouse_tile', 'mouse',

        'sort',
        'time_create',
        'time_update', 'is_published')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo', 'get_html_mobilephoto')
    save_on_top = True

    def get_html_photo(self, object):
        return mark_safe(f"<img src='{object.photo.url}' width=120>")

    def get_html_mobilephoto(self, object):
        return mark_safe(f"<img src='{object.photo_mobile.url}' width=120>")

    get_html_photo.short_description = 'Картинка'
    get_html_mobilephoto.short_description = 'Картинка для мобильных устройств'










#Zukovsky

########################
class ZukovskyNewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'short', 'get_html_photo', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'title', 'short',)
    search_fields = ('id', 'title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}
    fields = (
    'title', 'slug', 'short', 'descr', 'photo', 'get_html_photo', 'photo_mobile', 'get_html_mobilephoto', 'time_create',
    'time_update', 'is_published')
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





class ZukovskyPromoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'short', 'get_html_photo', 'sort', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'title', 'short',)
    search_fields = ('id', 'title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}
    fields = (
    'title', 'slug', 'short', 'descr', 'photo', 'get_html_photo', 'photo_mobile', 'get_html_mobilephoto', 'sort', 'time_create',
    'time_update', 'is_published')
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






class ZukovskyZonesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_html_photo', 'sort', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'title', )
    search_fields = ('id', 'title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}

    fields = (
        'title', 'slug',
        'photo', 'get_html_photo', 'photo_mobile', 'get_html_mobilephoto',

        'timeone', 'priceone',
        'timetwo', 'prictwo',
        'timetri', 'pricetri',
        'timefour', 'pricefour',
        'timefive', 'pricefive',
        'timesix', 'pricesix',

        'weekend_timeone', 'weekend_priceone',
        'weekend_timetwo', 'weekend_prictwo',
        'weekend_timetri', 'weekend_pricetri',
        'weekend_timefour', 'weekend_pricefour',
        'weekend_timefive', 'weekend_pricefive',
        'weekend_timesix', 'weekend_pricesix',

        'monitor_tile', 'monitor',
        'processor_tile', 'processor',
        'videocard_tile', 'videocard',
        'ozu_tile', 'ozu',
        'headset_tile', 'headset',
        'keyboard_tile', 'keyboard',
        'mouse_tile', 'mouse',

        'sort',
        'time_create',
        'time_update', 'is_published')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo', 'get_html_mobilephoto')
    save_on_top = True

    def get_html_photo(self, object):
        return mark_safe(f"<img src='{object.photo.url}' width=120>")

    def get_html_mobilephoto(self, object):
        return mark_safe(f"<img src='{object.photo_mobile.url}' width=120>")

    get_html_photo.short_description = 'Картинка'
    get_html_mobilephoto.short_description = 'Картинка для мобильных устройств'










#Serpuhovskaya

########################
class SerpuhovskayaNewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'short', 'get_html_photo', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'title', 'short',)
    search_fields = ('id', 'title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}
    fields = (
    'title', 'slug', 'short', 'descr', 'photo', 'get_html_photo', 'photo_mobile', 'get_html_mobilephoto', 'time_create',
    'time_update', 'is_published')
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





class SerpuhovskayaPromoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'short', 'get_html_photo', 'sort', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'title', 'short',)
    search_fields = ('id', 'title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}
    fields = (
    'title', 'slug', 'short', 'descr', 'photo', 'get_html_photo', 'photo_mobile', 'get_html_mobilephoto', 'sort', 'time_create',
    'time_update', 'is_published')
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





class SerpuhovskayaZonesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_html_photo', 'sort', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'title', )
    search_fields = ('id', 'title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}

    fields = (
        'title', 'slug',
        'photo', 'get_html_photo', 'photo_mobile', 'get_html_mobilephoto',

        'timeone', 'priceone',
        'timetwo', 'prictwo',
        'timetri', 'pricetri',
        'timefour', 'pricefour',
        'timefive', 'pricefive',
        'timesix', 'pricesix',

        'weekend_timeone', 'weekend_priceone',
        'weekend_timetwo', 'weekend_prictwo',
        'weekend_timetri', 'weekend_pricetri',
        'weekend_timefour', 'weekend_pricefour',
        'weekend_timefive', 'weekend_pricefive',
        'weekend_timesix', 'weekend_pricesix',

        'monitor_tile', 'monitor',
        'processor_tile', 'processor',
        'videocard_tile', 'videocard',
        'ozu_tile', 'ozu',
        'headset_tile', 'headset',
        'keyboard_tile', 'keyboard',
        'mouse_tile', 'mouse',

        'sort',
        'time_create',
        'time_update', 'is_published')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo', 'get_html_mobilephoto')
    save_on_top = True

    def get_html_photo(self, object):
        return mark_safe(f"<img src='{object.photo.url}' width=120>")

    def get_html_mobilephoto(self, object):
        return mark_safe(f"<img src='{object.photo_mobile.url}' width=120>")

    get_html_photo.short_description = 'Картинка'
    get_html_mobilephoto.short_description = 'Картинка для мобильных устройств'





# new version of zones with pics


class SerpuhovskayaZonesNewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'sort', 'is_published')
    list_display_links = ('id', 'title',)
    search_fields = ('id', 'title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}

    # fields = (
    #     'title', 'slug',
    #     'sort',
    #     'time_create',
    #     'time_update', 'is_published')

    fields = (
        'title', 'slug',

        'timeone', 'priceone',
        'timetwo', 'prictwo',
        'timetri', 'pricetri',
        'timefour', 'pricefour',
        'timefive', 'pricefive',
        'timesix', 'pricesix',

        'weekend_timeone', 'weekend_priceone',
        'weekend_timetwo', 'weekend_prictwo',
        'weekend_timetri', 'weekend_pricetri',
        'weekend_timefour', 'weekend_pricefour',
        'weekend_timefive', 'weekend_pricefive',
        'weekend_timesix', 'weekend_pricesix',

        'monitor_tile', 'monitor',
        'processor_tile', 'processor',
        'videocard_tile', 'videocard',
        'ozu_tile', 'ozu',
        'headset_tile', 'headset',
        'keyboard_tile', 'keyboard',
        'mouse_tile', 'mouse',

        'sort',
        'time_create',
        'time_update', 'is_published')

    readonly_fields = ('time_create', 'time_update')
    save_on_top = True



class ZonesSerpuhovskayaPicsAdmin(admin.ModelAdmin):
    list_display = ('id', 'zone', 'photo_display', 'photo_mobile_display')
    list_display_links = ('id', 'zone',)
    search_fields = ('id', 'zone__title',)
    list_filter = ('zone',)

    fields = ('zone', 'photo', 'photo_mobile')
    save_on_top = True

    def photo_display(self, obj):
        return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />',
                           obj.photo.url) if obj.photo else ''

    photo_display.short_description = 'Photo'

    def photo_mobile_display(self, obj):
        return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />',
                           obj.photo_mobile.url) if obj.photo_mobile else ''

    photo_mobile_display.short_description = 'Mobile Photo'



# admin.site.register(SerpuhovskayaZonesNew, SerpuhovskayaZonesNewAdmin)
# admin.site.register(ZonesSerpuhovskayaPics, ZonesSerpuhovskayaPicsAdmin)


# Pushkino

########################
class PushkinoNewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'short', 'get_html_photo', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'title', 'short',)
    search_fields = ('id', 'title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}
    fields = (
    'title', 'slug', 'short', 'descr', 'photo', 'get_html_photo', 'photo_mobile', 'get_html_mobilephoto', 'time_create',
    'time_update', 'is_published')
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





class PushkinoPromoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'short', 'get_html_photo', 'sort', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'title', 'short',)
    search_fields = ('id', 'title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}
    fields = (
    'title', 'slug', 'short', 'descr', 'photo', 'get_html_photo', 'photo_mobile', 'get_html_mobilephoto', 'sort', 'time_create',
    'time_update', 'is_published')
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






class PushkinoZonesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_html_photo', 'sort', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'title', )
    search_fields = ('id', 'title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}

    fields = (
        'title', 'slug',
        'photo', 'get_html_photo', 'photo_mobile', 'get_html_mobilephoto',

        'timeone', 'priceone',
        'timetwo', 'prictwo',
        'timetri', 'pricetri',
        'timefour', 'pricefour',
        'timefive', 'pricefive',
        'timesix', 'pricesix',

        'weekend_timeone', 'weekend_priceone',
        'weekend_timetwo', 'weekend_prictwo',
        'weekend_timetri', 'weekend_pricetri',
        'weekend_timefour', 'weekend_pricefour',
        'weekend_timefive', 'weekend_pricefive',
        'weekend_timesix', 'weekend_pricesix',

        'monitor_tile', 'monitor',
        'processor_tile', 'processor',
        'videocard_tile', 'videocard',
        'ozu_tile', 'ozu',
        'headset_tile', 'headset',
        'keyboard_tile', 'keyboard',
        'mouse_tile', 'mouse',

        'sort',
        'time_create',
        'time_update', 'is_published')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo', 'get_html_mobilephoto')
    save_on_top = True

    def get_html_photo(self, object):
        return mark_safe(f"<img src='{object.photo.url}' width=120>")

    def get_html_mobilephoto(self, object):
        return mark_safe(f"<img src='{object.photo_mobile.url}' width=120>")

    get_html_photo.short_description = 'Картинка'
    get_html_mobilephoto.short_description = 'Картинка для мобильных устройств'











# Mahachkala

########################
class MahachkalaNewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'short', 'get_html_photo', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'title', 'short',)
    search_fields = ('id', 'title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}
    fields = (
    'title', 'slug', 'short', 'descr', 'photo', 'get_html_photo', 'photo_mobile', 'get_html_mobilephoto', 'time_create',
    'time_update', 'is_published')
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





class MahachkalaPromoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'short', 'get_html_photo', 'sort', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'title', 'short',)
    search_fields = ('id', 'title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}
    fields = (
    'title', 'slug', 'short', 'descr', 'photo', 'get_html_photo', 'photo_mobile', 'get_html_mobilephoto', 'sort', 'time_create',
    'time_update', 'is_published')
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







class MahachkalaZonesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'sort', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'title', )
    search_fields = ('id', 'title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}

    fields = (
        'title', 'slug',


        'timeone', 'priceone',
        'timetwo', 'prictwo',
        'timetri', 'pricetri',
        'timefour', 'pricefour',
        'timefive', 'pricefive',
        'timesix', 'pricesix',

        'weekend_timeone', 'weekend_priceone',
        'weekend_timetwo', 'weekend_prictwo',
        'weekend_timetri', 'weekend_pricetri',
        'weekend_timefour', 'weekend_pricefour',
        'weekend_timefive', 'weekend_pricefive',
        'weekend_timesix', 'weekend_pricesix',

        'monitor_tile', 'monitor',
        'processor_tile', 'processor',
        'videocard_tile', 'videocard',
        'ozu_tile', 'ozu',
        'headset_tile', 'headset',
        'keyboard_tile', 'keyboard',
        'mouse_tile', 'mouse',

        'sort',
        'time_create',
        'time_update', 'is_published')
    
    readonly_fields = ('time_create', 'time_update',)
    save_on_top = True









#################  SEO #################
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



class VdnhSeoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'keywords')
    list_display_links = ('id', 'title', 'description',)
    search_fields = ('id', 'title',)
    fields = ('title', 'description', 'keywords')




class VernadkaSeoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'keywords')
    list_display_links = ('id', 'title', 'description',)
    search_fields = ('id', 'title',)
    fields = ('title', 'description', 'keywords')



class MitinoSeoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'keywords')
    list_display_links = ('id', 'title', 'description',)
    search_fields = ('id', 'title',)
    fields = ('title', 'description', 'keywords')




class KoptevoSeoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'keywords')
    list_display_links = ('id', 'title', 'description',)
    search_fields = ('id', 'title',)
    fields = ('title', 'description', 'keywords')


class ZulebinoSeoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'keywords')
    list_display_links = ('id', 'title', 'description',)
    search_fields = ('id', 'title',)
    fields = ('title', 'description', 'keywords')


class ZukovskySeoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'keywords')
    list_display_links = ('id', 'title', 'description',)
    search_fields = ('id', 'title',)
    fields = ('title', 'description', 'keywords')


class SerpuhovkayaSeoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'keywords')
    list_display_links = ('id', 'title', 'description',)
    search_fields = ('id', 'title',)
    fields = ('title', 'description', 'keywords')



class PushkinoSeoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'keywords')
    list_display_links = ('id', 'title', 'description',)
    search_fields = ('id', 'title',)
    fields = ('title', 'description', 'keywords')


class MahachkalaSeoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'keywords')
    list_display_links = ('id', 'title', 'description',)
    search_fields = ('id', 'title',)
    fields = ('title', 'description', 'keywords')

#################  SEO END #################












#################  GALLERY_BOOTOM #################


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





class VdnhGalleryAdmin(admin.ModelAdmin):
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




class VernadkaGalleryAdmin(admin.ModelAdmin):
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




class MitinoGalleryAdmin(admin.ModelAdmin):
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




class SerpuhovskayaGalleryAdmin(admin.ModelAdmin):
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






class KoptevoGalleryAdmin(admin.ModelAdmin):
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





class ZulebinoGalleryAdmin(admin.ModelAdmin):
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




class ZukovskyGalleryAdmin(admin.ModelAdmin):
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



class PushkinoGalleryAdmin(admin.ModelAdmin):
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







class MahachkalaGalleryAdmin(admin.ModelAdmin):
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



#################  GALLERY_BOOTOM END #################




admin.site.register(ContactPageZonesImages)




admin.site.register(HomePage, HomePageAdmin)
admin.site.register(ClubPageSeo, ClubPageSeoAdmin)
admin.site.register(PromoPageSeo, PromoPageSeoAdmin)
admin.site.register(FranchisePageSeo, FranchisePageSeoAdmin)
admin.site.register(ContactPageSeo, ContactPageSeoAdmin)

# admin.site.register(VdnhSeo, VdnhSeoAdmin)
# admin.site.register(VernadkaSeo, VernadkaSeoAdmin)
# admin.site.register(MitinoSeo, MitinoSeoAdmin)
# admin.site.register(KoptevoSeo, KoptevoSeoAdmin)
# admin.site.register(ZulebinoSeo, ZulebinoSeoAdmin)
# admin.site.register(ZukovskySeo, ZukovskySeoAdmin)
# admin.site.register(SerpuhovkayaSeo, SerpuhovkayaSeoAdmin)
# admin.site.register(PushkinoSeo, PushkinoSeoAdmin)
# admin.site.register(MahachkalaSeo, MahachkalaSeoAdmin)








admin.site.register(HomeGallery, HomeGalleryAdmin)
# admin.site.register(VdnhGallery, VdnhGalleryAdmin)
# admin.site.register(VernadkaGallery, VernadkaGalleryAdmin)
# admin.site.register(MitinoGallery, MitinoGalleryAdmin)
# admin.site.register(SerpuhovskayaGallery, SerpuhovskayaGalleryAdmin)
# admin.site.register(KoptevoGallery, KoptevoGalleryAdmin)
# admin.site.register(ZulebinoGallery, ZulebinoGalleryAdmin)
# admin.site.register(ZukovskyGallery, ZukovskyGalleryAdmin)
# admin.site.register(PushkinoGallery, PushkinoGalleryAdmin)
# admin.site.register(MahachkalaGallery, MahachkalaGalleryAdmin)








admin.site.register(PromoPage, PromoPageAdmin)
# admin.site.register(News, NewsAdmin)
# admin.site.register(Categorynews, CategorynewsAdmin)



# admin.site.register(VdnhNews, VdnhNewsAdmin)
# admin.site.register(VdnhPromo, VdnhPromoAdmin)
# admin.site.register(VdnhZones, VdnhZonesAdmin)


# admin.site.register(VernadkaNews, VernadkaNewsAdmin)
# admin.site.register(VernadkaPromo, VernadkaPromoAdmin)
# admin.site.register(VernadkaZones, VernadkaZonesAdmin)


# admin.site.register(MitinoNews, MitinoNewsAdmin)
# admin.site.register(MitinoPromo, MitinoPromoAdmin)
# admin.site.register(MitinoZones, MitinoZonesAdmin)



# admin.site.register(KoptevoNews, KoptevoNewsAdmin)
# admin.site.register(KoptevoPromo, KoptevoPromoAdmin)
# admin.site.register(KoptevoZones, KoptevoZonesAdmin)


# admin.site.register(ZulebinoNews, ZulebinoNewsAdmin)
# admin.site.register(ZulebinoPromo, ZulebinoPromoAdmin)
# admin.site.register(ZulebinoZones, ZulebinoZonesAdmin)



# admin.site.register(ZukovskyNews, ZukovskyNewsAdmin)
# admin.site.register(ZukovskyPromo, ZukovskyPromoAdmin)
# admin.site.register(ZukovskyZones, ZukovskyZonesAdmin)



# admin.site.register(SerpuhovskayaNews, SerpuhovskayaNewsAdmin)
# admin.site.register(SerpuhovskayaPromo, SerpuhovskayaPromoAdmin)
# admin.site.register(SerpuhovskayaZones, SerpuhovskayaZonesAdmin)



# admin.site.register(PushkinoNews, PushkinoNewsAdmin)
# admin.site.register(PushkinoPromo, PushkinoPromoAdmin)
# admin.site.register(PushkinoZones, PushkinoZonesAdmin)



# admin.site.register(MahachkalaNews, MahachkalaNewsAdmin)
# admin.site.register(MahachkalaPromo, MahachkalaPromoAdmin)
# admin.site.register(MahachkalaZoness, MahachkalaZonesAdmin)




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
@admin.register(ClubNews)
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
@admin.register(ClubPromo)
class ClubPromoAdmin(admin.ModelAdmin):
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
    inlines = [ClubSeoInline, PhotoClubInline, ClubGalleryInline, ClubRouteInline, ClubBottomAboutInline, ClubPageImagesInline,]

    # Группировка полей на странице клуба
    fieldsets = (
        (
            "Основная информация",
            {
                "fields": (
                    "name",
                    "full_name",
                    "slug",
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
    list_display = (
        "title",
        "club",
        "is_main_page",
        "is_published",
        "sort",
        "time_create",
        "time_update",
    )
    list_filter = ("is_published", "is_main_page", "club")
    search_fields = ("title", "short", "descr")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("-time_create",)
    list_editable = ("is_published", "is_main_page", "sort")
    readonly_fields = ("time_create", "time_update")

    fieldsets = (
        (
            "Основная информация",
            {
                "fields": (
                    "title",
                    "slug",
                    "club",
                    "is_main_page",
                    "is_published",
                    "sort",
                )
            },
        ),
        (
            "Контент",
            {
                "fields": (
                    "photo",
                    "photo_mobile",
                    "short",
                    "descr",
                )
            },
        ),
        (
            "Системная информация",
            {
                "classes": ("collapse",),
                "fields": ("time_create", "time_update"),
            },
        ),
    )

    def get_queryset(self, request):
        """Добавляем select_related для ускорения выборки клуба."""
        qs = super().get_queryset(request)
        return qs.select_related("club")

    def get_list_display_links(self, request, list_display):
        """Чтобы можно было кликнуть по названию для редактирования."""
        return ("title",)

    def save_model(self, request, obj, form, change):
        """
        Автоматически отключает 'is_main_page', если указан клуб.
        Это исключает логическую ошибку: новость не может быть и клубной, и главной.
        """
        if obj.club and obj.is_main_page:
            obj.is_main_page = False
        super().save_model(request, obj, form, change)


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
    )
    list_filter = ("club", "is_published")
    search_fields = ("title", "club__name")
    ordering = ("club", "title")
    inlines = [ZonePhotoInline, ZonePriceBlockInline]

    fieldsets = (
        ("Основное", {
            "fields": ("club", "title", "slug", "count", "sort", "is_published"),
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