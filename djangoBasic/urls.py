"""djangoBasic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from djangoBasic import views as views_basic
from posts import views as views_post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_basic.hello_world),
    path('hi/', views_basic.hi),
    path('h/<str:name>/<int:age>/', views_basic.ages),
    path('hpost/', views_post.proof),
]

