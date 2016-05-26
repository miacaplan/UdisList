"""udislist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.http.response import HttpResponse


def age(request, name, value):  # view function
    return HttpResponse("{}, you are {} years old.".format(name.title(), value))


urlpatterns = [
    url(r'^age/(?P<name>\w+)/(?P<value>\d+)/$', age),
    url(r'^age/(?P<value>\d+)/(?P<name>\w+)/$', age),
    url(r'^age/(?P<name>\w+)/$', age, kwargs={'value': '33'}),
    url(r'^kid/(?P<name>\w+)/$', age, kwargs={'value': '2'}),
    url(r'^admin/', admin.site.urls),
]
