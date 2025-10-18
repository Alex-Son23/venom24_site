from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    # path('', cache_page(60 * 1)(HomePageView.as_view()), name='home'),

    path('clubs/', ClubsPage.as_view(), name='clubs'),
    # path('clubs/', cache_page(60 * 1)(ClubsPage.as_view()), name='clubs'),


    # path('clubs/vdnh/', VdnhClub.as_view(), name='vdnh'),
    # path('clubs/vdnh/news/<slug:slug>', VdnnNewsDetail.as_view(), name='vdnhdetailnews'),
    # path('clubs/vdnh/novosti/<slug:slug>', VdnnNewsDetailNew.as_view(), name='vdnhdetailnewsnew'),
    # path('clubs/vdnh/promo/<slug:slug>', VdnnPromoDetail.as_view(), name='vdnhdetailpromo'),

    # path('clubs/vdnh/newsmobile/<slug:slug>', VdnnNewsDetailMobile.as_view(), name='vdnhdetailnewsmobile'),
    # path('clubs/vdnh/promomobile/<slug:slug>', VdnnPromoDetailMobile.as_view(), name='vdnhdetailpromomobile'),
    # path('clubs/vdnh/novostimobilevdnh/<slug:slug>', VdnnNewsDetailMobileNew.as_view(), name='vdnhdetailnewsmobilenew'),





    # path('clubs/vernadka/', VernadkaClub.as_view(), name='vernadka'),
    # path('clubs/vernadka/news/<slug:slug>', VernadkaNewsDetail.as_view(), name='vernadkadetailnews'),
    # path('clubs/vernadka/novosti/<slug:slug>', VernadkaNewsDetailNew.as_view(), name='vernadkadetailnewsnew'),
    # path('clubs/vernadka/promo/<slug:slug>', VernadkaPromoDetail.as_view(), name='vernadkadetailpromo'),

    # path('clubs/vernadka/newsmobile/<slug:slug>', VernadkaNewsDetailMobile.as_view(), name='vernadkadetailnewsmobile'),
    # path('clubs/vernadka/promomobile/<slug:slug>', VernadkaPromoDetailMobile.as_view(), name='vernadkadetailpromomobile'),

    # path('clubs/vernadka/novostimobile/<slug:slug>', VernadkaNewsDetailMobileNew.as_view(), name='vernadkadetailnewsmobilenew'),






    # path('clubs/mitino/', MitinoClub.as_view(), name='mitino'),
    # path('clubs/mitino/news/<slug:slug>', MitinoNewsDetail.as_view(), name='mitinodetailnews'),
    # path('clubs/mitino/novosti/<slug:slug>', MitinoNewsDetailNew.as_view(), name='mitinodetailnewsnew'),
    # path('clubs/mitino/promo/<slug:slug>', MitinoPromoDetail.as_view(), name='mitinodetailpromo'),

    # path('clubs/mitino/newsmobile/<slug:slug>', MitinoNewsDetailMobile.as_view(), name='mitinodetailnewsmobile'),
    # path('clubs/mitino/promomobile/<slug:slug>', MitinoPromoDetailMobile.as_view(), name='mitinodetailpromomobile'),

    # path('clubs/mitino/novostimobile/<slug:slug>', MitinoNewsDetailMobileNew.as_view(), name='mitinodetailnewsmobilenew'),





    # path('clubs/coptevo/', KoptevoClub.as_view(), name='coptevo'),
    # path('clubs/coptevo/news/<slug:slug>', KoptevoNewsDetail.as_view(), name='coptevodetailnews'),
    # path('clubs/coptevo/promo/<slug:slug>', KoptevoPromoDetail.as_view(), name='coptevodetailpromo'),

    # path('clubs/coptevo/newsmobile/<slug:slug>', KoptevoNewsDetailMobile.as_view(), name='coptevodetailnewsmobile'),
    # path('clubs/coptevo/promomobile/<slug:slug>', KoptevoPromoDetailMobile.as_view(), name='coptevodetailpromomobile'),





    # path('clubs/zulebino/', ZulebinoClub.as_view(), name='zulebino'),
    # path('clubs/zulebino/news/<slug:slug>', ZulebinoNewsDetail.as_view(), name='zulebinodetailnews'),
    # path('clubs/zulebino/novosti/<slug:slug>', ZulebinoNewsDetailNew.as_view(), name='zulebinodetailnewsnew'),
    # path('clubs/zulebino/promo/<slug:slug>', ZulebinoPromoDetail.as_view(), name='zulebinodetailpromo'),

    # path('clubs/zulebino/newsmobile/<slug:slug>', ZulebinoNewsDetailMobile.as_view(), name='zulebinodetailnewsmobile'),
    # path('clubs/zulebino/promomobile/<slug:slug>', ZulebinoPromoDetailMobile.as_view(), name='zulebinodetailpromomobile'),

    # path('clubs/zulebino/novostimobile/<slug:slug>', ZulebinoNewsDetailMobileNew.as_view(), name='zulebinodetailnewsmobilenew'),






    # path('clubs/zukovsky/', ZukovskyClub.as_view(), name='zukovsky'),
    # path('clubs/zukovsky/news/<slug:slug>', ZukovskyNewsDetail.as_view(), name='zukovskydetailnews'),
    # path('clubs/zukovsky/novosti/<slug:slug>', ZukovskyNewsDetailNew.as_view(), name='zukovskydetailnewsnew'),
    # path('clubs/zukovsky/promo/<slug:slug>', ZukovskyPromoDetail.as_view(), name='zukovskydetailpromo'),

    # path('clubs/zukovsky/newsmobile/<slug:slug>', ZukovskyNewsDetailMobile.as_view(), name='zukovskydetailnewsmobile'),
    # path('clubs/zukovsky/promomobile/<slug:slug>', ZukovskyPromoDetailMobile.as_view(), name='zukovskydetailpromomobile'),

    # path('clubs/zukovsky/novostimobile/<slug:slug>', ZukovskyNewsDetailMobileNew.as_view(), name='zukovskydetailnewsmobilenew'),






    # path('clubs/serpuhovskaya/', SerpuhovskayaClub.as_view(), name='serpuhovskaya'),
    # path('clubs/serpuhovskaya/news/<slug:slug>', SerpuhovskayaNewsDetail.as_view(), name='serpuhovskayadetailnews'),
    # path('clubs/serpuhovskaya/novosti/<slug:slug>', SerpuhovskayaNewsDetailNew.as_view(), name='serpuhovskayadetailnewsnew'),
    # path('clubs/serpuhovskaya/promo/<slug:slug>', SerpuhovskayaPromoDetail.as_view(), name='serpuhovskayadetailpromo'),

    # path('clubs/serpuhovskaya/newsmobile/<slug:slug>', SerpuhovskayaNewsDetailMobile.as_view(), name='serpuhovskayadetailnewsmobile'),
    # path('clubs/serpuhovskaya/promomobile/<slug:slug>', SerpuhovskayaPromoDetailMobile.as_view(), name='serpuhovskayadetailpromomobile'),

    # path('clubs/serpuhovskaya/novostimobile/<slug:slug>', SerpuhovskayaNewsDetailMobileNew.as_view(), name='serpuhovskayadetailnewsmobilenew'),






    # path('clubs/pushkino/', PushkinoClub.as_view(), name='pushkino'),
    # path('clubs/pushkino/news/<slug:slug>', PushkinoNewsDetail.as_view(), name='pushkinodetailnews'),
    # path('clubs/pushkino/novosti/<slug:slug>', PushkinoNewsDetailNew.as_view(), name='pushkinodetailnewsnew'),
    # path('clubs/pushkino/promo/<slug:slug>', PushkinoPromoDetail.as_view(), name='pushkinodetailpromo'),

    # path('clubs/pushkino/newsmobile/<slug:slug>', PushkinoNewsDetailMobile.as_view(), name='pushkinodetailnewsmobile'),
    # path('clubs/pushkino/promomobile/<slug:slug>', PushkinoPromoDetailMobile.as_view(), name='pushkinodetailpromomobile'),

    # path('clubs/pushkino/novostimobile/<slug:slug>', PushkinoNewsDetailMobileNew.as_view(), name='pushkinodetailnewsmobilenew'),





    # path('clubs/mahachkala/', MahachkalaClub.as_view(), name='mahachkala'),
    # path('clubs/mahachkala/news/<slug:slug>', MahachkalaNewsDetail.as_view(), name='mahachkaladetailnews'),
    # path('clubs/mahachkala/novosti/<slug:slug>', MahachkalaNewsDetailNew.as_view(), name='mahachkaladetailnewsnew'),
    # path('clubs/mahachkala/promo/<slug:slug>', MahachkalaPromoDetail.as_view(), name='mahachkaladetailpromo'),

    # path('clubs/mahachkala/newsmobile/<slug:slug>', MahachkalaNewsDetailMobile.as_view(), name='mahachkaladetailnewsmobile'),
    # path('clubs/mahachkala/promomobile/<slug:slug>', MahachkalaPromoDetailMobile.as_view(), name='mahachkaladetailpromomobile'),

    # path('clubs/mahachkala/novostimobile/<slug:slug>', MahachkalaNewsDetailMobileNew.as_view(), name='mahachkaladetailnewsmobilenew'),





    # path('promo/<str:pk>/', PromoDetail.as_view(), name='promodetail'),
    # path('news/<str:pk>/', NewsDetail.as_view(), name='newsdetail'),

    path('promo/', PromoPageView.as_view(), name='promo'),
    path('promo/<slug:slug>/', PromoDetail.as_view(), name='promodetail'),
    path('news/<slug:slug>/', NewsDetail.as_view(), name='newsdetail'),
    path('novosti/<slug:slug>/', NewsDetailNew.as_view(), name='news_detail_new'),




    path('newsmobile/<slug:slug>/', NewsDetailMobile.as_view(), name='newsdetailmobile'),
    path('promomobile/<slug:slug>/', PromoDetailMobile.as_view(), name='promodetailmobile'),
    path('novostimobile/<slug:slug>/', NewsDetailMobileNew.as_view(), name='news_detailmobile_new'),








    # path('franchise/', FranchisePage.as_view(), name='franchise'),
    # path('franchise/', cache_page(60 * 1)(Franchise.as_view()), name='franchise'),
    path('franchise/', Franchise.as_view(), name='franchise'),




    path('contact/', ContactPage.as_view(), name='contact'),
    # path('contact/', cache_page(60 * 1)(ContactPage.as_view()), name='contact'),

    path('politics/', PoliticsPage.as_view(), name='politics'),
    path('politic/', PoliticsPageMobile.as_view(), name='politic'),


    path('logout/', logout_user, name='logout'),


    path('clubs/<slug:club_slug>/', ClubPageView.as_view(), name='club_page'),
    path('clubs/<slug:club_slug>/news/<slug:slug>/', NewsNewDetailView.as_view(), name='club_news_detail'),
    path('clubs/<slug:club_slug>/promo/<slug:slug>/', ClubPromoDetailView.as_view(), name='club_promo_detail'),
]


