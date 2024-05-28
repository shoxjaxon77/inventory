from django import forms
from .models import Yetkazib_beruvchilar, Chiqimlar, Mahsulotlar, Kirimlar,Kategoriyalar

class YetkazibBeruvchilarForm(forms.ModelForm):
    class Meta:
        model = Yetkazib_beruvchilar  # Corrected model reference
        fields = ['FISH', 'INN', 'address']  # Corrected field names
        widgets = {
            'FISH': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'FISH',
                'data-val': 'true',
                'data-val-required': 'Please enter FISH',  # Updated validation message
            }),
            'INN': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'INN',
                'data-val': 'true',
                'data-val-required': 'Please enter INN',  # Updated validation message
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'address',
                'data-val': 'true',
                'data-val-required': 'Please enter address',
            }),
        }

class ChiqimForm(forms.ModelForm):
    class Meta:
        model = Chiqimlar
        fields = ['mahsulot', 'miqdori', 'ism', 'familiya', 'telefon', 'sotilgan_sana']  # Define the fields you want to include in the form

        widgets = {
            'mahsulot': forms.Select(attrs={
                'class': 'form-control',
                'id': 'mahsulot',
                'name':'mahsulot'
                # You can add additional attributes if needed
            }),
            'miqdori': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'miqdori',
                'name':'miqdori'
                # You can add additional attributes if needed
            }),
            'ism': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'ism',
                # You can add additional attributes if needed
            }),
            'familiya': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'familiya',
                # You can add additional attributes if needed
            }),
            'telefon': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'telefon',
                # You can add additional attributes if needed
            }),
            'sotilgan_sana': forms.DateInput(attrs={
                'class': 'form-control',
                'id': 'sotilgan_sana',
                # You can add additional attributes if needed
            }),
        }


class MahsulotlarForm(forms.ModelForm):
    class Meta:
        model = Mahsulotlar
        fields = ['nomi', 'narxi', 'kategoriya', 'ulchov_birligi']
        widgets = {
            'nomi': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'nomi'
            }),
            'narxi': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'narxi'
            }),
            'kategoriya': forms.Select(attrs={
                'class': 'form-control', 'id': 'kategoriya'
            }),
            'ulchov_birligi': forms.Select(attrs={
                'class': 'form-control', 'id': 'ulchov_birligi'
            }),
        }



class KirimForm(forms.ModelForm):
    class Meta:
        model = Kirimlar
        fields = ['yetkazib_beruvchi', 'mahsulot', 'soni', 'narx', 'keltirilgan_sana']
        widgets = {
            'yetkazib_beruvchi': forms.Select(attrs={
                'class': 'form-control', 'id': 'yetkazib_beruvchi','name':'yetkazib_beruvchi'
            }),
            'mahsulot': forms.Select(attrs={
                'class': 'form-control', 'id': 'mahsulot','name':'mahsulot'
            }),
            'soni': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'soni','name':'soni'
            }),
            'narx': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'umumiy_narx','name':'umumiy_narx'
            }),
            'keltirilgan_sana': forms.DateInput(attrs={
                'class': 'form-control', 'id': 'keltirilgan_sana','name':'keltirilgan_sana'
            }),
        }


class KategoriyalarForm(forms.ModelForm):
    class Meta:
        model = Kategoriyalar
        fields = ['nomi']
        widgets = {
            'nomi': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'nomi'
            }),
        }
