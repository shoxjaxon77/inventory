from django.urls import path
from . import views

urlpatterns = [
    path('yetkazib-beruvchi/create/', views.create_yetkazib_beruvchi, name='create-yetkazib-beruvchi'),
    path('yetkazib-beruvchi/', views.YetkazibBeruvchiListView.as_view(), name='yetkazib-beruvchi-list'),
    path('chiqimlar/create/', views.create_chiqim, name='create-chiqim'),
    path('chiqimlar/', views.ChiqimListView.as_view(), name='chiqim-list'),
    path('mahsulotlar/create/', views.create_mahsulot, name='create-mahsulot'),
    path('mahsulotlar/', views.MahsulotlarListView.as_view(), name='mahsulot-list'),
    path('tushumlar/create/', views.create_kirim, name='create-kirim'),
    path('tushumlar/', views.KirimlarListView.as_view(), name='kirim-list'),
    path('kirimlar/download/',views.KirimlarXLSXDownloadView.as_view(), name='kirimlar_csv_download'),
    path('download/mahsulotlar/', views.MahsulotlarXLSXDownloadView.as_view(), name='mahsulotlar_xlsx_download'),
    path('download/chiqimlar/', views.ChiqimlarXLSXDownloadView.as_view(), name='chiqimlar_xlsx_download'),
    path('download/yetkazib_beruvchilar/', views.YetkazibBeruvchilarXLSXDownloadView.as_view(), name='yetkazib_beruvchilar_xlsx_download'),
    path('mahsulotlar/edit/<id>/', views.MahsulotlarEditView.as_view(), name='mahsulotlar_edit'),
    path('mahsulotlar/delete/<id>', views.MahsulotlarDeleteView.as_view(), name='mahsulotlar_delete'),
    path('yetkazib-beruvchi/edit/<id>/', views.YetkazibBeruvchilarEditView.as_view(), name='kuryer_edit'),
    path('yetkazib-beruvchi/delete/<id>', views.YetkazibBeruvchilarDeleteView.as_view(), name='kuryer_delete')
]