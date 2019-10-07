"""power_monitor URL Configuration

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
from django.urls import re_path, path

from .views.main_power import MainPowerView
from .views.out_pin import OutPinView
from .views.test import exception_view

app_name = 'panel'
urlpatterns = [
    re_path(r'^out-pin/(\w*)$', OutPinView.as_view()),
    re_path(r'^main-power/(\w*)$', MainPowerView.as_view()),
    path('exception/', exception_view),
]
