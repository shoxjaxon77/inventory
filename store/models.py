import datetime
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import User

class Kategoriyalar(models.Model):
    nomi = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.nomi

class Yetkazib_beruvchilar(models.Model):
    FISH = models.CharField(max_length=120)
    INN = models.CharField(max_length=120)
    address = models.CharField(max_length=220)

    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.FISH


class Mahsulotlar(models.Model):
    BIRLIK_CHOICES = [
        ('Грамм', 'Грамм'),
        ('Килограмм', 'Килограмм'),
        ('Штука', 'Штука'),
        ('Коробка', 'Коробка'),
        ('Литр', 'Литр')
    ]

    nomi = models.CharField(max_length=120, unique=True)
    narxi = models.DecimalField(max_digits=10, decimal_places=2)
    kategoriya = models.ForeignKey(Kategoriyalar, on_delete=models.CASCADE)
    ulchov_birligi = models.CharField(max_length=10, choices=BIRLIK_CHOICES)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nomi


class Chiqimlar(models.Model):
    mahsulot = models.ForeignKey(Mahsulotlar,on_delete=models.CASCADE)
    miqdori = models.IntegerField()
    ism = models.CharField(max_length=120)
    familiya = models.CharField(max_length=120)
    telefon = models.CharField(max_length=50)
    sotilgan_sana = models.DateField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.ism} {self.familiya}"





class Kirimlar(models.Model):
    yetkazib_beruvchi = models.ForeignKey(Yetkazib_beruvchilar, on_delete=models.CASCADE)
    mahsulot = models.ForeignKey(Mahsulotlar, on_delete=models.CASCADE) 
    soni = models.IntegerField()
    keltirilgan_sana = models.DateField(default=datetime.date.today)
    narx = models.DecimalField(max_digits=15, decimal_places=2)
    
    def __str__(self):
        return f"{self.mahsulot.nomi} - {self.yetkazib_beruvchi.FISH}"
    



class Omborxona(models.Model):
    mahsulot = models.ForeignKey(Mahsulotlar, on_delete=models.CASCADE,unique=True) 
    umumiy_soni = models.IntegerField()
    umumiy_narx = models.DecimalField(max_digits=15, decimal_places=2)
    
    def __str__(self):
        return f"{self.mahsulot.nomi}"