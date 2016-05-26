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
from django.http.response import HttpResponse, JsonResponse


def home(request):  # view function
    # assert False, request.META['HTTP_USER_AGENT']
    # return HttpResponse("hello <b>world</b>!", status=404)
    # return HttpResponse("hello <b>world</b>!")
    # return HttpResponse("hello <b>world</b>!", content_type="text/plain")
    return JsonResponse({
        'abc': 12341324,
        'def': [4,5,6,7,7],
    })


def bar(request):
    assert False, "called bar"


urlpatterns = [
    url(r'^$', home),   # urlconf, url, route
    url(r'^foo/$', bar),
    url(r'^admin/', admin.site.urls),
]
