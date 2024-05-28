from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from store.models import Mahsulotlar, Yetkazib_beruvchilar, Chiqimlar, Omborxona,Kirimlar

@login_required(login_url='login')
def dashboard(request):
   
    mal=Omborxona.objects.all()

    kirim = Kirimlar.objects.count()
    chiqim = Chiqimlar.objects.count()
    y_b = Yetkazib_beruvchilar.objects.count()
    # for i in mal:
    #     print(i)
    context = {
        'mahsulot': mal,
        'kirim': kirim,
        'chiqim': chiqim,
        'yetkazib_beruvchilar': y_b,
    }
    return render(request, 'dashboard.html', context)
