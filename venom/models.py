from PIL import Image
import os
from io import BytesIO
from django.core.files.base import ContentFile
from os.path import basename
from django.db import models
from django.core.exceptions import ValidationError

class PhotoVdnx(models.Model):
    photo = models.ImageField(upload_to='photos/vdnx/', verbose_name='Фото')
    photo_mobile = models.ImageField(upload_to='photos/vdnx/', verbose_name='Фото мобильное')
    order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name='Порядок')
    
    def __str__(self):
        return f'{basename(self.photo.name)}'
    

    class Meta:
        verbose_name = 'Фотогаллерея ВДНХ'
        verbose_name_plural = 'Фотогаллерея ВДНХ'
        ordering = ['order', ]
        
    
    def save(self, *args, **kwargs):
        if self.photo:
            img = Image.open(self.photo)
            img = img.convert("RGB")
            img_io = BytesIO()
            img.save(img_io, format='WEBP', quality=85)
            img_name, _ = os.path.splitext(self.photo.name)
            self.photo.save(f"{img_name}.webp", ContentFile(img_io.getvalue()), save=False)
        if self.photo_mobile:
            img = Image.open(self.photo_mobile)
            img = img.convert("RGB")
            img_io = BytesIO()
            img.save(img_io, format='WEBP', quality=85)
            img_name, _ = os.path.splitext(self.photo_mobile.name)
            self.photo_mobile.save(f"{img_name}.webp", ContentFile(img_io.getvalue()), save=False)
        super().save(*args, **kwargs)
        
        
class PhotoMitino(models.Model):
    photo = models.ImageField(upload_to='photos/mitino/', verbose_name='Фото')
    photo_mobile = models.ImageField(upload_to='photos/mitino/', verbose_name='Фото мобильное')
    order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name='Порядок')
    
    def __str__(self):
        return f'{basename(self.photo.name)}'
    

    class Meta:
        verbose_name = 'Фотогаллерея Митино'
        verbose_name_plural = 'Фотогаллерея Митино'
        ordering = ['order', ]
        
    
    def save(self, *args, **kwargs):
        if self.photo:
            img = Image.open(self.photo)
            img = img.convert("RGB")
            img_io = BytesIO()
            img.save(img_io, format='WEBP', quality=85)
            img_name, _ = os.path.splitext(self.photo.name)
            self.photo.save(f"{img_name}.webp", ContentFile(img_io.getvalue()), save=False)
        if self.photo_mobile:
            img = Image.open(self.photo_mobile)
            img = img.convert("RGB")
            img_io = BytesIO()
            img.save(img_io, format='WEBP', quality=85)
            img_name, _ = os.path.splitext(self.photo_mobile.name)
            self.photo_mobile.save(f"{img_name}.webp", ContentFile(img_io.getvalue()), save=False)
        super().save(*args, **kwargs)
        

class PhotoVernadka(models.Model):
    photo = models.ImageField(upload_to='photos/vernadka/', verbose_name='Фото')
    photo_mobile = models.ImageField(upload_to='photos/vernadka/', verbose_name='Фото мобильное')
    order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name='Порядок')
    
    def __str__(self):
        return f'{basename(self.photo.name)}'
    
    
    class Meta:
        verbose_name = 'Фотогаллерея Вернадского'
        verbose_name_plural = 'Фотогаллерея Вернадского'
        ordering = ['order', ]
        
    
    def save(self, *args, **kwargs):
        if self.photo:
            img = Image.open(self.photo)
            img = img.convert("RGB")
            img_io = BytesIO()
            img.save(img_io, format='WEBP', quality=85)
            img_name, _ = os.path.splitext(self.photo.name)
            self.photo.save(f"{img_name}.webp", ContentFile(img_io.getvalue()), save=False)
        if self.photo_mobile:
            img = Image.open(self.photo_mobile)
            img = img.convert("RGB")
            img_io = BytesIO()
            img.save(img_io, format='WEBP', quality=85)
            img_name, _ = os.path.splitext(self.photo_mobile.name)
            self.photo_mobile.save(f"{img_name}.webp", ContentFile(img_io.getvalue()), save=False)
        super().save(*args, **kwargs)
        

class PhotoMahachkala(models.Model):
    photo = models.ImageField(upload_to='photos/mahachkala/', verbose_name='Фото')
    photo_mobile = models.ImageField(upload_to='photos/mahachkala/', verbose_name='Фото мобильное')
    order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name='Порядок')
    
    def __str__(self):
        return f'{basename(self.photo.name)}'
    
    
    class Meta:
        verbose_name = 'Фотогаллерея Махачкала'
        verbose_name_plural = 'Фотогаллерея Махачкала'
        ordering = ['order', ]
        
    
    def save(self, *args, **kwargs):
        if self.photo:
            img = Image.open(self.photo)
            img = img.convert("RGB")
            img_io = BytesIO()
            img.save(img_io, format='WEBP', quality=85)
            img_name, _ = os.path.splitext(self.photo.name)
            self.photo.save(f"{img_name}.webp", ContentFile(img_io.getvalue()), save=False)
        if self.photo_mobile:
            img = Image.open(self.photo_mobile)
            img = img.convert("RGB")
            img_io = BytesIO()
            img.save(img_io, format='WEBP', quality=85)
            img_name, _ = os.path.splitext(self.photo_mobile.name)
            self.photo_mobile.save(f"{img_name}.webp", ContentFile(img_io.getvalue()), save=False)
        super().save(*args, **kwargs)
        
        
class PhotoSerpuhskaya(models.Model):
    photo = models.ImageField(upload_to='photos/serp/', verbose_name='Фото')
    photo_mobile = models.ImageField(upload_to='photos/serp/', verbose_name='Фото мобильное')
    order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name='Порядок')
    
    def __str__(self):
        return f'{basename(self.photo.name)}'
    
    
    class Meta:
        verbose_name = 'Фотогаллерея Серпуховская'
        verbose_name_plural = 'Фотогаллерея Серпуховская'
        ordering = ['photo', ]
        
    
    def save(self, *args, **kwargs):
        if self.photo:
            img = Image.open(self.photo)
            img = img.convert("RGB")
            img_io = BytesIO()
            img.save(img_io, format='WEBP', quality=85)
            img_name, _ = os.path.splitext(self.photo.name)
            self.photo.save(f"{img_name}.webp", ContentFile(img_io.getvalue()), save=False)
        if self.photo_mobile:
            img = Image.open(self.photo_mobile)
            img = img.convert("RGB")
            img_io = BytesIO()
            img.save(img_io, format='WEBP', quality=85)
            img_name, _ = os.path.splitext(self.photo_mobile.name)
            self.photo_mobile.save(f"{img_name}.webp", ContentFile(img_io.getvalue()), save=False)
        super().save(*args, **kwargs)
        

class ZonePlay(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    photo = models.ImageField(upload_to='photos/zones/', verbose_name='Фото')
    photo_mobile = models.ImageField(upload_to='photos/zones/', verbose_name='Фото мобильное')
    order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name='Порядок')
    
    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = 'Игровая зона главной страницы'
        verbose_name_plural = 'Игровые зоны главной страницы'
        ordering = ['order', ]
        
        
    def save(self, *args, **kwargs):
        if self.photo:
            img = Image.open(self.photo)
            img = img.convert("RGB")
            img_io = BytesIO()
            img.save(img_io, format='WEBP', quality=85)
            img_name, _ = os.path.splitext(self.photo.name)
            self.photo.save(f"{img_name}.webp", ContentFile(img_io.getvalue()), save=False)
        if self.photo_mobile:
            img = Image.open(self.photo_mobile)
            img = img.convert("RGB")
            img_io = BytesIO()
            img.save(img_io, format='WEBP', quality=85)
            img_name, _ = os.path.splitext(self.photo_mobile.name)
            self.photo_mobile.save(f"{img_name}.webp", ContentFile(img_io.getvalue()), save=False)
        super().save(*args, **kwargs)

class Characteristics(models.Model):
    zone = models.ForeignKey('ZonePlay', on_delete=models.CASCADE, verbose_name='Игровая зона')
    key = models.CharField(max_length=255, verbose_name='Характеристика')
    value = models.CharField(max_length=255, verbose_name='Значение')
    
    def __str__(self):
        return self.key
    
    
    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'
        
class PhotoVenum(models.Model):
    photo = models.ImageField(upload_to='photos/venum/', verbose_name='Фото')
    photo_mobile = models.ImageField(upload_to='photos/venum/', verbose_name='Фото мобильное')
    order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name='Порядок')

    def __str__(self):
        return f'{basename(self.photo.name)}'

    class Meta:
        verbose_name = 'Фотогаллерея клубов VENOM'
        verbose_name_plural = 'Фотогаллерея клубов VENOM'
        ordering = ['order', ]


    def save(self, *args, **kwargs):
        if self.photo:
            img = Image.open(self.photo)
            img = img.convert("RGB")
            img_io = BytesIO()
            img.save(img_io, format='WEBP', quality=85)
            img_name, _ = os.path.splitext(self.photo.name)
            self.photo.save(f"{img_name}.webp", ContentFile(img_io.getvalue()), save=False)
        if self.photo_mobile:
            img = Image.open(self.photo_mobile)
            img = img.convert("RGB")
            img_io = BytesIO()
            img.save(img_io, format='WEBP', quality=85)
            img_name, _ = os.path.splitext(self.photo_mobile.name)
            self.photo_mobile.save(f"{img_name}.webp", ContentFile(img_io.getvalue()), save=False)
        super().save(*args, **kwargs)
        
class Tournament(models.Model):
    photo = models.ImageField(upload_to='photos/tournament/', verbose_name='Фото')
    photo_mobile = models.ImageField(upload_to='photos/tournament/', verbose_name='Фото мобильное')
    order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name='Порядок')
    
    def __str__(self):
        return f'{basename(self.photo.name)}'
    
    
    class Meta:
        verbose_name = 'Турниры VENOM'
        verbose_name_plural = 'Турниры VENOM'
        ordering = ['order', ]
        
        
    def save(self, *args, **kwargs):
        if self.photo:
            img = Image.open(self.photo)
            img = img.convert("RGB")
            img_io = BytesIO()
            img.save(img_io, format='WEBP', quality=85)
            img_name, _ = os.path.splitext(self.photo.name)
            self.photo.save(f"{img_name}.webp", ContentFile(img_io.getvalue()), save=False)
        if self.photo_mobile:
            img = Image.open(self.photo_mobile)
            img = img.convert("RGB")
            img_io = BytesIO()
            img.save(img_io, format='WEBP', quality=85)
            img_name, _ = os.path.splitext(self.photo_mobile.name)
            self.photo_mobile.save(f"{img_name}.webp", ContentFile(img_io.getvalue()), save=False)
        super().save(*args, **kwargs)
        
class HomePage(models.Model):
    title = models.CharField(max_length=400, blank=True, verbose_name='title seo')
    description = models.TextField(blank=True, verbose_name='description seo')
    keywords = models.TextField(blank=True, verbose_name='keywords seo')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '0) SEO Главная'
        verbose_name_plural = '0) SEO Главная'
        ordering = ['title', ]



class ClubPageSeo(models.Model):
    title = models.CharField(max_length=400, blank=True, verbose_name='title seo')
    description = models.TextField(blank=True, verbose_name='description seo')
    keywords = models.TextField(blank=True, verbose_name='keywords seo')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '0_2) SEO Клубы page'
        verbose_name_plural = '0_2) SEO Клубы page'
        ordering = ['title', ]



class PromoPageSeo(models.Model):
    title = models.CharField(max_length=400, blank=True, verbose_name='title seo')
    description = models.TextField(blank=True, verbose_name='description seo')
    keywords = models.TextField(blank=True, verbose_name='keywords seo')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '0_3) SEO Новости '
        verbose_name_plural = '0_3) SEO Новости'
        ordering = ['title', ]




class FranchisePageSeo(models.Model):
    title = models.CharField(max_length=400, blank=True, verbose_name='title seo')
    description = models.TextField(blank=True, verbose_name='description seo')
    keywords = models.TextField(blank=True, verbose_name='keywords seo')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '0_4) SEO Франшиза'
        verbose_name_plural = '0_4) SEO Франшиза'
        ordering = ['title', ]


class ContactPageSeo(models.Model):
    title = models.CharField(max_length=400, blank=True, verbose_name='title seo')
    description = models.TextField(blank=True, verbose_name='description seo')
    keywords = models.TextField(blank=True, verbose_name='keywords seo')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '0_5) SEO Контакты'
        verbose_name_plural = '0_5) SEO Контакты'
        ordering = ['title', ]



class VdnhSeo(models.Model):
    title = models.CharField(max_length=400, blank=True, verbose_name='title seo')
    description = models.TextField(blank=True, verbose_name='description seo')
    keywords = models.TextField(blank=True, verbose_name='keywords seo')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '0_6) SEO ВДНХ'
        verbose_name_plural = '0_6) SEO ВДНХ'
        ordering = ['title', ]




class VernadkaSeo(models.Model):
    title = models.CharField(max_length=400, blank=True, verbose_name='title seo')
    description = models.TextField(blank=True, verbose_name='description seo')
    keywords = models.TextField(blank=True, verbose_name='keywords seo')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '0_7) SEO Вернадка'
        verbose_name_plural = '0_7) SEO Вернадка'
        ordering = ['title', ]



class MitinoSeo(models.Model):
    title = models.CharField(max_length=400, blank=True, verbose_name='title seo')
    description = models.TextField(blank=True, verbose_name='description seo')
    keywords = models.TextField(blank=True, verbose_name='keywords seo')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '0_8) SEO Митино'
        verbose_name_plural = '0_8) SEO Митино'
        ordering = ['title', ]



class KoptevoSeo(models.Model):
    title = models.CharField(max_length=400, blank=True, verbose_name='title seo')
    description = models.TextField(blank=True, verbose_name='description seo')
    keywords = models.TextField(blank=True, verbose_name='keywords seo')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '0_9) SEO Коптево'
        verbose_name_plural = '0_9) SEO Коптево'
        ordering = ['title', ]


class ZulebinoSeo(models.Model):
    title = models.CharField(max_length=400, blank=True, verbose_name='title seo')
    description = models.TextField(blank=True, verbose_name='description seo')
    keywords = models.TextField(blank=True, verbose_name='keywords seo')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '0_10) SEO Жулебино'
        verbose_name_plural = '0_10) SEO Жулебино'
        ordering = ['title', ]



class ZukovskySeo(models.Model):
    title = models.CharField(max_length=400, blank=True, verbose_name='title seo')
    description = models.TextField(blank=True, verbose_name='description seo')
    keywords = models.TextField(blank=True, verbose_name='keywords seo')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '0_11) SEO Жуковский'
        verbose_name_plural = '0_11) SEO Жуковский'
        ordering = ['title', ]



class SerpuhovkayaSeo(models.Model):
    title = models.CharField(max_length=400, blank=True, verbose_name='title seo')
    description = models.TextField(blank=True, verbose_name='description seo')
    keywords = models.TextField(blank=True, verbose_name='keywords seo')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '0_12) SEO Серпуховская'
        verbose_name_plural = '0_12 SEO Серпуховская'
        ordering = ['title', ]


class PushkinoSeo(models.Model):
    title = models.CharField(max_length=400, blank=True, verbose_name='title seo')
    description = models.TextField(blank=True, verbose_name='description seo')
    keywords = models.TextField(blank=True, verbose_name='keywords seo')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '0_13) SEO Пушкино'
        verbose_name_plural = '0_13 SEO Пушкино'
        ordering = ['title', ]


class MahachkalaSeo(models.Model):
    title = models.CharField(max_length=400, blank=True, verbose_name='title seo')
    description = models.TextField(blank=True, verbose_name='description seo')
    keywords = models.TextField(blank=True, verbose_name='keywords seo')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '0_14) SEO Махачкала'
        verbose_name_plural = '0_14 SEO Махачкала'
        ordering = ['title', ]

#################  SEO END #################










#################  GALLERY_BOOTOM #################

class HomeGallery(models.Model):
    photo = models.ImageField(upload_to='photos/gallery/')
    photo_mobile = models.ImageField(upload_to='photos/gallery/')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')

    def __str__(self):
        return f'{basename(self.photo.name)}'

    class Meta:
        verbose_name = '_1) GALLERY_BOOTOM Главная'
        verbose_name_plural = '_1) GALLERY_BOOTOM Главная'
        ordering = ['photo', ]



class VdnhGallery(models.Model):
    photo = models.ImageField(upload_to='photos/gallery/')
    photo_mobile = models.ImageField(upload_to='photos/gallery/')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')

    def __str__(self):
        return f'{basename(self.photo.name)}'

    class Meta:
        verbose_name = '_2) GALLERY_BOOTOM ВДНХ'
        verbose_name_plural = '_2) GALLERY_BOOTOM ВДНХ'
        ordering = ['photo', ]



class VernadkaGallery(models.Model):
    photo = models.ImageField(upload_to='photos/gallery/')
    photo_mobile = models.ImageField(upload_to='photos/gallery/')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')

    def __str__(self):
        return f'{basename(self.photo.name)}'

    class Meta:
        verbose_name = '_3) GALLERY_BOOTOM Вернадка'
        verbose_name_plural = '_3) GALLERY_BOOTOM Вернадка'
        ordering = ['photo', ]



class MitinoGallery(models.Model):
    photo = models.ImageField(upload_to='photos/gallery/')
    photo_mobile = models.ImageField(upload_to='photos/gallery/')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')

    def __str__(self):
        return f'{basename(self.photo.name)}'

    class Meta:
        verbose_name = '_4) GALLERY_BOOTOM Митино'
        verbose_name_plural = '_4) GALLERY_BOOTOM Митино'
        ordering = ['photo', ]



class SerpuhovskayaGallery(models.Model):
    photo = models.ImageField(upload_to='photos/gallery/')
    photo_mobile = models.ImageField(upload_to='photos/gallery/')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')

    def __str__(self):
        return f'{basename(self.photo.name)}'

    class Meta:
        verbose_name = '_5) GALLERY_BOOTOM Серпуховская'
        verbose_name_plural = '_5) GALLERY_BOOTOM Серпуховская'
        ordering = ['photo', ]



class KoptevoGallery(models.Model):
    photo = models.ImageField(upload_to='photos/gallery/')
    photo_mobile = models.ImageField(upload_to='photos/gallery/')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')

    def __str__(self):
        return f'{basename(self.photo.name)}'

    class Meta:
        verbose_name = '_6) GALLERY_BOOTOM Коптево'
        verbose_name_plural = '_6) GALLERY_BOOTOM Коптево'
        ordering = ['photo', ]



class ZulebinoGallery(models.Model):
    photo = models.ImageField(upload_to='photos/gallery/')
    photo_mobile = models.ImageField(upload_to='photos/gallery/')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')

    def __str__(self):
        return f'{basename(self.photo.name)}'

    class Meta:
        verbose_name = '_7) GALLERY_BOOTOM Жулебино'
        verbose_name_plural = '_7) GALLERY_BOOTOM Жулебино'
        ordering = ['photo', ]




class ZukovskyGallery(models.Model):
    photo = models.ImageField(upload_to='photos/gallery/')
    photo_mobile = models.ImageField(upload_to='photos/gallery/')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')

    def __str__(self):
        return f'{basename(self.photo.name)}'

    class Meta:
        verbose_name = '_8) GALLERY_BOOTOM Жуковский'
        verbose_name_plural = '_8) GALLERY_BOOTOM Жуковский'
        ordering = ['photo', ]



class PushkinoGallery(models.Model):
    photo = models.ImageField(upload_to='photos/gallery/')
    photo_mobile = models.ImageField(upload_to='photos/gallery/')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')

    def __str__(self):
        return f'{basename(self.photo.name)}'

    class Meta:
        verbose_name = '_9) GALLERY_BOOTOM Пушкино'
        verbose_name_plural = '_9) GALLERY_BOOTOM Пушкино'
        ordering = ['photo', ]



class MahachkalaGallery(models.Model):
    photo = models.ImageField(upload_to='photos/gallery/')
    photo_mobile = models.ImageField(upload_to='photos/gallery/')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')

    def __str__(self):
        return f'{basename(self.photo.name)}'

    class Meta:
        verbose_name = '_10) GALLERY_BOOTOM Махачкала'
        verbose_name_plural = '_10) GALLERY_BOOTOM Махачкала'
        ordering = ['photo', ]


#################  GALLERY_BOOTOM END #################











# PromoPage Part
###################################

class PromoPage(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='slug')
    photo = models.ImageField(upload_to='photos/promo/')
    photo_mobile = models.ImageField(upload_to='photos/promo/')
    short = models.TextField(blank=True, verbose_name='Короткое описание')
    descr = models.TextField(blank=True, verbose_name='Текст')
    sort = models.CharField(max_length=4, blank=True, verbose_name='Сортировка')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создание')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '1) Акция '
        verbose_name_plural = '1) Акции (Страница)'
        ordering = ['time_create', 'title']


class Categorynews(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='slug')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '1) Категория'
        verbose_name_plural = '1) Категории новостей (Страница)'
        ordering = ['name']





# News Part
###################################

class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='slug')
    photo = models.ImageField(upload_to='photos/news/')
    photo_mobile = models.ImageField(upload_to='photos/news/')
    short = models.TextField(blank=True, verbose_name='Короткое описание')
    descr = models.TextField(blank=True, verbose_name='Текст')
    sort = models.CharField(max_length=4, blank=True, verbose_name='Сортировка')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    catnews = models.ForeignKey('Categorynews', on_delete=models.PROTECT)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '1) Новость'
        verbose_name_plural = '1) Новости (Страница)'
        ordering = ['time_create', 'title']









######## News Part NEW Variant #######
###################################

class NewsNewVariant(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='slug')
    photo = models.ImageField(upload_to='photos/newsnew/')
    photo_mobile = models.ImageField(upload_to='photos/newsnew/')
    short = models.TextField(blank=True, verbose_name='Короткое описание')
    descr = models.TextField(blank=True, verbose_name='Текст')
    sort = models.CharField(max_length=4, blank=True, verbose_name='Сортировка')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    catnews = models.ManyToManyField('CategorynewsNewVariant')  # Используем ManyToManyField для связи с категориями

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '1_1_new) Новость'
        verbose_name_plural = '1_1_new) Новости (Страница)'
        ordering = ['time_create', 'title']

class CategorynewsNewVariant(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='slug')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '1_1_new) Категория'
        verbose_name_plural = '1_1_new) Категории новостей'
        ordering = ['name']





# VDNH Part
###################################

class VdnhNews(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='slug')
    photo = models.ImageField(upload_to='photos/promo/')
    photo_mobile = models.ImageField(upload_to='photos/promo/')
    short = models.TextField(blank=True, verbose_name='Короткое описание')
    descr = models.TextField(blank=True, verbose_name='Текст')
    sort = models.CharField(max_length=4, blank=True, verbose_name='Сортировка')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создание')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '2) ВДНХ Новость (Клуб)'
        verbose_name_plural = '2) ВДНХ Новости (Клуб)'
        ordering = ['time_create', 'title']


class VdnhPromo(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='slug')
    photo = models.ImageField(upload_to='photos/promo/')
    photo_mobile = models.ImageField(upload_to='photos/promo/')
    short = models.TextField(blank=True, verbose_name='Короткое описание')
    descr = models.TextField(blank=True, verbose_name='Текст')
    sort = models.CharField(max_length=4,blank=True, verbose_name='Сортировка')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создание')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '2) ВДНХ Акция (Клуб)'
        verbose_name_plural = '2) ВДНХ Акции (Клуб)'
        ordering = ['time_create', 'title']




class VdnhZones(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название игровой зоны')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='slug')
    photo = models.ImageField(upload_to='photos/zones/')
    photo_mobile = models.ImageField(upload_to='photos/zones/')


    timeone = models.CharField(max_length=255, blank=True, verbose_name='Время 1 (Понедельник-Четверг)')
    priceone = models.CharField(max_length=255, blank=True, verbose_name='Цена 1')

    timetwo = models.CharField(max_length=255, blank=True, verbose_name='Время 2 (Понедельник-Четверг)')
    prictwo = models.CharField(max_length=255, blank=True, verbose_name='Цена 2')

    timetri = models.CharField(max_length=255, blank=True, verbose_name='Время 3 (Понедельник-Четверг)')
    pricetri = models.CharField(max_length=255, blank=True, verbose_name='Цена 3')

    timefour = models.CharField(max_length=255, blank=True, verbose_name='Время 4 (Понедельник-Четверг)')
    pricefour = models.CharField(max_length=255, blank=True, verbose_name='Цена 4')

    timefive = models.CharField(max_length=255, blank=True, verbose_name='Время 5 (Понедельник-Четверг)')
    pricefive = models.CharField(max_length=255, blank=True, verbose_name='Цена 5')

    timesix = models.CharField(max_length=255, blank=True, verbose_name='Время 6 (Понедельник-Четверг)')
    pricesix = models.CharField(max_length=255, blank=True, verbose_name='Цена 6')




    weekend_timeone = models.CharField(max_length=255, blank=True, verbose_name='Время 1 (Пятница-Воскресенье)')
    weekend_priceone = models.CharField(max_length=255, blank=True, verbose_name='Цена 1')

    weekend_timetwo = models.CharField(max_length=255, blank=True, verbose_name='Время 2 (Пятница-Воскресенье)')
    weekend_prictwo = models.CharField(max_length=255, blank=True, verbose_name='Цена 2')

    weekend_timetri = models.CharField(max_length=255, blank=True, verbose_name='Время 3 (Пятница-Воскресенье)')
    weekend_pricetri = models.CharField(max_length=255, blank=True, verbose_name='Цена 3')

    weekend_timefour = models.CharField(max_length=255, blank=True, verbose_name='Время 4 (Пятница-Воскресенье)')
    weekend_pricefour = models.CharField(max_length=255, blank=True, verbose_name='Цена 4')

    weekend_timefive = models.CharField(max_length=255, blank=True, verbose_name='Время 5 (Пятница-Воскресенье)')
    weekend_pricefive = models.CharField(max_length=255, blank=True, verbose_name='Цена 5')

    weekend_timesix = models.CharField(max_length=255, blank=True, verbose_name='Время 6 (Пятница-Воскресенье)')
    weekend_pricesix = models.CharField(max_length=255, blank=True, verbose_name='Цена 6')



    monitor_tile = models.CharField(max_length=255, blank=True, verbose_name='Монитор Заголовок или др...')
    monitor = models.CharField(max_length=255, blank=True, verbose_name='Монитор(ы)')

    processor_tile = models.CharField(max_length=255, blank=True, verbose_name='Процессор Заголовок или др...')
    processor = models.CharField(max_length=255, blank=True, verbose_name='Процессор')

    videocard_tile = models.CharField(max_length=255, blank=True, verbose_name='Видеокарта Заголовок или др...')
    videocard = models.CharField(max_length=255, blank=True, verbose_name='Видеокарта')

    ozu_tile = models.CharField(max_length=255, blank=True, verbose_name='Оперативная память Заголовок или др...')
    ozu = models.CharField(max_length=255, blank=True, verbose_name='Оперативная память')

    headset_tile = models.CharField(max_length=255, blank=True, verbose_name='Гарнитура Заголовок или др...')
    headset = models.CharField(max_length=255, blank=True, verbose_name='Гарнитура')

    keyboard_tile = models.CharField(max_length=255, blank=True, verbose_name='Клавиатура Заголовок или др...')
    keyboard = models.CharField(max_length=255, blank=True, verbose_name='Клавиатура')

    mouse_tile = models.CharField(max_length=255, blank=True, verbose_name='Мышь Заголовок или др...')
    mouse = models.CharField(max_length=255, blank=True, verbose_name='Мышь')


    sort = models.CharField(max_length=4, blank=True, verbose_name='Сортировка')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создание')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '2) ВДНХ Зоны (Клуб)'
        verbose_name_plural = '2) ВДНХ Игровые Зоны (Клуб)'
        ordering = ['time_create', 'title']





# new version of zones


class VdnhZonesNew(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название игровой зоны')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='slug')


    monitor_tile = models.CharField(max_length=255, blank=True, verbose_name='Монитор Заголовок или др...')
    monitor = models.CharField(max_length=255, blank=True, verbose_name='Монитор(ы)')

    processor_tile = models.CharField(max_length=255, blank=True, verbose_name='Процессор Заголовок или др...')
    processor = models.CharField(max_length=255, blank=True, verbose_name='Процессор')

    videocard_tile = models.CharField(max_length=255, blank=True, verbose_name='Видеокарта Заголовок или др...')
    videocard = models.CharField(max_length=255, blank=True, verbose_name='Видеокарта')

    ozu_tile = models.CharField(max_length=255, blank=True, verbose_name='Оперативная память Заголовок или др...')
    ozu = models.CharField(max_length=255, blank=True, verbose_name='Оперативная память')

    headset_tile = models.CharField(max_length=255, blank=True, verbose_name='Гарнитура Заголовок или др...')
    headset = models.CharField(max_length=255, blank=True, verbose_name='Гарнитура')

    keyboard_tile = models.CharField(max_length=255, blank=True, verbose_name='Клавиатура Заголовок или др...')
    keyboard = models.CharField(max_length=255, blank=True, verbose_name='Клавиатура')

    mouse_tile = models.CharField(max_length=255, blank=True, verbose_name='Мышь Заголовок или др...')
    mouse = models.CharField(max_length=255, blank=True, verbose_name='Мышь')


    timeone = models.CharField(max_length=255, blank=True, verbose_name='Время 1 (Понедельник-Четверг)')
    priceone = models.CharField(max_length=255, blank=True, verbose_name='Цена 1')

    timetwo = models.CharField(max_length=255, blank=True, verbose_name='Время 2 (Понедельник-Четверг)')
    prictwo = models.CharField(max_length=255, blank=True, verbose_name='Цена 2')

    timetri = models.CharField(max_length=255, blank=True, verbose_name='Время 3 (Понедельник-Четверг)')
    pricetri = models.CharField(max_length=255, blank=True, verbose_name='Цена 3')

    timefour = models.CharField(max_length=255, blank=True, verbose_name='Время 4 (Понедельник-Четверг)')
    pricefour = models.CharField(max_length=255, blank=True, verbose_name='Цена 4')

    timefive = models.CharField(max_length=255, blank=True, verbose_name='Время 5 (Понедельник-Четверг)')
    pricefive = models.CharField(max_length=255, blank=True, verbose_name='Цена 5')

    timesix = models.CharField(max_length=255, blank=True, verbose_name='Время 6 (Понедельник-Четверг)')
    pricesix = models.CharField(max_length=255, blank=True, verbose_name='Цена 6')



    weekend_timeone = models.CharField(max_length=255, blank=True, verbose_name='Время 1 (Пятница-Воскресенье)')
    weekend_priceone = models.CharField(max_length=255, blank=True, verbose_name='Цена 1')

    weekend_timetwo = models.CharField(max_length=255, blank=True, verbose_name='Время 2 (Пятница-Воскресенье)')
    weekend_prictwo = models.CharField(max_length=255, blank=True, verbose_name='Цена 2')

    weekend_timetri = models.CharField(max_length=255, blank=True, verbose_name='Время 3 (Пятница-Воскресенье)')
    weekend_pricetri = models.CharField(max_length=255, blank=True, verbose_name='Цена 3')

    weekend_timefour = models.CharField(max_length=255, blank=True, verbose_name='Время 4 (Пятница-Воскресенье)')
    weekend_pricefour = models.CharField(max_length=255, blank=True, verbose_name='Цена 4')

    weekend_timefive = models.CharField(max_length=255, blank=True, verbose_name='Время 5 (Пятница-Воскресенье)')
    weekend_pricefive = models.CharField(max_length=255, blank=True, verbose_name='Цена 5')

    weekend_timesix = models.CharField(max_length=255, blank=True, verbose_name='Время 6 (Пятница-Воскресенье)')
    weekend_pricesix = models.CharField(max_length=255, blank=True, verbose_name='Цена 6')


    sort = models.CharField(max_length=4, blank=True, verbose_name='Сортировка')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создание')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '2new) ВДНХ Зоны new (new)'
        verbose_name_plural = '2new) ВДНХ Игровые Зоны (new)'
        ordering = ['time_create', 'title']




class ZonesVdnhPics(models.Model):
    zone = models.ForeignKey(VdnhZonesNew, related_name='zone_pics', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/zonesvdnhpics/')
    photo_mobile = models.ImageField(upload_to='photos/zonesvdnhpics/')
    sort = models.CharField(max_length=4, blank=True, verbose_name='Сортировка')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')

    def __str__(self):
        return f"{self.zone.title} - {self.photo}"

    class Meta:
        verbose_name = '2_new) Картинки zones ВДНХ'
        verbose_name_plural = '2_new) Картинки zones ВДНХ'
        ordering = ['zone', 'id']














# vernadka Part
###################################

class VernadkaNews(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='slug')
    photo = models.ImageField(upload_to='photos/promo/')
    photo_mobile = models.ImageField(upload_to='photos/promo/')
    short = models.TextField(blank=True, verbose_name='Короткое описание')
    descr = models.TextField(blank=True, verbose_name='Текст')
    sort = models.CharField(max_length=4, blank=True, verbose_name='Сортировка')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создание')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '3) Вернадка Новость (Клуб)'
        verbose_name_plural = '3) Вернадка Новости (Клуб)'
        ordering = ['time_create', 'title']




class VernadkaPromo(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='slug')
    photo = models.ImageField(upload_to='photos/promo/')
    photo_mobile = models.ImageField(upload_to='photos/promo/')
    short = models.TextField(blank=True, verbose_name='Короткое описание')
    descr = models.TextField(blank=True, verbose_name='Текст')
    sort = models.CharField(max_length=4,blank=True, verbose_name='Сортировка')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создание')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '3) Вернадка Акция (Клуб)'
        verbose_name_plural = '3) Вернадка Акции (Клуб)'
        ordering = ['time_create', 'title']





class VernadkaZones(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название игровой зоны')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='slug')
    photo = models.ImageField(upload_to='photos/zones/')
    photo_mobile = models.ImageField(upload_to='photos/zones/')


    timeone = models.CharField(max_length=255, blank=True, verbose_name='Время 1 (Понедельник-Четверг)')
    priceone = models.CharField(max_length=255, blank=True, verbose_name='Цена 1')

    timetwo = models.CharField(max_length=255, blank=True, verbose_name='Время 2 (Понедельник-Четверг)')
    prictwo = models.CharField(max_length=255, blank=True, verbose_name='Цена 2')

    timetri = models.CharField(max_length=255, blank=True, verbose_name='Время 3 (Понедельник-Четверг)')
    pricetri = models.CharField(max_length=255, blank=True, verbose_name='Цена 3')

    timefour = models.CharField(max_length=255, blank=True, verbose_name='Время 4 (Понедельник-Четверг)')
    pricefour = models.CharField(max_length=255, blank=True, verbose_name='Цена 4')

    timefive = models.CharField(max_length=255, blank=True, verbose_name='Время 5 (Понедельник-Четверг)')
    pricefive = models.CharField(max_length=255, blank=True, verbose_name='Цена 5')

    timesix = models.CharField(max_length=255, blank=True, verbose_name='Время 6 (Понедельник-Четверг)')
    pricesix = models.CharField(max_length=255, blank=True, verbose_name='Цена 6')




    weekend_timeone = models.CharField(max_length=255, blank=True, verbose_name='Время 1 (Пятница-Воскресенье)')
    weekend_priceone = models.CharField(max_length=255, blank=True, verbose_name='Цена 1')

    weekend_timetwo = models.CharField(max_length=255, blank=True, verbose_name='Время 2 (Пятница-Воскресенье)')
    weekend_prictwo = models.CharField(max_length=255, blank=True, verbose_name='Цена 2')

    weekend_timetri = models.CharField(max_length=255, blank=True, verbose_name='Время 3 (Пятница-Воскресенье)')
    weekend_pricetri = models.CharField(max_length=255, blank=True, verbose_name='Цена 3')

    weekend_timefour = models.CharField(max_length=255, blank=True, verbose_name='Время 4 (Пятница-Воскресенье)')
    weekend_pricefour = models.CharField(max_length=255, blank=True, verbose_name='Цена 4')

    weekend_timefive = models.CharField(max_length=255, blank=True, verbose_name='Время 5 (Пятница-Воскресенье)')
    weekend_pricefive = models.CharField(max_length=255, blank=True, verbose_name='Цена 5')

    weekend_timesix = models.CharField(max_length=255, blank=True, verbose_name='Время 6 (Пятница-Воскресенье)')
    weekend_pricesix = models.CharField(max_length=255, blank=True, verbose_name='Цена 6')



    monitor_tile = models.CharField(max_length=255, blank=True, verbose_name='Монитор Заголовок или др...')
    monitor = models.CharField(max_length=255, blank=True, verbose_name='Монитор(ы)')

    processor_tile = models.CharField(max_length=255, blank=True, verbose_name='Процессор Заголовок или др...')
    processor = models.CharField(max_length=255, blank=True, verbose_name='Процессор')

    videocard_tile = models.CharField(max_length=255, blank=True, verbose_name='Видеокарта Заголовок или др...')
    videocard = models.CharField(max_length=255, blank=True, verbose_name='Видеокарта')

    ozu_tile = models.CharField(max_length=255, blank=True, verbose_name='Оперативная память Заголовок или др...')
    ozu = models.CharField(max_length=255, blank=True, verbose_name='Оперативная память')

    headset_tile = models.CharField(max_length=255, blank=True, verbose_name='Гарнитура Заголовок или др...')
    headset = models.CharField(max_length=255, blank=True, verbose_name='Гарнитура')

    keyboard_tile = models.CharField(max_length=255, blank=True, verbose_name='Клавиатура Заголовок или др...')
    keyboard = models.CharField(max_length=255, blank=True, verbose_name='Клавиатура')

    mouse_tile = models.CharField(max_length=255, blank=True, verbose_name='Мышь Заголовок или др...')
    mouse = models.CharField(max_length=255, blank=True, verbose_name='Мышь')


    sort = models.CharField(max_length=4, blank=True, verbose_name='Сортировка')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создание')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '3) Вернадка Зоны (Клуб)'
        verbose_name_plural = '3) Вернадка Игровые Зоны (Клуб)'
        ordering = ['time_create', 'title']







# new version


class VernadkaZonesNew(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название игровой зоны')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='slug')


    monitor_tile = models.CharField(max_length=255, blank=True, verbose_name='Монитор Заголовок или др...')
    monitor = models.CharField(max_length=255, blank=True, verbose_name='Монитор(ы)')

    processor_tile = models.CharField(max_length=255, blank=True, verbose_name='Процессор Заголовок или др...')
    processor = models.CharField(max_length=255, blank=True, verbose_name='Процессор')

    videocard_tile = models.CharField(max_length=255, blank=True, verbose_name='Видеокарта Заголовок или др...')
    videocard = models.CharField(max_length=255, blank=True, verbose_name='Видеокарта')

    ozu_tile = models.CharField(max_length=255, blank=True, verbose_name='Оперативная память Заголовок или др...')
    ozu = models.CharField(max_length=255, blank=True, verbose_name='Оперативная память')

    headset_tile = models.CharField(max_length=255, blank=True, verbose_name='Гарнитура Заголовок или др...')
    headset = models.CharField(max_length=255, blank=True, verbose_name='Гарнитура')

    keyboard_tile = models.CharField(max_length=255, blank=True, verbose_name='Клавиатура Заголовок или др...')
    keyboard = models.CharField(max_length=255, blank=True, verbose_name='Клавиатура')

    mouse_tile = models.CharField(max_length=255, blank=True, verbose_name='Мышь Заголовок или др...')
    mouse = models.CharField(max_length=255, blank=True, verbose_name='Мышь')


    timeone = models.CharField(max_length=255, blank=True, verbose_name='Время 1 (Понедельник-Четверг)')
    priceone = models.CharField(max_length=255, blank=True, verbose_name='Цена 1')

    timetwo = models.CharField(max_length=255, blank=True, verbose_name='Время 2 (Понедельник-Четверг)')
    prictwo = models.CharField(max_length=255, blank=True, verbose_name='Цена 2')

    timetri = models.CharField(max_length=255, blank=True, verbose_name='Время 3 (Понедельник-Четверг)')
    pricetri = models.CharField(max_length=255, blank=True, verbose_name='Цена 3')

    timefour = models.CharField(max_length=255, blank=True, verbose_name='Время 4 (Понедельник-Четверг)')
    pricefour = models.CharField(max_length=255, blank=True, verbose_name='Цена 4')

    timefive = models.CharField(max_length=255, blank=True, verbose_name='Время 5 (Понедельник-Четверг)')
    pricefive = models.CharField(max_length=255, blank=True, verbose_name='Цена 5')

    timesix = models.CharField(max_length=255, blank=True, verbose_name='Время 6 (Понедельник-Четверг)')
    pricesix = models.CharField(max_length=255, blank=True, verbose_name='Цена 6')



    weekend_timeone = models.CharField(max_length=255, blank=True, verbose_name='Время 1 (Пятница-Воскресенье)')
    weekend_priceone = models.CharField(max_length=255, blank=True, verbose_name='Цена 1')

    weekend_timetwo = models.CharField(max_length=255, blank=True, verbose_name='Время 2 (Пятница-Воскресенье)')
    weekend_prictwo = models.CharField(max_length=255, blank=True, verbose_name='Цена 2')

    weekend_timetri = models.CharField(max_length=255, blank=True, verbose_name='Время 3 (Пятница-Воскресенье)')
    weekend_pricetri = models.CharField(max_length=255, blank=True, verbose_name='Цена 3')

    weekend_timefour = models.CharField(max_length=255, blank=True, verbose_name='Время 4 (Пятница-Воскресенье)')
    weekend_pricefour = models.CharField(max_length=255, blank=True, verbose_name='Цена 4')

    weekend_timefive = models.CharField(max_length=255, blank=True, verbose_name='Время 5 (Пятница-Воскресенье)')
    weekend_pricefive = models.CharField(max_length=255, blank=True, verbose_name='Цена 5')

    weekend_timesix = models.CharField(max_length=255, blank=True, verbose_name='Время 6 (Пятница-Воскресенье)')
    weekend_pricesix = models.CharField(max_length=255, blank=True, verbose_name='Цена 6')


    sort = models.CharField(max_length=4, blank=True, verbose_name='Сортировка')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создание')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '3new) Вернадка Зоны new (new)'
        verbose_name_plural = '3new) Вернадка Игровые Зоны (new)'
        ordering = ['time_create', 'title']






class ZonesVernadkaPics(models.Model):
    zone = models.ForeignKey(VernadkaZonesNew, related_name='zone_pics', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/zonesvernadkapics/')
    photo_mobile = models.ImageField(upload_to='photos/zonesvernadkapics/')
    sort = models.CharField(max_length=4, blank=True, verbose_name='Сортировка')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')

    def __str__(self):
        return f"{self.zone.title} - {self.photo}"

    class Meta:
        verbose_name = '3_new) Картинки zones Вернадка'
        verbose_name_plural = '3_new) Картинки zones Вернадка'
        ordering = ['zone', 'id']









# Mitino Part
###################################

class MitinoNews(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='slug')
    photo = models.ImageField(upload_to='photos/promo/')
    photo_mobile = models.ImageField(upload_to='photos/promo/')
    short = models.TextField(blank=True, verbose_name='Короткое описание')
    descr = models.TextField(blank=True, verbose_name='Текст')
    sort = models.CharField(max_length=4, blank=True, verbose_name='Сортировка')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создание')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '4) Митино Новость (Клуб)'
        verbose_name_plural = '4) Митино Новости (Клуб)'
        ordering = ['time_create', 'title']




class MitinoPromo(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='slug')
    photo = models.ImageField(upload_to='photos/promo/')
    photo_mobile = models.ImageField(upload_to='photos/promo/')
    short = models.TextField(blank=True, verbose_name='Короткое описание')
    descr = models.TextField(blank=True, verbose_name='Текст')
    sort = models.CharField(max_length=4,blank=True, verbose_name='Сортировка')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создание')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '4) Митино Акция (Клуб)'
        verbose_name_plural = '4) Митино Акции (Клуб)'
        ordering = ['time_create', 'title']





class MitinoZones(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название игровой зоны')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='slug')
    photo = models.ImageField(upload_to='photos/zones/')
    photo_mobile = models.ImageField(upload_to='photos/zones/')


    timeone = models.CharField(max_length=255, blank=True, verbose_name='Время 1 (Понедельник-Четверг)')
    priceone = models.CharField(max_length=255, blank=True, verbose_name='Цена 1')

    timetwo = models.CharField(max_length=255, blank=True, verbose_name='Время 2 (Понедельник-Четверг)')
    prictwo = models.CharField(max_length=255, blank=True, verbose_name='Цена 2')

    timetri = models.CharField(max_length=255, blank=True, verbose_name='Время 3 (Понедельник-Четверг)')
    pricetri = models.CharField(max_length=255, blank=True, verbose_name='Цена 3')

    timefour = models.CharField(max_length=255, blank=True, verbose_name='Время 4 (Понедельник-Четверг)')
    pricefour = models.CharField(max_length=255, blank=True, verbose_name='Цена 4')

    timefive = models.CharField(max_length=255, blank=True, verbose_name='Время 5 (Понедельник-Четверг)')
    pricefive = models.CharField(max_length=255, blank=True, verbose_name='Цена 5')

    timesix = models.CharField(max_length=255, blank=True, verbose_name='Время 6 (Понедельник-Четверг)')
    pricesix = models.CharField(max_length=255, blank=True, verbose_name='Цена 6')




    weekend_timeone = models.CharField(max_length=255, blank=True, verbose_name='Время 1 (Пятница-Воскресенье)')
    weekend_priceone = models.CharField(max_length=255, blank=True, verbose_name='Цена 1')

    weekend_timetwo = models.CharField(max_length=255, blank=True, verbose_name='Время 2 (Пятница-Воскресенье)')
    weekend_prictwo = models.CharField(max_length=255, blank=True, verbose_name='Цена 2')

    weekend_timetri = models.CharField(max_length=255, blank=True, verbose_name='Время 3 (Пятница-Воскресенье)')
    weekend_pricetri = models.CharField(max_length=255, blank=True, verbose_name='Цена 3')

    weekend_timefour = models.CharField(max_length=255, blank=True, verbose_name='Время 4 (Пятница-Воскресенье)')
    weekend_pricefour = models.CharField(max_length=255, blank=True, verbose_name='Цена 4')

    weekend_timefive = models.CharField(max_length=255, blank=True, verbose_name='Время 5 (Пятница-Воскресенье)')
    weekend_pricefive = models.CharField(max_length=255, blank=True, verbose_name='Цена 5')

    weekend_timesix = models.CharField(max_length=255, blank=True, verbose_name='Время 6 (Пятница-Воскресенье)')
    weekend_pricesix = models.CharField(max_length=255, blank=True, verbose_name='Цена 6')



    monitor_tile = models.CharField(max_length=255, blank=True, verbose_name='Монитор Заголовок или др...')
    monitor = models.CharField(max_length=255, blank=True, verbose_name='Монитор(ы)')

    processor_tile = models.CharField(max_length=255, blank=True, verbose_name='Процессор Заголовок или др...')
    processor = models.CharField(max_length=255, blank=True, verbose_name='Процессор')

    videocard_tile = models.CharField(max_length=255, blank=True, verbose_name='Видеокарта Заголовок или др...')
    videocard = models.CharField(max_length=255, blank=True, verbose_name='Видеокарта')

    ozu_tile = models.CharField(max_length=255, blank=True, verbose_name='Оперативная память Заголовок или др...')
    ozu = models.CharField(max_length=255, blank=True, verbose_name='Оперативная память')

    headset_tile = models.CharField(max_length=255, blank=True, verbose_name='Гарнитура Заголовок или др...')
    headset = models.CharField(max_length=255, blank=True, verbose_name='Гарнитура')

    keyboard_tile = models.CharField(max_length=255, blank=True, verbose_name='Клавиатура Заголовок или др...')
    keyboard = models.CharField(max_length=255, blank=True, verbose_name='Клавиатура')

    mouse_tile = models.CharField(max_length=255, blank=True, verbose_name='Мышь Заголовок или др...')
    mouse = models.CharField(max_length=255, blank=True, verbose_name='Мышь')


    sort = models.CharField(max_length=4, blank=True, verbose_name='Сортировка')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создание')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '4) Митино Зоны (Клуб)'
        verbose_name_plural = '4) Митино Игровые Зоны (Клуб)'
        ordering = ['time_create', 'title']






# new version of zones


class MitinoZonesNew(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название игровой зоны')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='slug')


    monitor_tile = models.CharField(max_length=255, blank=True, verbose_name='Монитор Заголовок или др...')
    monitor = models.CharField(max_length=255, blank=True, verbose_name='Монитор(ы)')

    processor_tile = models.CharField(max_length=255, blank=True, verbose_name='Процессор Заголовок или др...')
    processor = models.CharField(max_length=255, blank=True, verbose_name='Процессор')

    videocard_tile = models.CharField(max_length=255, blank=True, verbose_name='Видеокарта Заголовок или др...')
    videocard = models.CharField(max_length=255, blank=True, verbose_name='Видеокарта')

    ozu_tile = models.CharField(max_length=255, blank=True, verbose_name='Оперативная память Заголовок или др...')
    ozu = models.CharField(max_length=255, blank=True, verbose_name='Оперативная память')

    headset_tile = models.CharField(max_length=255, blank=True, verbose_name='Гарнитура Заголовок или др...')
    headset = models.CharField(max_length=255, blank=True, verbose_name='Гарнитура')

    keyboard_tile = models.CharField(max_length=255, blank=True, verbose_name='Клавиатура Заголовок или др...')
    keyboard = models.CharField(max_length=255, blank=True, verbose_name='Клавиатура')

    mouse_tile = models.CharField(max_length=255, blank=True, verbose_name='Мышь Заголовок или др...')
    mouse = models.CharField(max_length=255, blank=True, verbose_name='Мышь')


    timeone = models.CharField(max_length=255, blank=True, verbose_name='Время 1 (Понедельник-Четверг)')
    priceone = models.CharField(max_length=255, blank=True, verbose_name='Цена 1')

    timetwo = models.CharField(max_length=255, blank=True, verbose_name='Время 2 (Понедельник-Четверг)')
    prictwo = models.CharField(max_length=255, blank=True, verbose_name='Цена 2')

    timetri = models.CharField(max_length=255, blank=True, verbose_name='Время 3 (Понедельник-Четверг)')
    pricetri = models.CharField(max_length=255, blank=True, verbose_name='Цена 3')

    timefour = models.CharField(max_length=255, blank=True, verbose_name='Время 4 (Понедельник-Четверг)')
    pricefour = models.CharField(max_length=255, blank=True, verbose_name='Цена 4')

    timefive = models.CharField(max_length=255, blank=True, verbose_name='Время 5 (Понедельник-Четверг)')
    pricefive = models.CharField(max_length=255, blank=True, verbose_name='Цена 5')

    timesix = models.CharField(max_length=255, blank=True, verbose_name='Время 6 (Понедельник-Четверг)')
    pricesix = models.CharField(max_length=255, blank=True, verbose_name='Цена 6')



    weekend_timeone = models.CharField(max_length=255, blank=True, verbose_name='Время 1 (Пятница-Воскресенье)')
    weekend_priceone = models.CharField(max_length=255, blank=True, verbose_name='Цена 1')

    weekend_timetwo = models.CharField(max_length=255, blank=True, verbose_name='Время 2 (Пятница-Воскресенье)')
    weekend_prictwo = models.CharField(max_length=255, blank=True, verbose_name='Цена 2')

    weekend_timetri = models.CharField(max_length=255, blank=True, verbose_name='Время 3 (Пятница-Воскресенье)')
    weekend_pricetri = models.CharField(max_length=255, blank=True, verbose_name='Цена 3')

    weekend_timefour = models.CharField(max_length=255, blank=True, verbose_name='Время 4 (Пятница-Воскресенье)')
    weekend_pricefour = models.CharField(max_length=255, blank=True, verbose_name='Цена 4')

    weekend_timefive = models.CharField(max_length=255, blank=True, verbose_name='Время 5 (Пятница-Воскресенье)')
    weekend_pricefive = models.CharField(max_length=255, blank=True, verbose_name='Цена 5')

    weekend_timesix = models.CharField(max_length=255, blank=True, verbose_name='Время 6 (Пятница-Воскресенье)')
    weekend_pricesix = models.CharField(max_length=255, blank=True, verbose_name='Цена 6')


    sort = models.CharField(max_length=4, blank=True, verbose_name='Сортировка')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создание')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '4new) Митино Зоны new (new)'
        verbose_name_plural = '4new) Митино Игровые Зоны (new)'
        ordering = ['time_create', 'title']




class ZonesMitinoPics(models.Model):
    zone = models.ForeignKey(MitinoZonesNew, related_name='zone_pics', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/zonesmitinopics/')
    photo_mobile = models.ImageField(upload_to='photos/zonesmitinopics/')
    sort = models.CharField(max_length=4, blank=True, verbose_name='Сортировка')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')

    def __str__(self):
        return f"{self.zone.title} - {self.photo}"

    class Meta:
        verbose_name = '4_new) Картинки zones Митино'
        verbose_name_plural = '4_new) Картинки zones Митино'
        ordering = ['zone', 'id']









# Koptevo Part
###################################

class KoptevoNews(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='slug')
    photo = models.ImageField(upload_to='photos/promo/')
    photo_mobile = models.ImageField(upload_to='photos/promo/')
    short = models.TextField(blank=True, verbose_name='Короткое описание')
    descr = models.TextField(blank=True, verbose_name='Текст')
    sort = models.CharField(max_length=4, blank=True, verbose_name='Сортировка')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создание')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '5) Коптево Новость (Клуб)'
        verbose_name_plural = '5) Коптево Новости (Клуб)'
        ordering = ['time_create', 'title']


class KoptevoPromo(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='slug')
    photo = models.ImageField(upload_to='photos/promo/')
    photo_mobile = models.ImageField(upload_to='photos/promo/')
    short = models.TextField(blank=True, verbose_name='Короткое описание')
    descr = models.TextField(blank=True, verbose_name='Текст')
    sort = models.CharField(max_length=4,blank=True, verbose_name='Сортировка')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создание')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '5) Коптево Акция (Клуб)'
        verbose_name_plural = '5) Коптево Акции (Клуб)'
        ordering = ['time_create', 'title']








class KoptevoZones(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название игровой зоны')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='slug')
    photo = models.ImageField(upload_to='photos/zones/')
    photo_mobile = models.ImageField(upload_to='photos/zones/')


    timeone = models.CharField(max_length=255, blank=True, verbose_name='Время 1 (Понедельник-Четверг)')
    priceone = models.CharField(max_length=255, blank=True, verbose_name='Цена 1')

    timetwo = models.CharField(max_length=255, blank=True, verbose_name='Время 2 (Понедельник-Четверг)')
    prictwo = models.CharField(max_length=255, blank=True, verbose_name='Цена 2')

    timetri = models.CharField(max_length=255, blank=True, verbose_name='Время 3 (Понедельник-Четверг)')
    pricetri = models.CharField(max_length=255, blank=True, verbose_name='Цена 3')

    timefour = models.CharField(max_length=255, blank=True, verbose_name='Время 4 (Понедельник-Четверг)')
    pricefour = models.CharField(max_length=255, blank=True, verbose_name='Цена 4')

    timefive = models.CharField(max_length=255, blank=True, verbose_name='Время 5 (Понедельник-Четверг)')
    pricefive = models.CharField(max_length=255, blank=True, verbose_name='Цена 5')

    timesix = models.CharField(max_length=255, blank=True, verbose_name='Время 6 (Понедельник-Четверг)')
    pricesix = models.CharField(max_length=255, blank=True, verbose_name='Цена 6')




    weekend_timeone = models.CharField(max_length=255, blank=True, verbose_name='Время 1 (Пятница-Воскресенье)')
    weekend_priceone = models.CharField(max_length=255, blank=True, verbose_name='Цена 1')

    weekend_timetwo = models.CharField(max_length=255, blank=True, verbose_name='Время 2 (Пятница-Воскресенье)')
    weekend_prictwo = models.CharField(max_length=255, blank=True, verbose_name='Цена 2')

    weekend_timetri = models.CharField(max_length=255, blank=True, verbose_name='Время 3 (Пятница-Воскресенье)')
    weekend_pricetri = models.CharField(max_length=255, blank=True, verbose_name='Цена 3')

    weekend_timefour = models.CharField(max_length=255, blank=True, verbose_name='Время 4 (Пятница-Воскресенье)')
    weekend_pricefour = models.CharField(max_length=255, blank=True, verbose_name='Цена 4')

    weekend_timefive = models.CharField(max_length=255, blank=True, verbose_name='Время 5 (Пятница-Воскресенье)')
    weekend_pricefive = models.CharField(max_length=255, blank=True, verbose_name='Цена 5')

    weekend_timesix = models.CharField(max_length=255, blank=True, verbose_name='Время 6 (Пятница-Воскресенье)')
    weekend_pricesix = models.CharField(max_length=255, blank=True, verbose_name='Цена 6')



    monitor_tile = models.CharField(max_length=255, blank=True, verbose_name='Монитор Заголовок или др...')
    monitor = models.CharField(max_length=255, blank=True, verbose_name='Монитор(ы)')

    processor_tile = models.CharField(max_length=255, blank=True, verbose_name='Процессор Заголовок или др...')
    processor = models.CharField(max_length=255, blank=True, verbose_name='Процессор')

    videocard_tile = models.CharField(max_length=255, blank=True, verbose_name='Видеокарта Заголовок или др...')
    videocard = models.CharField(max_length=255, blank=True, verbose_name='Видеокарта')

    ozu_tile = models.CharField(max_length=255, blank=True, verbose_name='Оперативная память Заголовок или др...')
    ozu = models.CharField(max_length=255, blank=True, verbose_name='Оперативная память')

    headset_tile = models.CharField(max_length=255, blank=True, verbose_name='Гарнитура Заголовок или др...')
    headset = models.CharField(max_length=255, blank=True, verbose_name='Гарнитура')

    keyboard_tile = models.CharField(max_length=255, blank=True, verbose_name='Клавиатура Заголовок или др...')
    keyboard = models.CharField(max_length=255, blank=True, verbose_name='Клавиатура')

    mouse_tile = models.CharField(max_length=255, blank=True, verbose_name='Мышь Заголовок или др...')
    mouse = models.CharField(max_length=255, blank=True, verbose_name='Мышь')


    sort = models.CharField(max_length=4, blank=True, verbose_name='Сортировка')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создание')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '5) Коптево Зоны (Клуб)'
        verbose_name_plural = '5) Коптево Игровые Зоны (Клуб)'
        ordering = ['time_create', 'title']












# Zulebino Part
###################################

class ZulebinoNews(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='slug')
    photo = models.ImageField(upload_to='photos/promo/')
    photo_mobile = models.ImageField(upload_to='photos/promo/')
    short = models.TextField(blank=True, verbose_name='Короткое описание')
    descr = models.TextField(blank=True, verbose_name='Текст')
    sort = models.CharField(max_length=4, blank=True, verbose_name='Сортировка')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создание')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '6) Жулебино Новость (Клуб)'
        verbose_name_plural = '6) Жулебино Новости (Клуб)'
        ordering = ['time_create', 'title']



class ZulebinoPromo(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='slug')
    photo = models.ImageField(upload_to='photos/promo/')
    photo_mobile = models.ImageField(upload_to='photos/promo/')
    short = models.TextField(blank=True, verbose_name='Короткое описание')
    descr = models.TextField(blank=True, verbose_name='Текст')
    sort = models.CharField(max_length=4,blank=True, verbose_name='Сортировка')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создание')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '6) Жулебино Акция (Клуб)'
        verbose_name_plural = '6) Жулебино Акции (Клуб)'
        ordering = ['time_create', 'title']






class ZulebinoZones(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название игровой зоны')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='slug')
    photo = models.ImageField(upload_to='photos/zones/')
    photo_mobile = models.ImageField(upload_to='photos/zones/')


    timeone = models.CharField(max_length=255, blank=True, verbose_name='Время 1 (Понедельник-Четверг)')
    priceone = models.CharField(max_length=255, blank=True, verbose_name='Цена 1')

    timetwo = models.CharField(max_length=255, blank=True, verbose_name='Время 2 (Понедельник-Четверг)')
    prictwo = models.CharField(max_length=255, blank=True, verbose_name='Цена 2')

    timetri = models.CharField(max_length=255, blank=True, verbose_name='Время 3 (Понедельник-Четверг)')
    pricetri = models.CharField(max_length=255, blank=True, verbose_name='Цена 3')

    timefour = models.CharField(max_length=255, blank=True, verbose_name='Время 4 (Понедельник-Четверг)')
    pricefour = models.CharField(max_length=255, blank=True, verbose_name='Цена 4')

    timefive = models.CharField(max_length=255, blank=True, verbose_name='Время 5 (Понедельник-Четверг)')
    pricefive = models.CharField(max_length=255, blank=True, verbose_name='Цена 5')

    timesix = models.CharField(max_length=255, blank=True, verbose_name='Время 6 (Понедельник-Четверг)')
    pricesix = models.CharField(max_length=255, blank=True, verbose_name='Цена 6')




    weekend_timeone = models.CharField(max_length=255, blank=True, verbose_name='Время 1 (Пятница-Воскресенье)')
    weekend_priceone = models.CharField(max_length=255, blank=True, verbose_name='Цена 1')

    weekend_timetwo = models.CharField(max_length=255, blank=True, verbose_name='Время 2 (Пятница-Воскресенье)')
    weekend_prictwo = models.CharField(max_length=255, blank=True, verbose_name='Цена 2')

    weekend_timetri = models.CharField(max_length=255, blank=True, verbose_name='Время 3 (Пятница-Воскресенье)')
    weekend_pricetri = models.CharField(max_length=255, blank=True, verbose_name='Цена 3')

    weekend_timefour = models.CharField(max_length=255, blank=True, verbose_name='Время 4 (Пятница-Воскресенье)')
    weekend_pricefour = models.CharField(max_length=255, blank=True, verbose_name='Цена 4')

    weekend_timefive = models.CharField(max_length=255, blank=True, verbose_name='Время 5 (Пятница-Воскресенье)')
    weekend_pricefive = models.CharField(max_length=255, blank=True, verbose_name='Цена 5')

    weekend_timesix = models.CharField(max_length=255, blank=True, verbose_name='Время 6 (Пятница-Воскресенье)')
    weekend_pricesix = models.CharField(max_length=255, blank=True, verbose_name='Цена 6')



    monitor_tile = models.CharField(max_length=255, blank=True, verbose_name='Монитор Заголовок или др...')
    monitor = models.CharField(max_length=255, blank=True, verbose_name='Монитор(ы)')

    processor_tile = models.CharField(max_length=255, blank=True, verbose_name='Процессор Заголовок или др...')
    processor = models.CharField(max_length=255, blank=True, verbose_name='Процессор')

    videocard_tile = models.CharField(max_length=255, blank=True, verbose_name='Видеокарта Заголовок или др...')
    videocard = models.CharField(max_length=255, blank=True, verbose_name='Видеокарта')

    ozu_tile = models.CharField(max_length=255, blank=True, verbose_name='Оперативная память Заголовок или др...')
    ozu = models.CharField(max_length=255, blank=True, verbose_name='Оперативная память')

    headset_tile = models.CharField(max_length=255, blank=True, verbose_name='Гарнитура Заголовок или др...')
    headset = models.CharField(max_length=255, blank=True, verbose_name='Гарнитура')

    keyboard_tile = models.CharField(max_length=255, blank=True, verbose_name='Клавиатура Заголовок или др...')
    keyboard = models.CharField(max_length=255, blank=True, verbose_name='Клавиатура')

    mouse_tile = models.CharField(max_length=255, blank=True, verbose_name='Мышь Заголовок или др...')
    mouse = models.CharField(max_length=255, blank=True, verbose_name='Мышь')


    sort = models.CharField(max_length=4, blank=True, verbose_name='Сортировка')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создание')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '6) Жулебино Зоны (Клуб)'
        verbose_name_plural = '6) Жулебино Игровые Зоны (Клуб)'
        ordering = ['time_create', 'title']









# Zukovsky Part
###################################

class ZukovskyNews(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='slug')
    photo = models.ImageField(upload_to='photos/promo/')
    photo_mobile = models.ImageField(upload_to='photos/promo/')
    short = models.TextField(blank=True, verbose_name='Короткое описание')
    descr = models.TextField(blank=True, verbose_name='Текст')
    sort = models.CharField(max_length=4, blank=True, verbose_name='Сортировка')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создание')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '7) Жуковский Новость (Клуб)'
        verbose_name_plural = '7) Жуковский Новости (Клуб)'
        ordering = ['time_create', 'title']



class ZukovskyPromo(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='slug')
    photo = models.ImageField(upload_to='photos/promo/')
    photo_mobile = models.ImageField(upload_to='photos/promo/')
    short = models.TextField(blank=True, verbose_name='Короткое описание')
    descr = models.TextField(blank=True, verbose_name='Текст')
    sort = models.CharField(max_length=4,blank=True, verbose_name='Сортировка')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создание')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '7) Жуковский Акция (Клуб)'
        verbose_name_plural = '7) Жуковский Акции (Клуб)'
        ordering = ['time_create', 'title']






class ZukovskyZones(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название игровой зоны')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='slug')
    photo = models.ImageField(upload_to='photos/zones/')
    photo_mobile = models.ImageField(upload_to='photos/zones/')


    timeone = models.CharField(max_length=255, blank=True, verbose_name='Время 1 (Понедельник-Четверг)')
    priceone = models.CharField(max_length=255, blank=True, verbose_name='Цена 1')

    timetwo = models.CharField(max_length=255, blank=True, verbose_name='Время 2 (Понедельник-Четверг)')
    prictwo = models.CharField(max_length=255, blank=True, verbose_name='Цена 2')

    timetri = models.CharField(max_length=255, blank=True, verbose_name='Время 3 (Понедельник-Четверг)')
    pricetri = models.CharField(max_length=255, blank=True, verbose_name='Цена 3')

    timefour = models.CharField(max_length=255, blank=True, verbose_name='Время 4 (Понедельник-Четверг)')
    pricefour = models.CharField(max_length=255, blank=True, verbose_name='Цена 4')

    timefive = models.CharField(max_length=255, blank=True, verbose_name='Время 5 (Понедельник-Четверг)')
    pricefive = models.CharField(max_length=255, blank=True, verbose_name='Цена 5')

    timesix = models.CharField(max_length=255, blank=True, verbose_name='Время 6 (Понедельник-Четверг)')
    pricesix = models.CharField(max_length=255, blank=True, verbose_name='Цена 6')




    weekend_timeone = models.CharField(max_length=255, blank=True, verbose_name='Время 1 (Пятница-Воскресенье)')
    weekend_priceone = models.CharField(max_length=255, blank=True, verbose_name='Цена 1')

    weekend_timetwo = models.CharField(max_length=255, blank=True, verbose_name='Время 2 (Пятница-Воскресенье)')
    weekend_prictwo = models.CharField(max_length=255, blank=True, verbose_name='Цена 2')

    weekend_timetri = models.CharField(max_length=255, blank=True, verbose_name='Время 3 (Пятница-Воскресенье)')
    weekend_pricetri = models.CharField(max_length=255, blank=True, verbose_name='Цена 3')

    weekend_timefour = models.CharField(max_length=255, blank=True, verbose_name='Время 4 (Пятница-Воскресенье)')
    weekend_pricefour = models.CharField(max_length=255, blank=True, verbose_name='Цена 4')

    weekend_timefive = models.CharField(max_length=255, blank=True, verbose_name='Время 5 (Пятница-Воскресенье)')
    weekend_pricefive = models.CharField(max_length=255, blank=True, verbose_name='Цена 5')

    weekend_timesix = models.CharField(max_length=255, blank=True, verbose_name='Время 6 (Пятница-Воскресенье)')
    weekend_pricesix = models.CharField(max_length=255, blank=True, verbose_name='Цена 6')



    monitor_tile = models.CharField(max_length=255, blank=True, verbose_name='Монитор Заголовок или др...')
    monitor = models.CharField(max_length=255, blank=True, verbose_name='Монитор(ы)')

    processor_tile = models.CharField(max_length=255, blank=True, verbose_name='Процессор Заголовок или др...')
    processor = models.CharField(max_length=255, blank=True, verbose_name='Процессор')

    videocard_tile = models.CharField(max_length=255, blank=True, verbose_name='Видеокарта Заголовок или др...')
    videocard = models.CharField(max_length=255, blank=True, verbose_name='Видеокарта')

    ozu_tile = models.CharField(max_length=255, blank=True, verbose_name='Оперативная память Заголовок или др...')
    ozu = models.CharField(max_length=255, blank=True, verbose_name='Оперативная память')

    headset_tile = models.CharField(max_length=255, blank=True, verbose_name='Гарнитура Заголовок или др...')
    headset = models.CharField(max_length=255, blank=True, verbose_name='Гарнитура')

    keyboard_tile = models.CharField(max_length=255, blank=True, verbose_name='Клавиатура Заголовок или др...')
    keyboard = models.CharField(max_length=255, blank=True, verbose_name='Клавиатура')

    mouse_tile = models.CharField(max_length=255, blank=True, verbose_name='Мышь Заголовок или др...')
    mouse = models.CharField(max_length=255, blank=True, verbose_name='Мышь')


    sort = models.CharField(max_length=4, blank=True, verbose_name='Сортировка')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создание')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '7) Жуковский Зоны (Клуб)'
        verbose_name_plural = '7) Жуковский Игровые Зоны (Клуб)'
        ordering = ['time_create', 'title']











# Serpuhovskaya Part
###################################

class SerpuhovskayaNews(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='slug')
    photo = models.ImageField(upload_to='photos/promo/')
    photo_mobile = models.ImageField(upload_to='photos/promo/')
    short = models.TextField(blank=True, verbose_name='Короткое описание')
    descr = models.TextField(blank=True, verbose_name='Текст')
    sort = models.CharField(max_length=4, blank=True, verbose_name='Сортировка')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создание')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '8) Серпуховская Новость (Клуб)'
        verbose_name_plural = '8) Серпуховская Новости (Клуб)'
        ordering = ['time_create', 'title']



class SerpuhovskayaPromo(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='slug')
    photo = models.ImageField(upload_to='photos/promo/')
    photo_mobile = models.ImageField(upload_to='photos/promo/')
    short = models.TextField(blank=True, verbose_name='Короткое описание')
    descr = models.TextField(blank=True, verbose_name='Текст')
    sort = models.CharField(max_length=4,blank=True, verbose_name='Сортировка')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создание')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '8) Серпуховская Акция (Клуб)'
        verbose_name_plural = '8) Серпуховская Акции (Клуб)'
        ordering = ['time_create', 'title']





class SerpuhovskayaZones(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название игровой зоны')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='slug')
    photo = models.ImageField(upload_to='photos/zones/')
    photo_mobile = models.ImageField(upload_to='photos/zones/')


    timeone = models.CharField(max_length=255, blank=True, verbose_name='Время 1 (Понедельник-Четверг)')
    priceone = models.CharField(max_length=255, blank=True, verbose_name='Цена 1')

    timetwo = models.CharField(max_length=255, blank=True, verbose_name='Время 2 (Понедельник-Четверг)')
    prictwo = models.CharField(max_length=255, blank=True, verbose_name='Цена 2')

    timetri = models.CharField(max_length=255, blank=True, verbose_name='Время 3 (Понедельник-Четверг)')
    pricetri = models.CharField(max_length=255, blank=True, verbose_name='Цена 3')

    timefour = models.CharField(max_length=255, blank=True, verbose_name='Время 4 (Понедельник-Четверг)')
    pricefour = models.CharField(max_length=255, blank=True, verbose_name='Цена 4')

    timefive = models.CharField(max_length=255, blank=True, verbose_name='Время 5 (Понедельник-Четверг)')
    pricefive = models.CharField(max_length=255, blank=True, verbose_name='Цена 5')

    timesix = models.CharField(max_length=255, blank=True, verbose_name='Время 6 (Понедельник-Четверг)')
    pricesix = models.CharField(max_length=255, blank=True, verbose_name='Цена 6')




    weekend_timeone = models.CharField(max_length=255, blank=True, verbose_name='Время 1 (Пятница-Воскресенье)')
    weekend_priceone = models.CharField(max_length=255, blank=True, verbose_name='Цена 1')

    weekend_timetwo = models.CharField(max_length=255, blank=True, verbose_name='Время 2 (Пятница-Воскресенье)')
    weekend_prictwo = models.CharField(max_length=255, blank=True, verbose_name='Цена 2')

    weekend_timetri = models.CharField(max_length=255, blank=True, verbose_name='Время 3 (Пятница-Воскресенье)')
    weekend_pricetri = models.CharField(max_length=255, blank=True, verbose_name='Цена 3')

    weekend_timefour = models.CharField(max_length=255, blank=True, verbose_name='Время 4 (Пятница-Воскресенье)')
    weekend_pricefour = models.CharField(max_length=255, blank=True, verbose_name='Цена 4')

    weekend_timefive = models.CharField(max_length=255, blank=True, verbose_name='Время 5 (Пятница-Воскресенье)')
    weekend_pricefive = models.CharField(max_length=255, blank=True, verbose_name='Цена 5')

    weekend_timesix = models.CharField(max_length=255, blank=True, verbose_name='Время 6 (Пятница-Воскресенье)')
    weekend_pricesix = models.CharField(max_length=255, blank=True, verbose_name='Цена 6')



    monitor_tile = models.CharField(max_length=255, blank=True, verbose_name='Монитор Заголовок или др...')
    monitor = models.CharField(max_length=255, blank=True, verbose_name='Монитор(ы)')

    processor_tile = models.CharField(max_length=255, blank=True, verbose_name='Процессор Заголовок или др...')
    processor = models.CharField(max_length=255, blank=True, verbose_name='Процессор')

    videocard_tile = models.CharField(max_length=255, blank=True, verbose_name='Видеокарта Заголовок или др...')
    videocard = models.CharField(max_length=255, blank=True, verbose_name='Видеокарта')

    ozu_tile = models.CharField(max_length=255, blank=True, verbose_name='Оперативная память Заголовок или др...')
    ozu = models.CharField(max_length=255, blank=True, verbose_name='Оперативная память')

    headset_tile = models.CharField(max_length=255, blank=True, verbose_name='Гарнитура Заголовок или др...')
    headset = models.CharField(max_length=255, blank=True, verbose_name='Гарнитура')

    keyboard_tile = models.CharField(max_length=255, blank=True, verbose_name='Клавиатура Заголовок или др...')
    keyboard = models.CharField(max_length=255, blank=True, verbose_name='Клавиатура')

    mouse_tile = models.CharField(max_length=255, blank=True, verbose_name='Мышь Заголовок или др...')
    mouse = models.CharField(max_length=255, blank=True, verbose_name='Мышь')


    sort = models.CharField(max_length=4, blank=True, verbose_name='Сортировка')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создание')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '8) Серпуховская Зоны (Клуб)'
        verbose_name_plural = '8) Серпуховская Игровые Зоны (Клуб)'
        ordering = ['time_create', 'title']







# new version of zones


class SerpuhovskayaZonesNew(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название игровой зоны')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='slug')


    monitor_tile = models.CharField(max_length=255, blank=True, verbose_name='Монитор Заголовок или др...')
    monitor = models.CharField(max_length=255, blank=True, verbose_name='Монитор(ы)')

    processor_tile = models.CharField(max_length=255, blank=True, verbose_name='Процессор Заголовок или др...')
    processor = models.CharField(max_length=255, blank=True, verbose_name='Процессор')

    videocard_tile = models.CharField(max_length=255, blank=True, verbose_name='Видеокарта Заголовок или др...')
    videocard = models.CharField(max_length=255, blank=True, verbose_name='Видеокарта')

    ozu_tile = models.CharField(max_length=255, blank=True, verbose_name='Оперативная память Заголовок или др...')
    ozu = models.CharField(max_length=255, blank=True, verbose_name='Оперативная память')

    headset_tile = models.CharField(max_length=255, blank=True, verbose_name='Гарнитура Заголовок или др...')
    headset = models.CharField(max_length=255, blank=True, verbose_name='Гарнитура')

    keyboard_tile = models.CharField(max_length=255, blank=True, verbose_name='Клавиатура Заголовок или др...')
    keyboard = models.CharField(max_length=255, blank=True, verbose_name='Клавиатура')

    mouse_tile = models.CharField(max_length=255, blank=True, verbose_name='Мышь Заголовок или др...')
    mouse = models.CharField(max_length=255, blank=True, verbose_name='Мышь')


    timeone = models.CharField(max_length=255, blank=True, verbose_name='Время 1 (Понедельник-Четверг)')
    priceone = models.CharField(max_length=255, blank=True, verbose_name='Цена 1')

    timetwo = models.CharField(max_length=255, blank=True, verbose_name='Время 2 (Понедельник-Четверг)')
    prictwo = models.CharField(max_length=255, blank=True, verbose_name='Цена 2')

    timetri = models.CharField(max_length=255, blank=True, verbose_name='Время 3 (Понедельник-Четверг)')
    pricetri = models.CharField(max_length=255, blank=True, verbose_name='Цена 3')

    timefour = models.CharField(max_length=255, blank=True, verbose_name='Время 4 (Понедельник-Четверг)')
    pricefour = models.CharField(max_length=255, blank=True, verbose_name='Цена 4')

    timefive = models.CharField(max_length=255, blank=True, verbose_name='Время 5 (Понедельник-Четверг)')
    pricefive = models.CharField(max_length=255, blank=True, verbose_name='Цена 5')

    timesix = models.CharField(max_length=255, blank=True, verbose_name='Время 6 (Понедельник-Четверг)')
    pricesix = models.CharField(max_length=255, blank=True, verbose_name='Цена 6')



    weekend_timeone = models.CharField(max_length=255, blank=True, verbose_name='Время 1 (Пятница-Воскресенье)')
    weekend_priceone = models.CharField(max_length=255, blank=True, verbose_name='Цена 1')

    weekend_timetwo = models.CharField(max_length=255, blank=True, verbose_name='Время 2 (Пятница-Воскресенье)')
    weekend_prictwo = models.CharField(max_length=255, blank=True, verbose_name='Цена 2')

    weekend_timetri = models.CharField(max_length=255, blank=True, verbose_name='Время 3 (Пятница-Воскресенье)')
    weekend_pricetri = models.CharField(max_length=255, blank=True, verbose_name='Цена 3')

    weekend_timefour = models.CharField(max_length=255, blank=True, verbose_name='Время 4 (Пятница-Воскресенье)')
    weekend_pricefour = models.CharField(max_length=255, blank=True, verbose_name='Цена 4')

    weekend_timefive = models.CharField(max_length=255, blank=True, verbose_name='Время 5 (Пятница-Воскресенье)')
    weekend_pricefive = models.CharField(max_length=255, blank=True, verbose_name='Цена 5')

    weekend_timesix = models.CharField(max_length=255, blank=True, verbose_name='Время 6 (Пятница-Воскресенье)')
    weekend_pricesix = models.CharField(max_length=255, blank=True, verbose_name='Цена 6')


    sort = models.CharField(max_length=4, blank=True, verbose_name='Сортировка')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создание')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '8new) Серпуховская Зоны new (new)'
        verbose_name_plural = '8new) Серпуховская Игровые Зоны (new)'
        ordering = ['time_create', 'title']




class ZonesSerpuhovskayaPics(models.Model):
    zone = models.ForeignKey(SerpuhovskayaZonesNew, related_name='zone_pics', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/zonesserpuhovskayapics/')
    photo_mobile = models.ImageField(upload_to='photos/zonesserpuhovskayapics/')
    sort = models.CharField(max_length=4, blank=True, verbose_name='Сортировка')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')

    def __str__(self):
        return f"{self.zone.title} - {self.photo}"

    class Meta:
        verbose_name = '8_new) Картинки zones Серпуховская'
        verbose_name_plural = '8_new) Картинки zones Серпуховская'
        ordering = ['zone', 'id']












# Pushkino Part
###################################

class PushkinoNews(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='slug')
    photo = models.ImageField(upload_to='photos/promo/')
    photo_mobile = models.ImageField(upload_to='photos/promo/')
    short = models.TextField(blank=True, verbose_name='Короткое описание')
    descr = models.TextField(blank=True, verbose_name='Текст')
    sort = models.CharField(max_length=4, blank=True, verbose_name='Сортировка')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создание')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '9) Пушкино Новость (Клуб)'
        verbose_name_plural = '9) Пушкино Новости (Клуб)'
        ordering = ['time_create', 'title']



class PushkinoPromo(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='slug')
    photo = models.ImageField(upload_to='photos/promo/')
    photo_mobile = models.ImageField(upload_to='photos/promo/')
    short = models.TextField(blank=True, verbose_name='Короткое описание')
    descr = models.TextField(blank=True, verbose_name='Текст')
    sort = models.CharField(max_length=4,blank=True, verbose_name='Сортировка')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создание')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '9) Пушкино Акция (Клуб)'
        verbose_name_plural = '9) Пушкино Акции (Клуб)'
        ordering = ['time_create', 'title']





class PushkinoZones(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название игровой зоны')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='slug')
    photo = models.ImageField(upload_to='photos/zones/')
    photo_mobile = models.ImageField(upload_to='photos/zones/')


    timeone = models.CharField(max_length=255, blank=True, verbose_name='Время 1 (Понедельник-Четверг)')
    priceone = models.CharField(max_length=255, blank=True, verbose_name='Цена 1')

    timetwo = models.CharField(max_length=255, blank=True, verbose_name='Время 2 (Понедельник-Четверг)')
    prictwo = models.CharField(max_length=255, blank=True, verbose_name='Цена 2')

    timetri = models.CharField(max_length=255, blank=True, verbose_name='Время 3 (Понедельник-Четверг)')
    pricetri = models.CharField(max_length=255, blank=True, verbose_name='Цена 3')

    timefour = models.CharField(max_length=255, blank=True, verbose_name='Время 4 (Понедельник-Четверг)')
    pricefour = models.CharField(max_length=255, blank=True, verbose_name='Цена 4')

    timefive = models.CharField(max_length=255, blank=True, verbose_name='Время 5 (Понедельник-Четверг)')
    pricefive = models.CharField(max_length=255, blank=True, verbose_name='Цена 5')

    timesix = models.CharField(max_length=255, blank=True, verbose_name='Время 6 (Понедельник-Четверг)')
    pricesix = models.CharField(max_length=255, blank=True, verbose_name='Цена 6')




    weekend_timeone = models.CharField(max_length=255, blank=True, verbose_name='Время 1 (Пятница-Воскресенье)')
    weekend_priceone = models.CharField(max_length=255, blank=True, verbose_name='Цена 1')

    weekend_timetwo = models.CharField(max_length=255, blank=True, verbose_name='Время 2 (Пятница-Воскресенье)')
    weekend_prictwo = models.CharField(max_length=255, blank=True, verbose_name='Цена 2')

    weekend_timetri = models.CharField(max_length=255, blank=True, verbose_name='Время 3 (Пятница-Воскресенье)')
    weekend_pricetri = models.CharField(max_length=255, blank=True, verbose_name='Цена 3')

    weekend_timefour = models.CharField(max_length=255, blank=True, verbose_name='Время 4 (Пятница-Воскресенье)')
    weekend_pricefour = models.CharField(max_length=255, blank=True, verbose_name='Цена 4')

    weekend_timefive = models.CharField(max_length=255, blank=True, verbose_name='Время 5 (Пятница-Воскресенье)')
    weekend_pricefive = models.CharField(max_length=255, blank=True, verbose_name='Цена 5')

    weekend_timesix = models.CharField(max_length=255, blank=True, verbose_name='Время 6 (Пятница-Воскресенье)')
    weekend_pricesix = models.CharField(max_length=255, blank=True, verbose_name='Цена 6')



    monitor_tile = models.CharField(max_length=255, blank=True, verbose_name='Монитор Заголовок или др...')
    monitor = models.CharField(max_length=255, blank=True, verbose_name='Монитор(ы)')

    processor_tile = models.CharField(max_length=255, blank=True, verbose_name='Процессор Заголовок или др...')
    processor = models.CharField(max_length=255, blank=True, verbose_name='Процессор')

    videocard_tile = models.CharField(max_length=255, blank=True, verbose_name='Видеокарта Заголовок или др...')
    videocard = models.CharField(max_length=255, blank=True, verbose_name='Видеокарта')

    ozu_tile = models.CharField(max_length=255, blank=True, verbose_name='Оперативная память Заголовок или др...')
    ozu = models.CharField(max_length=255, blank=True, verbose_name='Оперативная память')

    headset_tile = models.CharField(max_length=255, blank=True, verbose_name='Гарнитура Заголовок или др...')
    headset = models.CharField(max_length=255, blank=True, verbose_name='Гарнитура')

    keyboard_tile = models.CharField(max_length=255, blank=True, verbose_name='Клавиатура Заголовок или др...')
    keyboard = models.CharField(max_length=255, blank=True, verbose_name='Клавиатура')

    mouse_tile = models.CharField(max_length=255, blank=True, verbose_name='Мышь Заголовок или др...')
    mouse = models.CharField(max_length=255, blank=True, verbose_name='Мышь')


    sort = models.CharField(max_length=4, blank=True, verbose_name='Сортировка')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создание')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '9) Пушкино Зоны (Клуб)'
        verbose_name_plural = '9) Пушкино Игровые Зоны (Клуб)'
        ordering = ['time_create', 'title']













# Mahachkala Part
###################################

class MahachkalaNews(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='slug')
    photo = models.ImageField(upload_to='photos/promo/')
    photo_mobile = models.ImageField(upload_to='photos/promo/')
    short = models.TextField(blank=True, verbose_name='Короткое описание')
    descr = models.TextField(blank=True, verbose_name='Текст')
    sort = models.CharField(max_length=4, blank=True, verbose_name='Сортировка')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создание')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '10) Махачкала Новость (Клуб)'
        verbose_name_plural = '10) Махачкала Новости (Клуб)'
        ordering = ['time_create', 'title']


class MahachkalaPromo(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='slug')
    photo = models.ImageField(upload_to='photos/promo/')
    photo_mobile = models.ImageField(upload_to='photos/promo/')
    short = models.TextField(blank=True, verbose_name='Короткое описание')
    descr = models.TextField(blank=True, verbose_name='Текст')
    sort = models.CharField(max_length=4,blank=True, verbose_name='Сортировка')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создание')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '10) Махачкала Акция (Клуб)'
        verbose_name_plural = '10) Махачкала Акции (Клуб)'
        ordering = ['time_create', 'title']




class MahachkalaZones(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название игровой зоны')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='slug')
    timeone = models.CharField(max_length=255, blank=True, verbose_name='Время 1 (Понедельник-Четверг)')
    priceone = models.CharField(max_length=255, blank=True, verbose_name='Цена 1')

    timetwo = models.CharField(max_length=255, blank=True, verbose_name='Время 2 (Понедельник-Четверг)')
    prictwo = models.CharField(max_length=255, blank=True, verbose_name='Цена 2')

    timetri = models.CharField(max_length=255, blank=True, verbose_name='Время 3 (Понедельник-Четверг)')
    pricetri = models.CharField(max_length=255, blank=True, verbose_name='Цена 3')

    timefour = models.CharField(max_length=255, blank=True, verbose_name='Время 4 (Понедельник-Четверг)')
    pricefour = models.CharField(max_length=255, blank=True, verbose_name='Цена 4')

    timefive = models.CharField(max_length=255, blank=True, verbose_name='Время 5 (Понедельник-Четверг)')
    pricefive = models.CharField(max_length=255, blank=True, verbose_name='Цена 5')

    timesix = models.CharField(max_length=255, blank=True, verbose_name='Время 6 (Понедельник-Четверг)')
    pricesix = models.CharField(max_length=255, blank=True, verbose_name='Цена 6')




    weekend_timeone = models.CharField(max_length=255, blank=True, verbose_name='Время 1 (Пятница-Воскресенье)')
    weekend_priceone = models.CharField(max_length=255, blank=True, verbose_name='Цена 1')

    weekend_timetwo = models.CharField(max_length=255, blank=True, verbose_name='Время 2 (Пятница-Воскресенье)')
    weekend_prictwo = models.CharField(max_length=255, blank=True, verbose_name='Цена 2')

    weekend_timetri = models.CharField(max_length=255, blank=True, verbose_name='Время 3 (Пятница-Воскресенье)')
    weekend_pricetri = models.CharField(max_length=255, blank=True, verbose_name='Цена 3')

    weekend_timefour = models.CharField(max_length=255, blank=True, verbose_name='Время 4 (Пятница-Воскресенье)')
    weekend_pricefour = models.CharField(max_length=255, blank=True, verbose_name='Цена 4')

    weekend_timefive = models.CharField(max_length=255, blank=True, verbose_name='Время 5 (Пятница-Воскресенье)')
    weekend_pricefive = models.CharField(max_length=255, blank=True, verbose_name='Цена 5')

    weekend_timesix = models.CharField(max_length=255, blank=True, verbose_name='Время 6 (Пятница-Воскресенье)')
    weekend_pricesix = models.CharField(max_length=255, blank=True, verbose_name='Цена 6')



    monitor_tile = models.CharField(max_length=255, blank=True, verbose_name='Монитор Заголовок или др...')
    monitor = models.CharField(max_length=255, blank=True, verbose_name='Монитор(ы)')

    processor_tile = models.CharField(max_length=255, blank=True, verbose_name='Процессор Заголовок или др...')
    processor = models.CharField(max_length=255, blank=True, verbose_name='Процессор')

    videocard_tile = models.CharField(max_length=255, blank=True, verbose_name='Видеокарта Заголовок или др...')
    videocard = models.CharField(max_length=255, blank=True, verbose_name='Видеокарта')

    ozu_tile = models.CharField(max_length=255, blank=True, verbose_name='Оперативная память Заголовок или др...')
    ozu = models.CharField(max_length=255, blank=True, verbose_name='Оперативная память')

    headset_tile = models.CharField(max_length=255, blank=True, verbose_name='Гарнитура Заголовок или др...')
    headset = models.CharField(max_length=255, blank=True, verbose_name='Гарнитура')

    keyboard_tile = models.CharField(max_length=255, blank=True, verbose_name='Клавиатура Заголовок или др...')
    keyboard = models.CharField(max_length=255, blank=True, verbose_name='Клавиатура')

    mouse_tile = models.CharField(max_length=255, blank=True, verbose_name='Мышь Заголовок или др...')
    mouse = models.CharField(max_length=255, blank=True, verbose_name='Мышь')


    sort = models.CharField(max_length=4, blank=True, verbose_name='Сортировка')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создание')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '10) Махачкала Зоны (Клуб)'
        verbose_name_plural = '10) Махачкала Игровые Зоны (Клуб)'
        ordering = ['time_create', 'title']



class MahachkalaZoness(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название игровой зоны')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='slug')
    timeone = models.CharField(max_length=255, blank=True, verbose_name='Время 1 (Понедельник-Четверг)')
    priceone = models.CharField(max_length=255, blank=True, verbose_name='Цена 1')

    timetwo = models.CharField(max_length=255, blank=True, verbose_name='Время 2 (Понедельник-Четверг)')
    prictwo = models.CharField(max_length=255, blank=True, verbose_name='Цена 2')

    timetri = models.CharField(max_length=255, blank=True, verbose_name='Время 3 (Понедельник-Четверг)')
    pricetri = models.CharField(max_length=255, blank=True, verbose_name='Цена 3')

    timefour = models.CharField(max_length=255, blank=True, verbose_name='Время 4 (Понедельник-Четверг)')
    pricefour = models.CharField(max_length=255, blank=True, verbose_name='Цена 4')

    timefive = models.CharField(max_length=255, blank=True, verbose_name='Время 5 (Понедельник-Четверг)')
    pricefive = models.CharField(max_length=255, blank=True, verbose_name='Цена 5')

    timesix = models.CharField(max_length=255, blank=True, verbose_name='Время 6 (Понедельник-Четверг)')
    pricesix = models.CharField(max_length=255, blank=True, verbose_name='Цена 6')




    weekend_timeone = models.CharField(max_length=255, blank=True, verbose_name='Время 1 (Пятница-Воскресенье)')
    weekend_priceone = models.CharField(max_length=255, blank=True, verbose_name='Цена 1')

    weekend_timetwo = models.CharField(max_length=255, blank=True, verbose_name='Время 2 (Пятница-Воскресенье)')
    weekend_prictwo = models.CharField(max_length=255, blank=True, verbose_name='Цена 2')

    weekend_timetri = models.CharField(max_length=255, blank=True, verbose_name='Время 3 (Пятница-Воскресенье)')
    weekend_pricetri = models.CharField(max_length=255, blank=True, verbose_name='Цена 3')

    weekend_timefour = models.CharField(max_length=255, blank=True, verbose_name='Время 4 (Пятница-Воскресенье)')
    weekend_pricefour = models.CharField(max_length=255, blank=True, verbose_name='Цена 4')

    weekend_timefive = models.CharField(max_length=255, blank=True, verbose_name='Время 5 (Пятница-Воскресенье)')
    weekend_pricefive = models.CharField(max_length=255, blank=True, verbose_name='Цена 5')

    weekend_timesix = models.CharField(max_length=255, blank=True, verbose_name='Время 6 (Пятница-Воскресенье)')
    weekend_pricesix = models.CharField(max_length=255, blank=True, verbose_name='Цена 6')



    monitor_tile = models.CharField(max_length=255, blank=True, verbose_name='Монитор Заголовок или др...')
    monitor = models.CharField(max_length=255, blank=True, verbose_name='Монитор(ы)')

    processor_tile = models.CharField(max_length=255, blank=True, verbose_name='Процессор Заголовок или др...')
    processor = models.CharField(max_length=255, blank=True, verbose_name='Процессор')

    videocard_tile = models.CharField(max_length=255, blank=True, verbose_name='Видеокарта Заголовок или др...')
    videocard = models.CharField(max_length=255, blank=True, verbose_name='Видеокарта')

    ozu_tile = models.CharField(max_length=255, blank=True, verbose_name='Оперативная память Заголовок или др...')
    ozu = models.CharField(max_length=255, blank=True, verbose_name='Оперативная память')

    headset_tile = models.CharField(max_length=255, blank=True, verbose_name='Гарнитура Заголовок или др...')
    headset = models.CharField(max_length=255, blank=True, verbose_name='Гарнитура')

    keyboard_tile = models.CharField(max_length=255, blank=True, verbose_name='Клавиатура Заголовок или др...')
    keyboard = models.CharField(max_length=255, blank=True, verbose_name='Клавиатура')

    mouse_tile = models.CharField(max_length=255, blank=True, verbose_name='Мышь Заголовок или др...')
    mouse = models.CharField(max_length=255, blank=True, verbose_name='Мышь')


    sort = models.IntegerField(blank=True, null=True, verbose_name='Сортировка')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создание')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '10) Махачкала Зоны (Клуб)'
        verbose_name_plural = '10) Махачкала Игровые Зоны (Клуб)'
        # ordering = ['time_create', 'title']




class MahachkalaPicssMahachkalaPicss(models.Model):
    zone = models.ForeignKey(MahachkalaZoness, related_name='eewewe', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/mahachkalahpicwes/')
    photo_mobile = models.ImageField(upload_to='photos/mahachkalahpics/')
    sort = models.CharField(max_length=4, blank=True, verbose_name='Сортировка')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')

    def __str__(self):
        return f"{self.zone.title} - {self.photo}"

    class Meta:
        verbose_name = '10) Картинки zones Махачкала'
        verbose_name_plural = '10) Картинки zones Махачкала'
        ordering = ['zone', 'id']





class ContactPageZonesImages(models.Model):
    TYPE_CLUBS = (
        ('Серпуховская', 'Серпуховская'),
        ('ВДНХ', 'ВДНХ'),
        ('Вернадского', 'Вернадского'),
        ('Митино', 'Митино'),
        ('Коптево', 'Коптево'),
        ('Жулебино', 'Жулебино'),
        ('Жуковский', 'Жуковский'),
        ('Махачкала', 'Махачкала')
        
    )
    type = models.CharField(max_length=211, choices=TYPE_CLUBS, verbose_name='Тип клуба')
    image = models.ImageField(upload_to='contact_page_zones/', verbose_name='Изображение для Комп')
    image_mobile = models.ImageField(upload_to='contact_page_zones/', verbose_name='Изображение для Телефон')

    def __str__(self):
        return f"{self.type}"

    class Meta:
        verbose_name = 'Изображение зоны контактов'
        verbose_name_plural = 'Изображения зон контактов'
        
    def clean(self):
        # Проверка, существует ли уже запись с таким типом
        if ContactPageZonesImages.objects.filter(type=self.type).exists() and not self.pk:
            raise ValidationError(f"Запись с типом '{self.type}' уже существует.")
    
    def save(self, *args, **kwargs):
        self.clean()  # вызываем метод clean для валидации
        super().save(*args, **kwargs)



class ClubPageZonesImages(models.Model):
    TYPE_CLUBS = (
        ('Серпуховская', 'Серпуховская'),
        ('ВДНХ', 'ВДНХ'),
        ('Вернадского', 'Вернадского'),
        ('Митино', 'Митино'),
        ('Коптево', 'Коптево'),
        ('Жулебино', 'Жулебино'),
        ('Жуковский', 'Жуковский'),
        ('Махачкала', 'Махачкала')
        
    )
    type = models.CharField(max_length=211, choices=TYPE_CLUBS, verbose_name='Тип клуба')
    image = models.ImageField(upload_to='club_page_zones/', verbose_name='Изображение для Комп')
    image_mobile = models.ImageField(upload_to='club_page_zones/', verbose_name='Изображение для Телефон')

    def __str__(self):
        return f"{self.type}"

    class Meta:
        verbose_name = 'Изображение Клубы'
        verbose_name_plural = 'Изображения Клубы'
        
    def clean(self):
        # Проверка, существует ли уже запись с таким типом
        if ClubPageZonesImages.objects.filter(type=self.type).exists() and not self.pk:
            raise ValidationError(f"Запись с типом '{self.type}' уже существует.")
    
    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)
            img = img.convert("RGB")
            img_io = BytesIO()
            img.save(img_io, format='WEBP', quality=85)
            img_name, _ = os.path.splitext(self.image.name)
            self.image.save(f"{img_name}.webp", ContentFile(img_io.getvalue()), save=False)
        if self.image_mobile:
            img = Image.open(self.image_mobile)
            img = img.convert("RGB")
            img_io = BytesIO()
            img.save(img_io, format='WEBP', quality=85)
            img_name, _ = os.path.splitext(self.image_mobile.name)
            self.image_mobile.save(f"{img_name}.webp", ContentFile(img_io.getvalue()), save=False)
        super().save(*args, **kwargs)


def club_photo_upload_path(instance, filename):
    """Кладём фото в отдельную папку клуба по его slug."""
    return f"photos/{instance.club.slug}/{filename}"

def club_gallery_upload_path(instance, filename):
    """Кладём фото в отдельную папку клуба по его slug."""
    return f"photos/{instance.club.slug}/gallery/{filename}"

def club_news_upload_path(instance, filename):
    """Кладём фото в отдельную папку клуба по его slug."""
    return f"photos/{instance.club.slug}/news/{filename}"

# READY
class Club(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="Название клуба полное", blank=True, null=True)
    name = models.CharField(max_length=255, unique=True, verbose_name="Название клуба")
    slug = models.CharField(max_length=255, verbose_name="slug")
    video = models.FileField(
        upload_to="videos/clubs/",
        blank=True,
        null=True,
        verbose_name="Видео промо клуба (mp4)"
    )
    image_of_zones = models.ImageField(upload_to="club_zones/", verbose_name="Картинка зон клуба", blank=True, null=True)
    
    pc_games = models.TextField(
        blank=True,
        verbose_name="Игры для ПК (через запятую, без пробелов)"
    )
    tv_games = models.TextField(
        blank=True,
        verbose_name="Игры для ТВ (через запятую, без пробелов)"
    )

    phone = models.CharField(verbose_name="Номер телефона", max_length=64, blank=True, null=True)
    map_link = models.CharField(verbose_name="Ссылка на карты", max_length=255, blank=True, null=True)

    is_open_24 = models.BooleanField(verbose_name="Круглосуточный", blank=True, null=True)

    is_open = models.BooleanField(verbose_name="Открыт ли клуб", blank=True, null=True, default=True)

    def get_pc_games(self):
        return [g.strip() for g in self.pc_games.split(",") if g.strip()]

    def get_tv_games(self):
        return [g.strip() for g in self.tv_games.split(",") if g.strip()]

    def __str__(self):
        return f"{self.name} - {self.slug}"
    
    @property
    def total_pcs(self):
        """Считает общее количество ПК по всем зонам клуба."""
        return sum(zone.count for zone in self.zones.all() if zone.count)
    
    class Meta:
        verbose_name = "Клуб"
        verbose_name_plural = "Клубы"

class ClubPageImages(models.Model):
    club = models.OneToOneField(
        Club,
        on_delete=models.CASCADE,
        related_name="zones_image",
        verbose_name="Клуб"
    )

    image = models.ImageField(
        upload_to="club_page_zones/",
        verbose_name="Изображение для компьютеров"
    )

    image_mobile = models.ImageField(
        upload_to="club_page_zones/",
        verbose_name="Изображение для телефонов"
    )

    def __str__(self):
        return f"Изображение зон — {self.club.name}"

    class Meta:
        verbose_name = "Изображение зон клуба"
        verbose_name_plural = "Изображения зон клубов"

    def clean(self):
        # Проверяем, чтобы не было дубликатов для одного клуба
        if ClubPageImages.objects.filter(club=self.club).exists() and not self.pk:
            raise ValidationError(f"Для клуба '{self.club.name}' изображение зон уже существует.")

    def save(self, *args, **kwargs):
        """
        При сохранении — конвертируем изображения в WEBP (если загружены).
        """
        for field_name in ["image", "image_mobile"]:
            img_field = getattr(self, field_name)
            if img_field:
                img = Image.open(img_field)
                img = img.convert("RGB")
                img_io = BytesIO()
                img.save(img_io, format="WEBP", quality=85)
                img_name, _ = os.path.splitext(img_field.name)
                img_field.save(f"{img_name}.webp", ContentFile(img_io.getvalue()), save=False)

        super().save(*args, **kwargs)


class ClubRoute(models.Model):
    club = models.OneToOneField(
        "Club",
        on_delete=models.CASCADE,
        related_name="route",
        verbose_name="Клуб"
    )

    title = models.CharField(
        max_length=255,
        default="Как найти клуб",
        verbose_name="Заголовок блока",
        blank=True,
    )

    address = models.CharField(
        max_length=255,
        verbose_name="Адрес клуба",
        blank=True,
    )

    landmark = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Ориентир"
    )

    metro_info = models.TextField(
        blank=True,
        verbose_name="Информация о метро (можно с переносами строк)"
    )

    phone = models.CharField(
        max_length=50,
        verbose_name="Телефон для связи",
        blank=True,
    )

    lottie_file = models.FileField(
        upload_to="lottie/clubs/",
        blank=True,
        null=True,
        verbose_name="Lottie JSON-анимация"
    )

    is_published = models.BooleanField(
        default=True,
        verbose_name="Показывать блок на сайте"
    )

    def __str__(self):
        return f"Как найти клуб {self.club.name}"

    class Meta:
        verbose_name = "Как найти клуб"
        verbose_name_plural = "Как найти клуб (блоки)"


class ClubBottomAbout(models.Model):
    club = models.OneToOneField(
        Club,
        on_delete=models.CASCADE,
        related_name="bottom_about",
        verbose_name="Клуб"
    )
    title = models.CharField(max_length=127, verbose_name="Заголовок")
    txt = models.TextField(
        verbose_name="Текст",
        help_text="Можно использовать HTML-теги для форматирования"
    )
    is_published = models.BooleanField(default=True, verbose_name="Показывать на сайте")


    def __str__(self):
        return f"{self.club.name} - {self.title}"
    
    class Meta:
        verbose_name = "Нижние описание"
        verbose_name_plural = "Нижние описания"



# READY
class PhotoClub(models.Model):
    club = models.ForeignKey("Club", related_name="photos", on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=club_photo_upload_path, verbose_name='Фото')
    photo_mobile = models.ImageField(upload_to=club_photo_upload_path, verbose_name='Фото мобильное')
    order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name='Порядок')
    
    def __str__(self):
        return f"{self.club.name} — {os.path.basename(self.photo.name)}"
    

    class Meta:
        verbose_name = 'Фотогаллерея'
        verbose_name_plural = 'Фотогаллереи'
        ordering = ['order', ]
        
    
    def save(self, *args, **kwargs):
        for field in ['photo', 'photo_mobile']:
            file = getattr(self, field)
            if file and not file.name.lower().endswith(".webp"):
                img = Image.open(file).convert("RGB")
                buf = BytesIO()
                img.save(buf, format='WEBP', quality=85)
                name, _ = os.path.splitext(file.name)
                getattr(self, field).save(f"{name}.webp", ContentFile(buf.getvalue()), save=False)
        super().save(*args, **kwargs)

# READY
class ClubSeo(models.Model):
    club = models.OneToOneField("Club", related_name="seo", on_delete=models.CASCADE)
    title = models.CharField(max_length=400, blank=True, verbose_name='title seo')
    description = models.TextField(blank=True, verbose_name='description seo')
    keywords = models.TextField(blank=True, verbose_name='keywords seo')

    def __str__(self):
        return f"SEO — {self.club.name}"
    
    class Meta:
        ordering = ['club__name']
        verbose_name = 'SEO'
        verbose_name_plural = "SEO's"

#READY
class ClubGallery(models.Model):
    club = models.ForeignKey("Club", related_name="gallery", on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=club_gallery_upload_path)
    photo_mobile = models.ImageField(upload_to=club_gallery_upload_path)
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')

    def __str__(self):
        return f"{self.club.name} — {os.path.basename(self.photo.name)}"

    class Meta:
        ordering = ['id']
        verbose_name = "Фото галереи (низ)"
        verbose_name_plural = "Фото галереи (низ)"

#READY
class ClubNews(models.Model):
    club = models.ForeignKey("Club", related_name="news", on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, db_index=True, verbose_name='slug')
    photo = models.ImageField(upload_to='photos/promo/')
    photo_mobile = models.ImageField(upload_to='photos/promo/')
    short = models.TextField(blank=True, verbose_name='Короткое описание')
    descr = models.TextField(blank=True, verbose_name='Текст')
    sort = models.CharField(max_length=4, blank=True, verbose_name='Сортировка')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создание')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость Клуба'
        verbose_name_plural = 'Новости Клуба'
        ordering = ['-time_create']
        constraints = [
            models.UniqueConstraint(fields=["club", "slug"], name="unique_club_news_slug")
        ]

#READY
def club_promo_upload_path(instance, filename):
    """Путь для акций: photos/<club_slug>/promo/<filename>"""
    return f"photos/{instance.club.slug}/promo/{filename}"


class ClubPromo(models.Model):
    """
    Акция, которая может относиться к нескольким клубам.
    """
    clubs = models.ManyToManyField(
        "Club",
        through="ClubPromoRelation",
        related_name="promos",
        verbose_name="Клубы, участвующие в акции",
        blank=True,
    )

    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, db_index=True, verbose_name="Slug")

    photo = models.ImageField(upload_to="photos/clubs/promos/")
    photo_mobile = models.ImageField(upload_to="photos/clubs/promos/", blank=True, null=True)

    short = models.TextField(blank=True, verbose_name="Короткое описание")
    descr = models.TextField(blank=True, verbose_name="Текст")

    sort = models.PositiveIntegerField(default=0, verbose_name="Порядок")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Обновлено")
    is_published = models.BooleanField(default=True, verbose_name="Опубликована")
    show_tags = models.BooleanField(default=True, verbose_name="Показывать теги")
    is_main_page = models.BooleanField(default=False, verbose_name="Показывать на главной")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Акция клуба"
        verbose_name_plural = "Акции клубов"
        ordering = ["-time_create"]


class ClubPromoRelation(models.Model):
    """
    Промежуточная таблица для связи акции и клуба.
    Обеспечивает уникальность slug в пределах клуба.
    """
    club = models.ForeignKey("Club", on_delete=models.CASCADE)
    promo = models.ForeignKey(ClubPromo, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Связь клуба и акции"
        verbose_name_plural = "Связи клубов и акций"
        constraints = [
            models.UniqueConstraint(fields=["club", "promo"], name="unique_club_promo_relation")
        ]

    def __str__(self):
        return f"{self.club.name} — {self.promo.title}"
    

class ClubZonesNew(models.Model):
    club = models.ForeignKey("Club", related_name="zones", on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name="Название игровой зоны")
    slug = models.SlugField(max_length=255, db_index=True, verbose_name="slug")
    count = models.PositiveIntegerField(verbose_name="Количество", blank=True, null=True)

    # характеристики оборудования
    monitor = models.CharField(max_length=255, blank=True, verbose_name="Монитор")
    processor = models.CharField(max_length=255, blank=True, verbose_name="Процессор/Телевизор")
    videocard = models.CharField(max_length=255, blank=True, verbose_name="Видеокарта/Размер и характеристики")
    ozu = models.CharField(max_length=255, blank=True, verbose_name="Оперативная память/Звук")
    headset = models.CharField(max_length=255, blank=True, verbose_name="Гарнитура/Комфорт")
    keyboard = models.CharField(max_length=255, blank=True, verbose_name="Клавиатура/Преимущества")
    mouse = models.CharField(max_length=255, blank=True, verbose_name="Мышь/Расположение")

    # доп параметры
    sort = models.CharField(max_length=4, blank=True, verbose_name="Сортировка")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создание')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, verbose_name="Опубликован")

    is_tv = models.BooleanField(default=False, null=True, verbose_name='TV ZONE')

    class Meta:
        verbose_name = "Игровая зона"
        verbose_name_plural = "Игровые зоны"
        constraints = [
            models.UniqueConstraint(fields=["club", "slug"], name="unique_zone_slug_per_club")
        ]
        ordering = ["-count",]

    def __str__(self):
        return f"{self.club.name} — {self.title}"


class ZonePriceBlock(models.Model):
    """
    Один блок прайса, например:
    'ПН–ЧТ', 'ПТ–ВС', 'Общий прайс', 'VIP тариф' и т.п.
    """
    zone = models.ForeignKey(
        ClubZonesNew, related_name="price_blocks", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255, verbose_name="Название блока (заголовок)")
    is_visible = models.BooleanField(default=True, verbose_name="Отображать блок")

    class Meta:
        verbose_name = "Блок прайса"
        verbose_name_plural = "Блоки прайса"
        ordering = ["id"]

    def __str__(self):
        return f"{self.zone.title} — {self.title}"


class ZonePriceItem(models.Model):
    """
    Отдельная строка прайса внутри блока.
    Например: "10:00–18:00" | "200 ₽"
    """
    block = models.ForeignKey(
        ZonePriceBlock, related_name="prices", on_delete=models.CASCADE
    )
    time = models.CharField(max_length=255, verbose_name="Время")
    price = models.CharField(max_length=255, verbose_name="Цена")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок сортировки")

    class Meta:
        verbose_name = "Элемент прайса"
        verbose_name_plural = "Элементы прайса"
        ordering = ["order"]

    def __str__(self):
        return f"{self.time} — {self.price}"



def club_zone_pics_upload_path(instance, filename):
    """Путь для фото зоны: photos/<club_slug>/zones/<zone_slug>/<filename>"""
    return f"photos/{instance.club.slug}/zones/{instance.zone.slug}/{filename}"


class ZonesClubPics(models.Model):
    club = models.ForeignKey("Club", related_name="zone_photos", on_delete=models.CASCADE, null=True)
    zone = models.ForeignKey("ClubZonesNew", related_name="zone_pics", on_delete=models.CASCADE)

    photo = models.ImageField(upload_to=club_zone_pics_upload_path)
    photo_mobile = models.ImageField(upload_to=club_zone_pics_upload_path, blank=True, null=True)

    sort = models.PositiveIntegerField(default=0, verbose_name="Порядок")
    is_published = models.BooleanField(default=True, verbose_name="Опубликован")

    def __str__(self):
        return f"{self.zone.title} — {os.path.basename(self.photo.name)}"
        # return f"{self.club.name} — {self.zone.title} — {os.path.basename(self.photo.name)}"

    class Meta:
        verbose_name = "Фото игровой зоны"
        verbose_name_plural = "Фото игровых зон"
        ordering = ["zone", "sort", "id"]


class NewsNew(models.Model):
    clubs = models.ManyToManyField(
        "Club",
        blank=True,
        related_name="global_news",
        verbose_name="Клубы (если новость клубная)"
    )

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug')

    photo = models.ImageField(upload_to='photos/newsnew/')
    photo_mobile = models.ImageField(upload_to='photos/newsnew/')

    short = models.TextField(blank=True, verbose_name='Короткое описание')
    descr = models.TextField(blank=True, verbose_name='Текст')
    sort = models.CharField(max_length=4, blank=True, verbose_name='Сортировка')

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    show_tags = models.BooleanField(default=True, verbose_name="Показывать теги")

    is_main_page = models.BooleanField(default=False, verbose_name="Показывать на главной")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'
        ordering = ['-time_create']


class MainPage(models.Model):
    phone = models.CharField(verbose_name="Номер телефона", max_length=64)
    video = models.FileField(upload_to="videos/mainpage/", verbose_name="Видео")
    background_video = models.FileField(upload_to="videos/mainpage/", verbose_name="Видео заднего фона", null=True)

    class Meta:
        verbose_name = "Главная странца"
        verbose_name_plural = "Главная странца"

    def __str__(self):
        return "Главная"

    @classmethod
    def get_solo(cls):
        """Возвращает единственный экземпляр модели (создает при необходимости)."""
        obj, created = cls.objects.get_or_create(pk=1)
        return obj
    

class FranchisePage(models.Model):
    phone = models.CharField(verbose_name="Номер телефона", max_length=64)

    class Meta:
        verbose_name = "Страница Франшизы"
        verbose_name_plural = "Страница Франшизы"

    def __str__(self):
        return "Франшиза"

    @classmethod
    def get_solo(cls):
        """Возвращает единственный экземпляр модели (создает при необходимости)."""
        obj, created = cls.objects.get_or_create(pk=1)
        return obj
    

class Logo(models.Model):
    page_logo = models.ImageField(verbose_name="Картинка на вкладке", upload_to="page_logo/")
    site_logo = models.ImageField(verbose_name="Картинка на странцие", upload_to="logo/")
    
    class Meta:
        verbose_name = "Лого"
        verbose_name_plural = "Лого"



    def __str__(self):
        return "Лого"

    @classmethod
    def get_solo(cls):
        """Возвращает единственный экземпляр модели (создает при необходимости)."""
        obj, created = cls.objects.get_or_create(pk=1)
        return obj