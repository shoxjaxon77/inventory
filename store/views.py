from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Sum

from .models import Yetkazib_beruvchilar, Chiqimlar, Kategoriyalar, Mahsulotlar, Kirimlar,Omborxona
from .forms import YetkazibBeruvchilarForm,ChiqimForm,MahsulotlarForm,KirimForm,KategoriyalarForm

# Yetkazib beruvchi views
@login_required(login_url='login')
def create_yetkazib_beruvchi(request):
    form = YetkazibBeruvchilarForm()
    if request.method == 'POST':
        form = YetkazibBeruvchilarForm(request.POST)
        if form.is_valid():
            yetkazib_beruvchi = form.save(commit=False)
            yetkazib_beruvchi.user = request.user
            yetkazib_beruvchi.save()
            return redirect('yetkazib-beruvchi-list')
    context = {
        'form': form
    }
    return render(request, 'store/create_yetkazib_beruvchi.html', context)

class YetkazibBeruvchiListView(ListView):
    model = Yetkazib_beruvchilar
    template_name = 'store/yetkazib_beruvchi_list.html'
    context_object_name = 'yetkazib_beruvchilar'

# Mijoz views
@login_required(login_url='login')
def create_chiqim(request):
    form = ChiqimForm()
    if request.method == 'POST':
        form = ChiqimForm(request.POST)
        if form.is_valid():
            chiqim = form.save(commit=False)
            chiqim.user = request.user
            chiqim.save()

            mah_v= str(form.cleaned_data['mahsulot'])
            mah_chiqim = mah_v.split(' ', 1)[0]
            chiqim_obj = Chiqimlar.objects.filter(mahsulot__nomi=mah_chiqim).first()
            mahsulot = Mahsulotlar.objects.filter(nomi=mah_chiqim).first()

            if chiqim_obj and mahsulot:  
                mah_ombor = Omborxona.objects.filter(mahsulot__nomi=mah_chiqim).first()
                if mah_ombor:
                    mah_ombor.umumiy_soni -= chiqim.miqdori 
                    narx = chiqim.miqdori * mahsulot.narxi 
                    mah_ombor.umumiy_narx -= narx
                    mah_ombor.save()
            
            return redirect('chiqim-list')
    
    context = {
        'form': form
    }
    return render(request, 'store/create_chiqim.html', context)


class ChiqimListView(ListView):
   def get(self,request):
       chiqim = Chiqimlar.objects.all().order_by('-id')
       return render(request,'store/chiqim_list.html',{'chiqimlar':chiqim})

# Mahsulotlar views
@login_required(login_url='login')
def create_mahsulot(request):
    form = MahsulotlarForm()
    if request.method == 'POST':
        form = MahsulotlarForm(request.POST)
        if form.is_valid():
            mahsulot = form.save(commit=False)
            mahsulot.user = request.user 
            mahsulot.save()
            
            return redirect('mahsulot-list')

    context = {
        'form': form,
    }
    return render(request, 'store/create_mahsulot.html', context)

class MahsulotlarListView(ListView):
    model = Mahsulotlar
    template_name = 'store/mahsulot_list.html'
    context_object_name = 'mahsulotlar'

# Kirimlar views
@login_required(login_url='login')
def create_kirim(request):
    form = KirimForm()
    if request.method == 'POST':
        form = KirimForm(request.POST)
        if form.is_valid():
            kirim = form.save(commit=False)
            kirim.user = request.user
            kirim.save()
            mah_v= str(form.cleaned_data['mahsulot'])
            mah_ombor = mah_v.split(' ', 1)[0]
            kirim_mah=Kirimlar.objects.filter(mahsulot__nomi=mah_ombor)
            mahsulot=Omborxona.objects.filter(mahsulot__nomi=mah_ombor)
            b=[i for i in kirim_mah][-1]
            mak=Mahsulotlar.objects.get(nomi=mah_ombor)
            if mahsulot:
                mahsulot[0].umumiy_soni+=b.soni
                mahsulot[0].umumiy_narx+=(b.narx)*b.soni
                mahsulot[0].save()
            else:
                Omborxona.objects.create(
                    mahsulot=mak,
                    umumiy_soni=b.soni,
                    umumiy_narx=(b.narx)*b.soni+(b.narx)*b.soni
                )
            return redirect('kirim-list')

    context = {
        'form': form
    }
    return render(request, 'store/create_kirim.html', context)

class KirimlarListView(ListView):
    def get(self,request):
        kirim = Kirimlar.objects.all().order_by('-id')
        return render(request, 'store/kirim_list.html', {"kirimlar":kirim})
