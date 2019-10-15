"""database URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.default),
    path('newuser/',views.newuser),
    path('forgot/',views.forgot),
    path('login/',views.login),
    path('auth/',views.auth),
    path('checkbalance/',views.checkbalance),
    path('depositamt/',views.depositamt),
    path('withdrawamt/',views.withdrawamt),
    path('updatepass/',views.updatepass),
    path('logout/',views.logout),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
