# /usr/bin/python2
# -*- coding:utf8 -*-
from django.db import models

# Create your models here.

class Author(models.Model):
    """ 博客作者模型"""
    name=models.CharField('作者姓名',max_length=20)
    email=models.EmailField('邮箱')
    descrip=models.TextField('描述')

    def __unicode__(self):
        return u'%s' % (self.name)

class Tag(models.Model):
    """博客分类"""
    tag_name=models.CharField(max_length=20)
    create_time=models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s' % (self.tag_name)

class Blog(models.Model):
    """博客"""
    caption=models.CharField('标题',max_length=50)
    author=models.ForeignKey(Author)
    tags = models.ManyToManyField(Tag,blank=True) #多对多字段，绑定下面的Tag模型
    content = models.TextField('博客内容')  #Text长文本字段，可以写很多内容

    publish_time = models.DateTimeField('发表日期',auto_now_add=True) #日期，新增自动写入
    update_time = models.DateTimeField('修改日期',auto_now=True) #日期，修改自动更新
    recommend = models.BooleanField('是否推荐',default=False) #布尔字段，我用于标记是否是推荐博文

    def __unicode__(self):
        return u'%s %s %s' % (self.caption, self.author, self.publish_time)

    class Meta:
        #排序
        ordering=['-publish_time']

