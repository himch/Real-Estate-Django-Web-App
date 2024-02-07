from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from blog.models import Article
from our_company.models import OurCompany


class BlogHome(ListView):
    model = Article
    template_name = 'includes/content/blog.html'
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        our_company = OurCompany.objects.all().first()
        context['our_company'] = our_company
        return context


def blog(request):
    our_company = OurCompany.objects.all().first()
    blog_articles = Article.objects.all()
    paginator = Paginator(blog_articles, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'our_company': our_company,
        'page_obj': page_obj,
    }

    return render(request, 'includes/content/blog.html', context)


def blog_article(request, slug):
    article = get_object_or_404(Article, slug=slug)

    our_company = OurCompany.objects.all().first()

    blog_articles = Article.objects.all()
    blog_paginator = Paginator(blog_articles, 6)
    paged_blog_articles = blog_paginator.get_page(1)

    # # Get all realtors
    # realtors = Realtor.objects.order_by('-hire_date')
    #
    # # Get MVP
    # mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    #
    # listings = Listing.objects.order_by('-list_date').filter(is_fully_loaded=True, offer_type='sell')
    #
    # paginator = Paginator(listings, 6)
    # page = request.GET.get('page')
    # paged_listings = paginator.get_page(page)

    context = {
        'our_company': our_company,
        'article': article,
        'blog_articles': paged_blog_articles,
        # 'listings': paged_listings,
        # 'realtors': realtors,
        # 'mvp_realtors': mvp_realtors
    }

    return render(request, 'includes/content/article.html', context)