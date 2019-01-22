from django.contrib.auth.models import User
from django.db import models



class Column(models.Model):
    """栏目"""
    name = models.CharField(max_length=20, null=True, unique=True)   # 栏目名
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'column'


class Article(models.Model):
    """文章"""
    title = models.CharField(max_length=100, null=True, unique=True)   # 标题
    content = models.CharField(max_length=20000, null=True)   # 内容
    image = models.ImageField(upload_to='img')    # 图片
    tag = models.CharField(max_length=20)    # 标签
    des = models.CharField(max_length=50)    # 描述
    create_date = models.DateTimeField(auto_now_add=True)   # 创建时间
    col = models.ForeignKey(Column, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'article'


