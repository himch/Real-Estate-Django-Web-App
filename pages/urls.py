from django.urls import path
from django.contrib.auth.decorators import login_required

from developers.views import developer
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('dadi', views.about, name='dadi'),
    # path('blog', views.blog, name='blog'),
    path('arenda', views.arenda, name='arenda'),
    path('buy', views.buy, name='buy'),
    path('katalogi', views.katalogi, name='katalogi'),
    path('izbrannoe', login_required(views.izbrannoe), name='izbrannoe'),
    path('sravnenie', login_required(views.sravnenie), name='sravnenie'),
    path('policy', views.policy, name='policy'),
    path('otmena', views.otmena, name='otmena'),
    path('lk', login_required(views.lk), name='lk'),
    path('developer/<str:slug>/', developer, name='developer'),
    # path('article', views.article, name='article'),
    # path('arenda_single', views.arenda_single, name='arenda_single'),
]
