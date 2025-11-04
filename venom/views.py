from itertools import chain
from django.db.models import Q, Prefetch
from django.shortcuts import redirect

from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django_user_agents.utils import get_user_agent
from django.views.generic import TemplateView, ListView, DetailView

from .models import *


# Create your views here.


class HomePageView(ListView):
    template_name = 'venom/index.html'
    context_object_name = 'all_content'

    def get_queryset(self):
        seo = HomePage.objects.all()
        homegallery = HomeGallery.objects.filter(is_published=True)
        news = News.objects.filter(is_published=True).order_by('-sort', '-time_create')[:4]
        news_new_variant = NewsNewVariant.objects.filter(is_published=True).exclude(catnews=1).order_by('-time_create', '-id')[:7]
        photovenum = PhotoVenum.objects.all().order_by('-order')[:8]
        zoneplay = ZonePlay.objects.all()
        characteristics = Characteristics.objects.all()
        all_content = list(chain(seo, homegallery, news, news_new_variant, photovenum, zoneplay, characteristics))
        return all_content

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['seo'] = [content for content in context['all_content'] if isinstance(content, HomePage)]
        context['homegallery'] = [content for content in context['all_content'] if isinstance(content, HomeGallery)]
        context['news'] = [content for content in context['all_content'] if isinstance(content, News)]
        context['news_new_variant'] = [content for content in context['all_content'] if
                                       isinstance(content, NewsNewVariant)]

        latest_news = NewsNew.objects.filter(is_published=True).filter(is_main_page=True).order_by( '-time_create', '-id')[:7]

        context['latest_news'] = latest_news
        context['photovenum'] = [content for content in context['all_content'] if isinstance(content, PhotoVenum)]
        context['zoneplay'] = [content for content in context['all_content'] if isinstance(content, ZonePlay)]
        context['characteristics'] = [content for content in context['all_content'] if isinstance(content, Characteristics)]
        context["mainpage"] = MainPage.get_solo
        # context["clubs"] = Club.objects.all()
        zones_queryset = ClubZonesNew.objects.all().order_by('sort')
        context["clubs"] = Club.objects.all().select_related('zones_image').prefetch_related(
            Prefetch("zones", queryset=zones_queryset)
        ).order_by("name")
        return context

    def get(self, request, *args, **kwargs):
        user_agent = get_user_agent(request)

        if user_agent.is_mobile:
            # Если это мобильное устройство, используйте другой шаблон
            self.template_name = 'venom/mobile/index.html'

        return super().get(request, *args, **kwargs)







class ClubsPage(ListView):
    template_name = 'venom/clubs.html'
    context_object_name = 'all_content'

    def get_queryset(self):
        seo = ClubPageSeo.objects.last()
        return seo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        seo = self.get_queryset()  # Получаем объект ClubPageSeo
        context['clubs_images'] = ClubPageZonesImages.objects.all() 
        context['seo'] = seo  # Добавляем объект ClubPageSeo в контекст
        zones_queryset = ClubZonesNew.objects.all().order_by('sort')
        context["clubs"] = Club.objects.all().select_related('zones_image').prefetch_related(
            Prefetch("zones", queryset=zones_queryset)
        ).order_by("name")
        context["mainpage"] = MainPage.get_solo
        return context


    def get(self, request, *args, **kwargs):
        user_agent = get_user_agent(request)

        if user_agent.is_mobile:
            # Если это мобильное устройство, используйте другой шаблон
            self.template_name = 'venom/mobile/clubs.html'

        return super().get(request, *args, **kwargs)






class PromoPageView(ListView):
    template_name = 'venom/promo.html'
    context_object_name = 'all_content'

    def get_queryset(self):
        promo_pages = PromoPage.objects.filter(is_published=True).order_by('-time_create')
        news = News.objects.filter(is_published=True).order_by('-time_create')
        news_new_variant = NewsNewVariant.objects.filter(is_published=True).order_by('-sort', '-time_create', '-id')
        photovenum = Tournament.objects.all().order_by('-order')[:8]
        all_content = list(chain(promo_pages, news, news_new_variant, photovenum))
        return all_content

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['promos'] = ClubPromo.objects.filter(is_published=True)
        context['news'] = [content for content in context['all_content'] if isinstance(content, News)]
        context['seo'] = PromoPageSeo.objects.last()
        context['news_new_variant'] = [content for content in context['all_content'] if
                                       isinstance(content, NewsNewVariant)]

        latest_news = NewsNew.objects.filter(is_published=True).order_by('-sort', '-time_create', '-id')
        context['photovenum'] = [content for content in context['all_content'] if isinstance(content, Tournament)]
        context['latest_news'] = latest_news
        context["mainpage"] = MainPage.get_solo
        

        return context

    def get(self, request, *args, **kwargs):
        user_agent = get_user_agent(request)

        if user_agent.is_mobile:
            # Если это мобильное устройство, используйте другой шаблон
            self.template_name = 'venom/mobile/promo.html'

        return super().get(request, *args, **kwargs)



class PromoDetail(DetailView):
    model = ClubPromo
    template_name = 'venom/promodetail.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'promo'



class NewsDetail(DetailView):
    model = News
    template_name = 'venom/newsDetail.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'news'


class NewsDetailNew(DetailView):
    model = NewsNew
    template_name = 'venom/newsDetailNew.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Получаем текущую новость
        news = self.get_object()
        # Добавляем рубрики новости в контекст
        context['categories'] = news.clubs.all()
        return context



class NewsDetailMobileNew(DetailView):
    model = ClubNews
    template_name = 'venom/news_detail_mobile_new.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'newsdetailmobile'

    def get_queryset(self):
        slug = self.kwargs.get("slug")

        # if club_slug:
        #     return (
        #         NewsNew.objects
        #         .filter(
        #             Q(clubs__slug=club_slug) |
        #             Q(is_main_page=False),  # можно включить и общие, если нужно
        #             is_published=True
        #         )
        #         .distinct()
        #     )
        # else:
        #     # Главные или общие новости
        #     return NewsNew.objects.filter(
        #         Q(is_main_page=True) | Q(clubs__isnull=True),
        #         is_published=True
        #     ).distinct()
        return NewsNew.objects.filter(slug=slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Получаем текущую новость
        news = self.get_object()
        # Добавляем рубрики новости в контекст
        context['categories'] = news.clubs.all()
        return context

    # def get(self, request, *args, **kwargs):
    #     slug = self.kwargs.get('slug')
    #     print("Requested slug:", slug)
    #     return super().get(request, *args, **kwargs)


class NewsDetailMobile(DetailView):
    model = News
    template_name = 'venom/news_detail_mobile.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'newsdetailmobile'



class PromoDetailMobile(DetailView):
    model = ClubPromo
    template_name = 'venom/promo_detail_mobile.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'promodetailmobile'







class Franchise(TemplateView):
    template_name = 'venom/franchise.html'
    context_object_name = 'all_content'

    def get_queryset(self):
        seo = FranchisePageSeo.objects.all()
        homegallery = HomeGallery.objects.filter(is_published=True)
        all_content = list(chain(seo, homegallery))
        return all_content

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        seo_object = FranchisePageSeo.objects.first()
        context['seo'] = seo_object if seo_object else None
        homegallery = HomeGallery.objects.filter(is_published=True)
        context['homegallery'] = homegallery
        context["franchisepage"] = FranchisePage.get_solo
        return context


    def get(self, request, *args, **kwargs):
        user_agent = get_user_agent(request)

        if user_agent.is_mobile:
            # Если это мобильное устройство, используйте другой шаблон
            self.template_name = 'venom/mobile/franchise.html'

        return super().get(request, *args, **kwargs)





class PoliticsPage(TemplateView):
    template_name = 'venom/politics.html'

class PoliticsPageMobile(TemplateView):
    template_name = 'venom/mobile/politics.html'




class ContactPage(TemplateView):
    template_name = 'venom/contact.html'
    context_object_name = 'all_content'

    def get_queryset(self):
        seo = ContactPageSeo.objects.last()
        return seo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        seo = self.get_queryset()  # Получаем объект ClubPageSeo
        context['seo'] = seo  # Добавляем объект ClubPageSeo в контекст
        context['clubs_images'] = ContactPageZonesImages.objects.all()  
        context["clubs"] = Club.objects.all()
        return context


    def get(self, request, *args, **kwargs):
        user_agent = get_user_agent(request)

        if user_agent.is_mobile:
            # Если это мобильное устройство, используйте другой шаблон
            self.template_name = 'venom/mobile/contact.html'

        return super().get(request, *args, **kwargs)











# VDNH Club

# class VdnhClub(ListView):
#     model = VdnhNews
#     template_name = 'venom/vdnh.html'
#     context_object_name = 'content_vdnhnews'

class VdnhClub(ListView):
    template_name = 'venom/vdnh.html'
    context_object_name = 'all_content'

    def get_queryset(self):
        newsVdnh = VdnhNews.objects.filter(is_published=True).order_by('-sort', '-time_create')
        promoVdnh = VdnhPromo.objects.filter(is_published=True)
        zonesVdnh = VdnhZones.objects.filter(is_published=True)
        zonesVdnhNew = VdnhZonesNew.objects.filter(is_published=True).order_by('-sort', 'time_create')
        vdnhgallery = VdnhGallery.objects.filter(is_published=True)
        news_new_variant = NewsNewVariant.objects.filter(is_published=True, catnews="3").order_by('-sort', '-time_create')
        photos = PhotoVdnx.objects.all().order_by("-order")
        all_content = list(chain(newsVdnh, promoVdnh, zonesVdnh, vdnhgallery, news_new_variant, zonesVdnhNew, photos))
        return all_content

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['newsVdnh'] = [content for content in context['all_content'] if isinstance(content, VdnhNews)]
        context['promoVdnh'] = [content for content in context['all_content'] if isinstance(content, VdnhPromo)]
        context['zonesVdnh'] = [content for content in context['all_content'] if isinstance(content, VdnhZones)]
        context['zonesVdnhNew'] = [content for content in context['all_content'] if isinstance(content, VdnhZonesNew)]
        context['seo'] = VdnhSeo.objects.last()
        context['vdnhgallery'] = [content for content in context['all_content'] if isinstance(content, VdnhGallery)]
        context['photos'] = [content for content in context['all_content'] if isinstance(content, PhotoVdnx)]
        context['news_new_variant'] = [content for content in context['all_content'] if
                                       isinstance(content, NewsNewVariant)]
        context['news_categories'] = {news.id: news.catnews.all() for news in context['news_new_variant']}

        return context

    def get(self, request, *args, **kwargs):
        user_agent = get_user_agent(request)

        if user_agent.is_mobile:
            # Если это мобильное устройство, используйте другой шаблон
            self.template_name = 'venom/mobile/vdnhMobile.html'


        return super().get(request, *args, **kwargs)




class VdnnNewsDetail(DetailView):
    model = VdnhNews
    template_name = 'venom/vdnh/vdnh_news_detail.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'vdnhnews'


class VdnnNewsDetailNew(DetailView):
    model = NewsNewVariant
    template_name = 'venom/vdnh/vdnh_news_detail_news.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'vdnhnews'


class VdnnNewsDetailMobileNew(DetailView):
    model = NewsNewVariant
    template_name = 'venom/vdnh/vdnh_news_detail_mobile_new.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'vdnhnewsmobile'



class VdnnPromoDetail(DetailView):
    model = VdnhPromo
    template_name = 'venom/vdnh/vdnh_promo_detail.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'vdnhpromo'






class VdnnNewsDetailMobile(DetailView):
    model = VdnhNews
    template_name = 'venom/vdnh/vdnh_news_detail_mobile.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'vdnhnewsmobile'



class VdnnPromoDetailMobile(DetailView):
    model = VdnhPromo
    template_name = 'venom/vdnh/vdnh_promo_detail_mobile.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'vdnhpromomobile'










# Vernadka Club

# class VernadkaClub(TemplateView):
#     template_name = 'venom/vernadka.html'


class VernadkaClub(ListView):
    template_name = 'venom/vernadka.html'
    context_object_name = 'all_content'

    def get_queryset(self):
        newsVernadka = VernadkaNews.objects.filter(is_published=True).order_by('-sort', '-time_create')
        promoVernadka = VernadkaPromo.objects.filter(is_published=True)
        zonesVernadka = VernadkaZones.objects.filter(is_published=True)
        zonesVernadkaNew = VernadkaZonesNew.objects.filter(is_published=True).order_by('-sort', 'time_create')
        vernadkagallery = VernadkaGallery.objects.filter(is_published=True)
        news_new_variant = NewsNewVariant.objects.filter(is_published=True, catnews="4").order_by('-sort', '-time_create')
        photos = PhotoVernadka.objects.all().order_by('-order')
        all_content = list(chain(newsVernadka, promoVernadka, zonesVernadka, vernadkagallery, news_new_variant, zonesVernadkaNew, photos))
        return all_content

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['newsVernadka'] = [content for content in context['all_content'] if isinstance(content, VernadkaNews)]
        context['promoVernadka'] = [content for content in context['all_content'] if isinstance(content, VernadkaPromo)]
        context['zonesVernadka'] = [content for content in context['all_content'] if isinstance(content, VernadkaZones)]
        context['zonesVernadkaNew'] = [content for content in context['all_content'] if isinstance(content, VernadkaZonesNew)]
        context['seo'] = VernadkaSeo.objects.last()
        context['vernadkagallery'] = [content for content in context['all_content'] if isinstance(content, VernadkaGallery)]

        context['news_new_variant'] = [content for content in context['all_content'] if
                                       isinstance(content, NewsNewVariant)]
        context['news_categories'] = {news.id: news.catnews.all() for news in context['news_new_variant']}
        context['photos'] = [content for content in context['all_content'] if
                                       isinstance(content, PhotoVernadka)]
        return context

    def get(self, request, *args, **kwargs):
        user_agent = get_user_agent(request)

        if user_agent.is_mobile:
            # Если это мобильное устройство, используйте другой шаблон
            self.template_name = 'venom/mobile/vernadkaMobile.html'

        return super().get(request, *args, **kwargs)




class VernadkaNewsDetail(DetailView):
    model = VernadkaNews
    template_name = 'venom/vernadka/vernadka_news_detail.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'vernadkanews'


class VernadkaNewsDetailNew(DetailView):
    model = NewsNewVariant
    template_name = 'venom/vernadka/vernadka_news_detail_new.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'vernadkanews'


class VernadkaNewsDetailMobileNew(DetailView):
    model = NewsNewVariant
    template_name = 'venom/vernadka/vernadka_news_detail_mobile_new.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'vernadkanewsmobile'



class VernadkaPromoDetail(DetailView):
    model = VernadkaPromo
    template_name = 'venom/vernadka/vernadka_promo_detail.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'vernadkapromo'




class VernadkaNewsDetailMobile(DetailView):
    model = VernadkaNews
    template_name = 'venom/vernadka/vernadka_news_detail_mobile.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'vernadkanewsmobile'


class VernadkaPromoDetailMobile(DetailView):
    model = VernadkaPromo
    template_name = 'venom/vernadka/vernadka_promo_detail_mobile.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'vernadkapromomobile'














# Mitino Club

# class MitinoClub(TemplateView):
#     template_name = 'venom/mitino.html'

class MitinoClub(ListView):
    template_name = 'venom/mitino.html'
    context_object_name = 'all_content'

    def get_queryset(self):
        newsMitino = MitinoNews.objects.filter(is_published=True).order_by('-sort', '-time_create')
        promoMitino = MitinoPromo.objects.filter(is_published=True)
        zonesMitino = MitinoZones.objects.filter(is_published=True)
        zonesMitinoNew = MitinoZonesNew.objects.filter(is_published=True).order_by('-sort', 'time_create')
        mitinogallery = MitinoGallery.objects.filter(is_published=True)
        news_new_variant = NewsNewVariant.objects.filter(is_published=True, catnews="5").order_by('-sort', '-time_create')
        photos = PhotoMitino.objects.all().order_by('-order')
        all_content = list(chain(newsMitino, promoMitino, zonesMitino, mitinogallery, news_new_variant, zonesMitinoNew, photos))
        return all_content

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['newsMitino'] = [content for content in context['all_content'] if isinstance(content, MitinoNews)]
        context['promoMitino'] = [content for content in context['all_content'] if isinstance(content, MitinoPromo)]
        context['zonesMitino'] = [content for content in context['all_content'] if isinstance(content, MitinoZones)]
        context['zonesMitinoNew'] = [content for content in context['all_content'] if isinstance(content, MitinoZonesNew)]
        context['seo'] = MitinoSeo.objects.last()
        context['mitinogallery'] = [content for content in context['all_content'] if isinstance(content, MitinoGallery)]

        context['news_new_variant'] = [content for content in context['all_content'] if
                                       isinstance(content, NewsNewVariant)]
        context['news_categories'] = {news.id: news.catnews.all() for news in context['news_new_variant']}
        context['photos'] = [content for content in context['all_content'] if
                                       isinstance(content, PhotoMitino)]
        return context

    def get(self, request, *args, **kwargs):
        user_agent = get_user_agent(request)

        if user_agent.is_mobile:
            # Если это мобильное устройство, используйте другой шаблон
            self.template_name = 'venom/mobile/mitinoMobile.html'

        return super().get(request, *args, **kwargs)


class MitinoNewsDetail(DetailView):
    model = MitinoNews
    template_name = 'venom/mitino/mitino_news_detail.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'mitinonews'

class MitinoNewsDetailNew(DetailView):
    model = NewsNewVariant
    template_name = 'venom/mitino/mitino_news_detail_new.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'mitinonews'


class MitinoNewsDetailMobileNew(DetailView):
    model = NewsNewVariant
    template_name = 'venom/mitino/mitino_news_detail_mobile_new.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'mitinonewsmobile'


class MitinoPromoDetail(DetailView):
    model = MitinoPromo
    template_name = 'venom/mitino/mitino_promo_detail.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'mitinopromo'



class MitinoNewsDetailMobile(DetailView):
    model = MitinoNews
    template_name = 'venom/mitino/mitino_news_detail_mobile.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'mitinonewsmobile'


class MitinoPromoDetailMobile(DetailView):
    model = MitinoPromo
    template_name = 'venom/mitino/mitino_promo_detail_mobile.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'mitinopromomobile'











# Koptevo Club

# class KoptevoClub(TemplateView):
#     template_name = 'venom/koptevo.html'

class KoptevoClub(ListView):
    template_name = 'venom/koptevo.html'
    context_object_name = 'all_content'

    def get_queryset(self):
        newsKoptevo = KoptevoNews.objects.filter(is_published=True)
        promoKoptevo = KoptevoPromo.objects.filter(is_published=True)
        zonesKoptevo = KoptevoZones.objects.filter(is_published=True)
        koptevogallery = KoptevoGallery.objects.filter(is_published=True)
        all_content = list(chain(newsKoptevo, promoKoptevo, zonesKoptevo, koptevogallery))
        return all_content

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['newsKoptevo'] = [content for content in context['all_content'] if isinstance(content, KoptevoNews)]
        context['promoKoptevo'] = [content for content in context['all_content'] if isinstance(content, KoptevoPromo)]
        context['zonesKoptevo'] = [content for content in context['all_content'] if isinstance(content, KoptevoZones)]
        context['seo'] = KoptevoSeo.objects.last()
        context['koptevogallery'] = [content for content in context['all_content'] if isinstance(content, KoptevoGallery)]
        return context

    def get(self, request, *args, **kwargs):
        user_agent = get_user_agent(request)

        if user_agent.is_mobile:
            # Если это мобильное устройство, используйте другой шаблон
            self.template_name = 'venom/mobile/koptevoMobile.html'

        return super().get(request, *args, **kwargs)


class KoptevoNewsDetail(DetailView):
    model = KoptevoNews
    template_name = 'venom/koptevo/koptevo_news_detail.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'koptevonews'



class KoptevoPromoDetail(DetailView):
    model = KoptevoPromo
    template_name = 'venom/koptevo/koptevo_promo_detail.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'koptevopromo'



class KoptevoNewsDetailMobile(DetailView):
    model = KoptevoNews
    template_name = 'venom/koptevo/koptevo_news_detail_mobile.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'koptevonewsmobile'



class KoptevoPromoDetailMobile(DetailView):
    model = KoptevoPromo
    template_name = 'venom/koptevo/koptevo_promo_detail_mobile.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'koptevopromomobile'













# Zulebino Club

# class ZulebinoClub(TemplateView):
#     template_name = 'venom/zulebino.html'


class ZulebinoClub(ListView):
    template_name = 'venom/zulebino.html'
    context_object_name = 'all_content'

    def get_queryset(self):
        newsZulebino = ZulebinoNews.objects.filter(is_published=True)
        promoZulebino = ZulebinoPromo.objects.filter(is_published=True)
        zonesZulebino = ZulebinoZones.objects.filter(is_published=True)
        zulebinogallery = ZulebinoGallery.objects.filter(is_published=True)
        news_new_variant = NewsNewVariant.objects.filter(is_published=True, catnews="7").order_by('-sort', '-time_create')
        all_content = list(chain(newsZulebino, promoZulebino, zonesZulebino, zulebinogallery, news_new_variant))
        return all_content

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['newsZulebino'] = [content for content in context['all_content'] if isinstance(content, ZulebinoNews)]
        context['promoZulebino'] = [content for content in context['all_content'] if isinstance(content, ZulebinoPromo)]
        context['zonesZulebino'] = [content for content in context['all_content'] if isinstance(content, ZulebinoZones)]
        context['seo'] = ZulebinoSeo.objects.last()
        context['zulebinogallery'] = [content for content in context['all_content'] if isinstance(content, ZulebinoGallery)]

        context['news_new_variant'] = [content for content in context['all_content'] if
                                       isinstance(content, NewsNewVariant)]
        context['news_categories'] = {news.id: news.catnews.all() for news in context['news_new_variant']}


        return context

    def get(self, request, *args, **kwargs):
        user_agent = get_user_agent(request)

        if user_agent.is_mobile:
            # Если это мобильное устройство, используйте другой шаблон
            self.template_name = 'venom/mobile/zulebinoMobile.html'

        return super().get(request, *args, **kwargs)


class ZulebinoNewsDetail(DetailView):
    model = ZulebinoNews
    template_name = 'venom/zulebino/zulebino_news_detail.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'zulebinonews'

class ZulebinoNewsDetailNew(DetailView):
    model = NewsNewVariant
    template_name = 'venom/zulebino/zulebino_news_detail_new.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'zulebinonews'


class ZulebinoNewsDetailMobileNew(DetailView):
    model = NewsNewVariant
    template_name = 'venom/zulebino/zulebino_news_detail_mobile_new.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'zulebinonewsmobile'


class ZulebinoPromoDetail(DetailView):
    model = ZulebinoPromo
    template_name = 'venom/zulebino/zulebino_promo_detail.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'zulebinopromo'


class ZulebinoNewsDetailMobile(DetailView):
    model = ZulebinoNews
    template_name = 'venom/zulebino/zulebino_news_detail_mobile.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'zulebinonewsmobile'


class ZulebinoPromoDetailMobile(DetailView):
    model = ZulebinoPromo
    template_name = 'venom/zulebino/zulebino_promo_detail_mobile.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'zulebinopromomobile'












# Zukovsky Club

# class ZukovskyClub(TemplateView):
#     template_name = 'venom/zukovsky.html'


class ZukovskyClub(ListView):
    template_name = 'venom/zukovsky.html'
    context_object_name = 'all_content'

    def get_queryset(self):
        newsZukovsky = ZukovskyNews.objects.filter(is_published=True)
        promoZukovsky = ZukovskyPromo.objects.filter(is_published=True)
        zonesZukovsky = ZukovskyZones.objects.filter(is_published=True)
        zukovskygallery = ZukovskyGallery.objects.filter(is_published=True)
        news_new_variant = NewsNewVariant.objects.filter(is_published=True, catnews="8").order_by('-sort', '-time_create')
        all_content = list(chain(newsZukovsky, promoZukovsky, zonesZukovsky, zukovskygallery, news_new_variant))
        return all_content

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['newsZukovsky'] = [content for content in context['all_content'] if isinstance(content, ZukovskyNews)]
        context['promoZukovsky'] = [content for content in context['all_content'] if isinstance(content, ZukovskyPromo)]
        context['zonesZukovsky'] = [content for content in context['all_content'] if isinstance(content, ZukovskyZones)]
        context['seo'] = ZukovskySeo.objects.last()
        context['zukovskygallery'] = [content for content in context['all_content'] if isinstance(content, ZukovskyGallery)]

        context['news_new_variant'] = [content for content in context['all_content'] if
                                       isinstance(content, NewsNewVariant)]
        context['news_categories'] = {news.id: news.catnews.all() for news in context['news_new_variant']}

        return context

    def get(self, request, *args, **kwargs):
        user_agent = get_user_agent(request)

        if user_agent.is_mobile:
            # Если это мобильное устройство, используйте другой шаблон
            self.template_name = 'venom/mobile/zukovskyMobile.html'

        return super().get(request, *args, **kwargs)


class ZukovskyNewsDetail(DetailView):
    model = ZukovskyNews
    template_name = 'venom/zukovsky/zukovsky_news_detail.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'zukovskynews'


class ZukovskyNewsDetailNew(DetailView):
    model = NewsNewVariant
    template_name = 'venom/zukovsky/zukovsky_news_detail_new.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'zukovskynews'


class ZukovskyNewsDetailMobileNew(DetailView):
    model = NewsNewVariant
    template_name = 'venom/zukovsky/zukovsky_news_detail_mobile_new.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'zukovskynewsmobile'


class ZukovskyPromoDetail(DetailView):
    model = ZukovskyPromo
    template_name = 'venom/zukovsky/zukovsky_promo_detail.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'zukovskypromo'



class ZukovskyNewsDetailMobile(DetailView):
    model = ZukovskyNews
    template_name = 'venom/zukovsky/zukovsky_news_detail_mobile.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'zukovskynewsmobile'



class ZukovskyPromoDetailMobile(DetailView):
    model = ZukovskyPromo
    template_name = 'venom/zukovsky/zukovsky_promo_detail_mobile.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'zukovskypromomobile'











# Serpuhovskaya Club

# class SerpuhovskayaClub(TemplateView):
#     template_name = 'venom/serpuhovskaya.html'

class SerpuhovskayaClub(ListView):
    template_name = 'venom/serpuhovskaya.html'
    context_object_name = 'all_content'

    def get_queryset(self):
        newsSerpuhovskaya = SerpuhovskayaNews.objects.filter(is_published=True).order_by('-sort', '-time_create')
        promoSerpuhovskaya = SerpuhovskayaPromo.objects.filter(is_published=True)
        zonesSerpuhovskaya = SerpuhovskayaZones.objects.filter(is_published=True)
        zonesSerpuhovskayaNew = SerpuhovskayaZonesNew.objects.filter(is_published=True).order_by('-sort', 'time_create')
        serpuhovskayagallery = SerpuhovskayaGallery.objects.filter(is_published=True)
        news_new_variant = NewsNewVariant.objects.filter(is_published=True, catnews="9").order_by('-sort', '-time_create')
        photos = PhotoSerpuhskaya.objects.all().order_by('-order')
        all_content = list(chain(newsSerpuhovskaya, promoSerpuhovskaya, zonesSerpuhovskaya, serpuhovskayagallery, news_new_variant, zonesSerpuhovskayaNew, photos))
        return all_content

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['newsSerpuhovskaya'] = [content for content in context['all_content'] if isinstance(content, SerpuhovskayaNews)]
        context['promoSerpuhovskaya'] = [content for content in context['all_content'] if isinstance(content, SerpuhovskayaPromo)]
        context['zonesSerpuhovskaya'] = [content for content in context['all_content'] if isinstance(content, SerpuhovskayaZones)]
        context['zonesSerpuhovskayaNew'] = [content for content in context['all_content'] if isinstance(content, SerpuhovskayaZonesNew)]
        context['seo'] = SerpuhovkayaSeo.objects.last()
        context['serpuhovskayagallery'] = [content for content in context['all_content'] if isinstance(content, SerpuhovskayaGallery)]

        context['news_new_variant'] = [content for content in context['all_content'] if
                                       isinstance(content, NewsNewVariant)]
        context['news_categories'] = {news.id: news.catnews.all() for news in context['news_new_variant']}
        context['photos'] = [content for content in context['all_content'] if
                                       isinstance(content, PhotoSerpuhskaya)]
        return context

    def get(self, request, *args, **kwargs):
        user_agent = get_user_agent(request)

        if user_agent.is_mobile:
            # Если это мобильное устройство, используйте другой шаблон
            self.template_name = 'venom/mobile/serpuhovskayaMobile.html'

        return super().get(request, *args, **kwargs)


class SerpuhovskayaNewsDetail(DetailView):
    model = SerpuhovskayaNews
    template_name = 'venom/serpuhovskaya/serpuhovskaya_news_detail.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'serpuhovskayanews'

class SerpuhovskayaNewsDetailNew(DetailView):
    model = NewsNewVariant
    template_name = 'venom/serpuhovskaya/serpuhovskaya_news_detail_new.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'serpuhovskayanews'



class SerpuhovskayaNewsDetailMobileNew(DetailView):
    model = NewsNewVariant
    template_name = 'venom/serpuhovskaya/serpuhovskaya_news_detail_mobile_new.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'serpuhovskayanewsmobile'


class SerpuhovskayaPromoDetail(DetailView):
    model = SerpuhovskayaPromo
    template_name = 'venom/serpuhovskaya/serpuhovskaya_promo_detail.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'serpuhovskayapromo'



class SerpuhovskayaNewsDetailMobile(DetailView):
    model = SerpuhovskayaNews
    template_name = 'venom/serpuhovskaya/serpuhovskaya_news_detail_mobile.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'serpuhovskayanewsmobile'



class SerpuhovskayaPromoDetailMobile(DetailView):
    model = SerpuhovskayaPromo
    template_name = 'venom/serpuhovskaya/serpuhovskaya_promo_detail_mobile.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'serpuhovskayapromomobile'








# Pushkino Club

# class PushkinoClub(TemplateView):
#     template_name = 'venom/pushkino.html'


class PushkinoClub(View):
    def get(self, request, *args, **kwargs):
        return redirect('home')



# class PushkinoClub(ListView):
#     template_name = 'venom/pushkino.html'
#     context_object_name = 'all_content'
#
#     def get_queryset(self):
#         newsPushkino = PushkinoNews.objects.filter(is_published=True)
#         promoPushkino = PushkinoPromo.objects.filter(is_published=True)
#         zonesPushkino = PushkinoZones.objects.filter(is_published=True)
#         pushkinogallery = PushkinoGallery.objects.filter(is_published=True)
#         news_new_variant = NewsNewVariant.objects.filter(is_published=True, catnews="10").order_by('-sort', '-time_create')
#         all_content = list(chain(newsPushkino, promoPushkino, zonesPushkino, pushkinogallery, news_new_variant))
#         return all_content
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['newsPushkino'] = [content for content in context['all_content'] if isinstance(content, PushkinoNews)]
#         context['promoPushkino'] = [content for content in context['all_content'] if isinstance(content, PushkinoPromo)]
#         context['zonesPushkino'] = [content for content in context['all_content'] if isinstance(content, PushkinoZones)]
#         context['seo'] = PushkinoSeo.objects.last()
#         context['pushkinogallery'] = [content for content in context['all_content'] if isinstance(content, PushkinoGallery)]
#         context['news_new_variant'] = [content for content in context['all_content'] if
#                                        isinstance(content, NewsNewVariant)]
#         context['news_categories'] = {news.id: news.catnews.all() for news in context['news_new_variant']}
#
#         return context
#
#     def get(self, request, *args, **kwargs):
#         user_agent = get_user_agent(request)
#
#         if user_agent.is_mobile:
#             self.template_name = 'venom/mobile/pushkinoMobile.html'
#
#         return super().get(request, *args, **kwargs)




class PushkinoNewsDetail(DetailView):
    model = PushkinoNews
    template_name = 'venom/pushkino/pushkino_news_detail.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'pushkinonews'


class PushkinoNewsDetailNew(DetailView):
    model = NewsNewVariant
    template_name = 'venom/pushkino/pushkino_news_detail_new.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'pushkinonews'

class PushkinoNewsDetailMobileNew(DetailView):
    model = NewsNewVariant
    template_name = 'venom/pushkino/pushkino_news_detail_mobile_new.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'pushkinonewsmobile'



class PushkinoPromoDetail(DetailView):
    model = PushkinoPromo
    template_name = 'venom/pushkino/pushkino_promo_detail.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'pushkinopromo'



class PushkinoNewsDetailMobile(DetailView):
    model = PushkinoNews
    template_name = 'venom/pushkino/pushkino_news_detail_mobile.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'pushkinonewsmobile'



class PushkinoPromoDetailMobile(DetailView):
    model = PushkinoPromo
    template_name = 'venom/pushkino/pushkino_promo_detail_mobile.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'pushkinopromomobile'












# Mahachkala Club

# class MahachkalaClub(TemplateView):
#     template_name = 'venom/mahachkala.html'


# class MahachkalaClub(View):
#     def get(self, request, *args, **kwargs):
#         return redirect('home')

class MahachkalaClub(ListView):
    template_name = 'venom/mahachkala.html'
    context_object_name = 'all_content'

    def get_queryset(self):
        newsMahachkala = MahachkalaNews.objects.filter(is_published=True)
        promoMahachkala = MahachkalaPromo.objects.filter(is_published=True)
        zonesMahachkala = MahachkalaZoness.objects.filter(is_published=True).order_by('sort')
        mahachkalagallery = MahachkalaGallery.objects.filter(is_published=True)
        news_new_variant = NewsNewVariant.objects.filter(is_published=True, catnews="11").order_by('-sort', '-time_create')
        photos = PhotoMahachkala.objects.all().order_by('-order')
        all_content = list(chain(newsMahachkala, promoMahachkala, zonesMahachkala, mahachkalagallery, news_new_variant, photos))
        return all_content

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['newsMahachkala'] = [content for content in context['all_content'] if isinstance(content, MahachkalaNews)]
        context['promoMahachkala'] = [content for content in context['all_content'] if isinstance(content, MahachkalaPromo)]
        context['zonesMahachkala'] = [content for content in context['all_content'] if isinstance(content, MahachkalaZoness)]
        context['seo'] = MahachkalaSeo.objects.last()
        context['mahachkalagallery'] = [content for content in context['all_content'] if isinstance(content, MahachkalaGallery)]
        context['news_new_variant'] = [content for content in context['all_content'] if
                                       isinstance(content, NewsNewVariant)]
        context['news_categories'] = {news.id: news.catnews.all() for news in context['news_new_variant']}
        context['photos'] = [content for content in context['all_content'] if
                                       isinstance(content, PhotoMahachkala)]
        return context

    def get(self, request, *args, **kwargs):
        user_agent = get_user_agent(request)

        if user_agent.is_mobile:
            self.template_name = 'venom/mobile/mahachkalaMobile.html'

        return super().get(request, *args, **kwargs)



class MahachkalaNewsDetail(DetailView):
    model = MahachkalaNews
    template_name = 'venom/mahachkala/mahachkala_news_detail.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'mahachkalanews'

class MahachkalaNewsDetailNew(DetailView):
    model = NewsNewVariant
    template_name = 'venom/mahachkala/mahachkala_news_detail_new.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'mahachkalanews'


class MahachkalaNewsDetailMobileNew(DetailView):
    model = NewsNewVariant
    template_name = 'venom/mahachkala/mahachkala_news_detail_mobile_new.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'mahachkalanewsmobile'



class MahachkalaPromoDetail(DetailView):
    model = MahachkalaPromo
    template_name = 'venom/mahachkala/mahachkala_promo_detail.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'mahachkalapromo'



class MahachkalaNewsDetailMobile(DetailView):
    model = MahachkalaNews
    template_name = 'venom/mahachkala/mahachkala_news_detail_mobile.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'mahachkalanewsmobile'


class MahachkalaPromoDetailMobile(DetailView):
    model = MahachkalaPromo
    template_name = 'venom/mahachkala/mahachkala_promo_detail_mobile.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'mahachkalapromomobile'










def logout_user(request):
    logout(request)
    return redirect('home')


class ClubPageView(ListView):
    template_name = 'club.html'
    context_object_name = 'all_content'

    def get_queryset(self):
        # Определяем клуб по slug
        self.club = get_object_or_404(Club, slug=self.kwargs["club_slug"])

        # Собираем контент по клубу
        news = ClubNews.objects.filter(club=self.club, is_published=True).order_by('-sort', '-time_create')
        promos = ClubPromo.objects.filter(clubs=self.club, is_published=True).order_by('-sort', '-time_create')
        zones = ClubZonesNew.objects.filter(club=self.club, is_published=True).order_by('sort', 'time_create')
        gallery = ClubGallery.objects.filter(club=self.club, is_published=True).order_by('id')
        photos = PhotoClub.objects.filter(club=self.club).order_by('-order')
        news_new_variant = NewsNew.objects.filter(is_published=True, clubs=self.club).order_by('-sort', '-time_create')
        route = ClubRoute.objects.filter(club=self.club)
        print(news_new_variant)
        # Объединяем все сущности в общий список, если тебе нужно их рендерить циклом
        all_content = list(chain(news, promos, zones, gallery, photos, news_new_variant, route))
        return all_content

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Добавляем клуб и SEO
        club = getattr(self, 'club', None)
        context["club"] = club
        context["seo"] = getattr(club, "seo", None)

        # Разделяем контент по типам (удобно для шаблонов)
        all_content = context.get("all_content", [])
        context["news"] = [obj for obj in all_content if isinstance(obj, ClubNews)]
        context["promos"] = [obj for obj in all_content if isinstance(obj, ClubPromo)]
        context["zones"] = [obj for obj in all_content if isinstance(obj, ClubZonesNew)]
        context["gallery"] = [obj for obj in all_content if isinstance(obj, ClubGallery)]
        context["photos"] = [obj for obj in all_content if isinstance(obj, PhotoClub)]
        context['news_new_variant'] = [content for content in context['all_content'] if
                                       isinstance(content, NewsNew)]
        context["pc_games"] = club.get_pc_games()
        context["tv_games"] = club.get_tv_games()
        context["route"] = getattr(club, "route", None)
        context["bottom_about"] = getattr(club, "bottom_about", None)
        # context['news_categories'] = {news.id: news.catnews.all() for news in context['news_new_variant']}

        return context

    def get(self, request, *args, **kwargs):
        user_agent = get_user_agent(request)

        # Определяем шаблон под мобильную версию
        if hasattr(user_agent, "is_mobile") and user_agent.is_mobile:
            self.template_name = "venom/club_mobile.html"
        else:
            self.template_name = "venom/club.html"

        return super().get(request, *args, **kwargs)


class NewsNewDetailView(DetailView):
    """
    Универсальная страница новости.
    Работает как для клубных новостей, так и для главных.
    """
    model = NewsNew
    template_name = "venom/newsDetail.html"
    context_object_name = "news"
    slug_url_kwarg = "slug"

    def get_queryset(self):
        """
        Определяем queryset:
        - если есть club_slug → фильтруем новости, связанные с этим клубом;
        - иначе выводим только общие новости (is_main_page=True или без клубов).
        """
        club_slug = self.kwargs.get("club_slug")

        if club_slug:
            return (
                NewsNew.objects
                .filter(
                    Q(clubs__slug=club_slug) |
                    Q(is_main_page=True),  # можно включить и общие, если нужно
                    is_published=True
                )
                .distinct()
            )
        else:
            # Главные или общие новости
            return NewsNew.objects.filter(
                Q(is_main_page=True) | Q(clubs__isnull=True),
                is_published=True
            ).distinct()

    def get_context_data(self, **kwargs):
        """
        Добавляем клуб (если есть) и SEO.
        """
        context = super().get_context_data(**kwargs)
        club_slug = self.kwargs.get("club_slug")

        if club_slug:
            club = get_object_or_404(Club, slug=club_slug)
            context["club"] = club
            context["seo"] = getattr(club, "seo", None)
        else:
            context["club"] = None
            context["seo"] = None

        # 🔹 Дополнительно: показываем, для каких клубов новость относится
        context["related_clubs"] = self.object.clubs.all()

        return context

    def get(self, request, *args, **kwargs):
        """
        Определяем шаблон под мобильную версию.
        """
        user_agent = get_user_agent(request)

        if hasattr(user_agent, "is_mobile") and user_agent.is_mobile:
            self.template_name = "venom/news_detail_mobile_new.html"
        else:
            self.template_name = "venom/newsDetail.html"

        return super().get(request, *args, **kwargs)


class ClubPromoDetailView(DetailView):
    """
    Универсальная страница акции клуба.
    URL: /clubs/<club_slug>/promo/<slug>/
    """
    model = ClubPromo
    template_name = 'venom/promo_detail.html'
    context_object_name = 'promo'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        """
        Фильтруем акции по клубу, чтобы slug был уникален в его рамках.
        """
        return (
            ClubPromo.objects
            .filter(
                clubs__slug=self.kwargs["club_slug"],
                is_published=True
            )
        )

    def get_context_data(self, **kwargs):
        """
        Добавляем клуб и SEO в контекст шаблона.
        """
        context = super().get_context_data(**kwargs)
        club = get_object_or_404(Club, slug=self.kwargs["club_slug"])
        context["club"] = club
        context["seo"] = getattr(club, "seo", None)
        return context
    
    def get(self, request, *args, **kwargs):
        user_agent = get_user_agent(request)

        # Определяем шаблон под мобильную версию
        if hasattr(user_agent, "is_mobile") and user_agent.is_mobile:
            self.template_name = "venom/promo_detail_mobile.html"
        else:
            self.template_name = "venom/promo_detail.html"

        return super().get(request, *args, **kwargs)