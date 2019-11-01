"""mechanic_user URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from mechanic_assign.views import *
from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="index"),
    url(r'^signup_login$', signup_login, name="signup_login"),
    url(r'^logout$', logout_view, name="logout"),
    url(r'^services$', service, name="services"),
    url(r'^contact$', contact, name="contact"),
    url(r'^user_profile$',user_profile, name="user_profile"),
    url(r'^user_edit$',user_edit,name="user_edit"),
    url(r'^dashboard', dashboard, name="dashboard"),
    url(r'^user_employee$', user_employee, name="user_employee"),
    url(r"^booking_view/(?P<id>\d+)", booking_view, name="booking_view"),
    path(r"^upload_images/(?P<id>\d+)", upload_image, name="upload_image"),
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)