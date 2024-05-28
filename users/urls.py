from django.urls import path

from .views import LoginView, logout_page

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_page, name='logout'),
]
