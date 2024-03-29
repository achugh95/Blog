"""blog URL Configuration

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
from django.conf.urls import include, url       # Importing url and include function for app specific URLs
from django.views.generic import RedirectView
from blog_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url('home/', include('blog_app.urls')),     # Homepage URL for the Application
    url('^$', RedirectView.as_view(url='home/')),   # Redirecting the Server Address/IP to Home Page
    url(r'^contact/', views.contact_us, name='contact_us'),
]
