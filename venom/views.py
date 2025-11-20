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
        context['promos'] = ClubPromo.objects.filter(is_published=True).filter(is_main_page=True).order_by('-sort')
        context['news'] = [content for content in context['all_content'] if isinstance(content, News)]
        context['seo'] = PromoPageSeo.objects.last()
        context['news_new_variant'] = [content for content in context['all_content'] if
                                       isinstance(content, NewsNewVariant)]

        latest_news = NewsNew.objects.filter(is_published=True).filter(is_main_page=True).order_by('-sort', '-time_create', '-id')
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
    context_object_name = 'news'

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
    context_object_name = 'promo'
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)

    #     context["promo"] = ClubPromo.objects.filter(slug=)







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
            context["newsdetailmobile"] = club
            context["seo"] = getattr(club, "seo", None)
        else:
            context["club"] = None
            context["seo"] = None

        # 🔹 Дополнительно: показываем, для каких клубов новость относится
        context["related_clubs"] = self.object.clubs.all()

        print(context)

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