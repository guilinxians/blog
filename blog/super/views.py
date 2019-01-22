from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from super.forms import Userlogin
from super.models import Article, Column


def login(request):
    if request.method == 'GET':
        # 插入管理员数据
        # User.objects.create_user(username='lhj', password='123456')
        return render(request, 'backweb/login.html')
    if request.method == 'POST':
        data = request.POST
        form = Userlogin(data)
        if form.is_valid():
            user = auth.authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('userpwd'))
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('super:index'))
            else:
                return render(request, 'backweb/login.html', {'msg':'用户名或者密码错误！'})
        else:
            return render(request, 'backweb/login.html', {'errors':form.errors})

@login_required
def index(request):
    if request.method == 'GET':
        arts = Article.objects.all()
        length = len(arts)
        return render(request, 'backweb/index.html', {'length':length})

@login_required
def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        return HttpResponseRedirect(reverse('super:login'))

@login_required
def article(request):
    if request.method == 'GET':
        page = request.GET.get('page', 1)
        art = Article.objects.all()
        paginator = Paginator(art, 8)
        articles = paginator.page(page)
        return render(request, 'backweb/article.html', {'articles':articles, 'page':page})

@login_required
def add_article(request):
    if request.method == 'GET':
        cols = Column.objects.all()
        return render(request, 'backweb/add-article.html', {'cols':cols})
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        tags = request.POST.get('tags')
        describe = request.POST.get('describe')
        id = request.user.id
        category = request.POST.get('category')
        Article.objects.create(title=title, content=content, tag=tags, des=describe,
                               col_id=category, user_id=id)
        return  HttpResponse('发布文章成功！')

@login_required
def category(request):
    if request.method == 'GET':
        cols = Column.objects.all()
        return render(request, 'backweb/category.html', {'cols':cols})
    if request.method == 'POST':
        name = request.POST.get('name')
        id = request.user.id
        Column.objects.create(name=name, user_id=id)
        return HttpResponse('添加成功')

@login_required
def update_category(request):
    if request.method == 'GET':
        return render(request, 'backweb/up_cat.html')
    if request.method == 'POST':
        id = request.GET.get('id')
        name = request.POST.get('name')
        column = Column.objects.filter(id=id).first()
        column.name = name
        column.save()
        return HttpResponse('栏目修改成功！')

@login_required
def del_category(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        column = Column.objects.filter(id=id).first()
        # 删除栏目下的文章
        column.article_set.all().delete()
        # 删除栏目
        Column.objects.filter(id=id).delete()
        return HttpResponse('删除栏目成功！删除该栏目下对应的文章成功！')

@login_required
def del_article(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        Article.objects.filter(id=id).first().delete()
        return HttpResponse('删除文章成功！')


@login_required
def update_article(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        art = Article.objects.filter(id=id).first()
        cols = Column.objects.all()
        return render(request, 'backweb/update-article.html', {'art':art, 'cols':cols})
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        tags = request.POST.get('tags')
        describe = request.POST.get('describe')
        category = request.POST.get('category')
        user_id = request.user.id
        art_id = request.GET.get('id')
        Article.objects.filter(id=art_id).update(title=title, content=content, tag=tags, des=describe,
                               col_id=category, user_id=user_id)
        return  HttpResponse('更新文章成功！')