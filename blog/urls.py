from django.urls import path

from .views import BlogHome, blog, blog_article

urlpatterns = [
    # path('', blog, name='blog'),
    path('', BlogHome.as_view(), name='blog'),
    path('<slug:slug>/', blog_article, name='article'),
]