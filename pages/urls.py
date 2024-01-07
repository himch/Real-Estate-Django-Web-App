from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('dadi', views.about, name='dadi'),
    path('blog', views.blog, name='blog'),
    path('arenda', views.arenda, name='arenda'),
    path('buy', views.buy, name='buy'),
    path('katalogi', views.katalogi, name='katalogi'),
    path('izbrannoe', views.izbrannoe, name='izbrannoe'),
    path('sravnenie', views.sravnenie, name='sravnenie'),
]
