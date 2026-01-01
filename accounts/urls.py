from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('registracija/', views.register, name='register'),
    path('prijava/', views.login_view, name='login'),
    path('odjava/', views.logout_view, name='logout'),
    path('nalog/', views.account, name='account'),
]


