from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),

    path('clubs/', ClubsPage.as_view(), name='clubs'),

    path('promo/', PromoPageView.as_view(), name='promo'),
    path('promo/<slug:slug>/', PromoDetail.as_view(), name='promodetail'),
    path('news/<slug:slug>/', NewsDetail.as_view(), name='newsdetail'),
    path('novosti/<slug:slug>/', NewsDetailNew.as_view(), name='news_detail_new'),




    path('newsmobile/<slug:slug>/', NewsDetailMobile.as_view(), name='newsdetailmobile'),
    path('promomobile/<slug:slug>/', PromoDetailMobile.as_view(), name='promodetailmobile'),
    path('novostimobile/<slug:slug>/', NewsDetailMobileNew.as_view(), name='news_detailmobile_new'),


    path('franchise/', Franchise.as_view(), name='franchise'),




    path('contact/', ContactPage.as_view(), name='contact'),

    path('politics/', PoliticsPage.as_view(), name='politics'),
    path('politic/', PoliticsPageMobile.as_view(), name='politic'),


    path('logout/', logout_user, name='logout'),


    path('clubs/<slug:club_slug>/', ClubPageView.as_view(), name='club_page'),
    path('clubs/<slug:club_slug>/news/<slug:slug>/', NewsNewDetailView.as_view(), name='club_news_detail'),
    path('clubs/<slug:club_slug>/promo/<slug:slug>/', ClubPromoDetailView.as_view(), name='club_promo_detail'),
]


