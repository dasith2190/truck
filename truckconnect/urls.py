"""truckconnect URL Configuration

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
from order.views import *
from order.edit_views import *
from order.models import *
from order.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.conf.urls import include


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^accounts/register/$', GenericCreate.as_view(
            template_name='generic/generic_create.html',
            form_class=UserCreationForm,
            success_url='/'
    ), name='register'),
    url(r'^bid/create/(?P<pk>[0-9]+)/$', bid_create, name='bid_create'),

    url('^order/create/$', login_required(GenericCreate.as_view(template_name = 'generic/generic_create.html',
                                                                model=Order, form_class=OrderForm)), name='order_create'),
    url('^order/list/$', login_required(GenericList.as_view(template_name = 'order_list.html', model=Order)), name='order_list'),
    url('^order/detail/(?P<pk>[0-9]+)/$', (GenericDetail.as_view(template_name = 'order_detail.html', model=Order)), name='order_detail'),

    url('^bid/list/$', login_required(GenericList.as_view(template_name = 'bid_list.html', model=Bids)), name='bid_list'),

]
