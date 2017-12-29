# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85\xe5\xa7\x93\xe5\x90\x8d')),
                ('email', models.EmailField(max_length=254, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1')),
                ('descrip', models.TextField(verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('caption', models.CharField(max_length=50, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('content', models.TextField(verbose_name=b'\xe5\x8d\x9a\xe5\xae\xa2\xe5\x86\x85\xe5\xae\xb9')),
                ('publish_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x8f\x91\xe8\xa1\xa8\xe6\x97\xa5\xe6\x9c\x9f')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xa5\xe6\x9c\x9f')),
                ('recommend', models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x8e\xa8\xe8\x8d\x90')),
                ('author', models.ForeignKey(to='blog.Author')),
            ],
            options={
                'ordering': ['-publish_time'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag_name', models.CharField(max_length=20)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag', blank=True),
        ),
    ]
