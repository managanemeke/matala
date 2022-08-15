from django.urls import path
from . import views


urlpatterns = [
    #
    path(r'galaka_sava', views.galaka_sava, name="galaka_sava"),
    path(r'galaka_zovo', views.galaka_zovo, name="galaka_zovo"),
    #
    path(r'mara/', views.mara_mara, name='mara_mara'),
    path(r'mara/kara/', views.mara_kara, name='mara_kara'),
    path(r'mara/<str:pk>/',views.mara_saha,name='mara_saha'),
    path(r'mara/<str:pk>/hapa/',views.mara_hapa,name='mara_hapa'),
    path(r'mara/<str:pk>/dala/',views.mara_dala,name='mara_dala'),
    #
    path(r'fara/', views.fara_fara, name='fara_fara'),
    path(r'fara/kara/', views.fara_kara, name='fara_kara'),
    path(r'fara/<str:pk>/',views.fara_saha,name='fara_saha'),
    path(r'fara/<str:pk>/hapa/',views.fara_hapa,name='fara_hapa'),
    path(r'fara/<str:pk>/dala/',views.fara_dala,name='fara_dala'),
    #
    path(r'maka/', views.maka_maka, name='maka_maka'),
    path(r'maka/kara/', views.maka_kara, name='maka_kara'),
    path(r'maka/<str:pk>/',views.maka_saha,name='maka_saha'),
    path(r'maka/<str:pk>/hapa/',views.maka_hapa,name='maka_hapa'),
    path(r'maka/<str:pk>/dala/',views.maka_dala,name='maka_dala'),
    #
    path(r'raza/', views.raza_raza, name='raza_raza'),
    path(r'raza/kara/', views.raza_kara, name='raza_kara'),
    path(r'raza/<str:pk>/',views.raza_saha,name='raza_saha'),
    path(r'raza/<str:pk>/hapa/',views.raza_hapa,name='raza_hapa'),
    path(r'raza/<str:pk>/dala/',views.raza_dala,name='raza_dala'),
    #
    path(r'sata/', views.sata_sata, name='sata_sata'),
    path(r'sata/kara/', views.sata_kara, name='sata_kara'),
    path(r'sata/<str:pk>/',views.sata_saha,name='sata_saha'),
    path(r'sata/<str:pk>/hapa/',views.sata_hapa,name='sata_hapa'),
    path(r'sata/<str:pk>/dala/',views.sata_dala,name='sata_dala'),
    #
    path(r'mata/', views.mata_mata, name='mata_mata'),
    path(r'mata/kara/', views.mata_kara, name='mata_kara'),
    path(r'mata/<str:pk>/',views.mata_saha,name='mata_saha'),
    path(r'mata/<str:pk>/hapa/',views.mata_hapa,name='mata_hapa'),
    path(r'mata/<str:pk>/dala/',views.mata_dala,name='mata_dala'),
    #
    path(r'sava/', views.sava_sava, name='sava_sava'),
    path(r'sava/kara/', views.sava_kara, name='sava_kara'),
    path(r'sava/<str:pk>/',views.sava_saha,name='sava_saha'),
    path(r'sava/<str:pk>/hapa/',views.sava_hapa,name='sava_hapa'),
    path(r'sava/<str:pk>/dala/',views.sava_dala,name='sava_dala'),
    #
    path(r'solo/', views.solo_solo, name='solo_solo'),
    path(r'solo/kara/', views.solo_kara, name='solo_kara'),
    path(r'solo/<str:pk>/',views.solo_saha,name='solo_saha'),
    path(r'solo/<str:pk>/hapa/',views.solo_hapa,name='solo_hapa'),
    path(r'solo/<str:pk>/dala/',views.solo_dala,name='solo_dala'),
    #
    path(r'', views.curcy, name="curcy"),
    path(r'kara/', views.kara, name='teve_kara'),
    path(r'<str:pk>/',views.saha,name='teve_saha'),
    path(r'<str:pk>/hapa/',views.hapa,name='teve_hapa'),
    path(r'<str:pk>/dala/',views.dala,name='teve_dala'),
    #
]