from django.urls import path
from . import views

urlpatterns = [
    path('yetkazib-beruvchi/create/', views.create_yetkazib_beruvchi, name='create-yetkazib-beruvchi'),
    path('yetkazib-beruvchi/', views.YetkazibBeruvchiListView.as_view(), name='yetkazib-beruvchi-list'),
    path('chiqimlar/create/', views.create_chiqim, name='create-chiqim'),
    path('chiqimlar/', views.ChiqimListView.as_view(), name='chiqim-list'),
    path('mahsulot/create/', views.create_mahsulot, name='create-mahsulot'),
    path('mahsulot/', views.MahsulotlarListView.as_view(), name='mahsulot-list'),
    path('tushumlar/create/', views.create_kirim, name='create-kirim'),
    path('tushumlar/', views.KirimlarListView.as_view(), name='kirim-list'),
]
