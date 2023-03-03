"""connect_plus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from connectes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('buttons/', views.buttons, name='buttons'),
    path('dropdowns/', views.dropdowns, name='dropdowns'),
    path('typography/', views.typography, name='typography'),
    path('mdi/', views.mdi, name='mdi'),
    path('basic_elements/', views.basic_elements, name='basic_elements'),
    path('basic_table/', views.basic_table, name='basic_table'),
    path('error_404s/', views.error_404s, name='error_404s'),
    path('error_500s/', views.error_500s, name='error_500s'),
    path('blank_page/', views.blank_page, name='blank_page'),
    path('chartjs/', views.chartjs, name='chartjs'),
    path('documentation/', views.documentation, name='documentation'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register')
]
