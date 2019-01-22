from django.core.paginator import Paginator
from django.shortcuts import render

from super.models import Column, Article


def about(request):
    if request.method == 'GET':
        columns = Column.objects.all()
        return render(request, 'web/about.html', {'columns':columns})

def gbook(request):
    if request.method == 'GET':
        columns = Column.objects.all()
        return render(request, 'web/gbook.html', {'columns':columns})

def index(request):
    if request.method == 'GET':
        columns = Column.objects.all()
        return render(request, 'web/index.html', {'columns':columns})

def info(request):
    if request.method == 'GET':
        id = request.GET.get('id', 3)
        art = Article.objects.filter(id=id).first()
        columns = Column.objects.all()

        return render(request, 'web/info.html', {'art':art, 'columns':columns})

def infopic(request):
    if request.method == 'GET':
        columns = Column.objects.all()
        return render(request, 'web/infopic.html', {'columns':columns})

def list(request):
    if request.method == 'GET':
        columns = Column.objects.all()
        articles = Article.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(articles, 8)
        arts = paginator.page(page)
        return render(request, 'web/list.html', {'columns':columns, 'arts':arts})

def column(request):
    if request.method == 'GET':
        id = request.GET.get('id', 3)
        arts = Article.objects.filter(col_id=id)
        columns = Column.objects.all()
        return render(request, 'web/column.html', {'arts':arts, 'columns':columns})

