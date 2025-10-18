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


