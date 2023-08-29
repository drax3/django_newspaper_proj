from django.shortcuts import render
from django.views.generic import ListView
from . import models

# Create your views here.
class ArticleListView(ListView):
    model = models.Article
    template_name = 'article_list.html'
