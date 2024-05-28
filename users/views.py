from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import LoginForm
from django.contrib.auth.forms import AuthenticationForm


def login_page(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            
            if user:
                login(request, user)
                return redirect('dashboard')
    context = {'form': forms}
    return render(request, 'users/login.html', context)


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "users/login.html", {'form':form})

    def post(self, request):
        check = AuthenticationForm(data=request.POST)

        if check.is_valid():
            user = check.get_user()
            login(request, user)
            return redirect('dashboard')
        else:
            return redirect('login')

def logout_page(request):
    logout(request)
    return redirect('login')
