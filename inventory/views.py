from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from store.models import Mahsulotlar, Yetkazib_beruvchilar, Chiqimlar, Omborxona,Kirimlar

@login_required(login_url='login')
def dashboard(request):
   
    mal=Omborxona.objects.all()
    total_quantity = Omborxona.objects.aggregate(total_quantity=Sum('umumiy_soni'))['total_quantity']
    kirim = Kirimlar.objects.count()
    chiqim = Chiqimlar.objects.count()
    y_b = Yetkazib_beruvchilar.objects.count()

    context = {
        'total':total_quantity,
        'mahsulot': mal,
        'kirim': kirim,
        'chiqim': chiqim,
        'yetkazib_beruvchilar': y_b,
    }
    return render(request, 'dashboard.html', context)
