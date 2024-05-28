from django.contrib import admin
from .models import Kategoriyalar, Yetkazib_beruvchilar, Chiqimlar, Mahsulotlar,Kirimlar, Omborxona

class KategoriyalarAdmin(admin.ModelAdmin):
    list_display = ('nomi',)
    search_fields = ('nomi',)

class YetkazibBeruvchilarAdmin(admin.ModelAdmin):
    list_display = ('FISH', 'INN', 'address', 'created_date')
    search_fields = ('FISH', 'INN', 'address')
    list_filter = ('created_date',)

class ChiqimlarAdmin(admin.ModelAdmin):
    list_display = ('mahsulot','miqdori','ism', 'familiya', 'telefon', 'created_date')
    search_fields = ('ism', 'familiya', 'telefon')
    list_filter = ('created_date',)

class MahsulotlarAdmin(admin.ModelAdmin):
    list_display = ('nomi', 'narxi', 'kategoriya', 'ulchov_birligi', 'created_date')
    search_fields = ('nomi',)
    list_filter = ('kategoriya', 'ulchov_birligi', 'created_date')

class OmborxonaAdmin(admin.ModelAdmin):
    list_display = ('mahsulot','umumiy_soni', 'umumiy_narx')
    search_fields = ('mahsulot__nomi',)
    list_filter = ('umumiy_soni','umumiy_narx')

class KirimlarAdmin(admin.ModelAdmin):
    list_display = ('mahsulot', 'yetkazib_beruvchi', 'soni', 'narx', 'keltirilgan_sana')
    search_fields = ('mahsulot__nomi', 'yetkazib_beruvchi__FISH')
    list_filter = ('keltirilgan_sana',)

admin.site.register(Kategoriyalar, KategoriyalarAdmin)
admin.site.register(Yetkazib_beruvchilar, YetkazibBeruvchilarAdmin)
admin.site.register(Kirimlar, KirimlarAdmin)
admin.site.register(Chiqimlar, ChiqimlarAdmin)

admin.site.register(Mahsulotlar, MahsulotlarAdmin)
admin.site.register(Omborxona, OmborxonaAdmin)
