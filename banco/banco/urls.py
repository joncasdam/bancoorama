"""banco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^dashboard/$', 'base.views.dashboard', name='dashboard'),
    url(r'^saque/$', 'base.views.saque', name='saque'),
    url(r'^deposito/$', 'base.views.deposito', name='deposito'),
    url(r'^extrato/$', 'base.views.extrato', name='extrato'),
    url(r'^listasaldos/$', 'base.views.listasaldos', name='listasaldos'),
    url(r'^login/$', 'base.views.login_usr', name='login_usr'),
    url(r'^logout/$', 'base.views.logout_usr', name='logout_usr'),
    url(r'^signup/$', 'base.views.signup_usr', name='signup_usr'),
    url(r'^$', 'base.views.index', name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
