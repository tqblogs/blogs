# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-05 18:47
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('original', models.CharField(choices=[('原创', '原创'), ('转载', '转载')], default='原创', max_length=10, verbose_name='是否原创')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='标题')),
                ('author', models.CharField(default='追梦者', max_length=10, verbose_name='作者')),
                ('image', models.ImageField(upload_to='images/article/', verbose_name='图片')),
                ('view', models.PositiveIntegerField(default=0, verbose_name='浏览量')),
                ('like', models.PositiveIntegerField(default=0, verbose_name='点赞数')),
                ('desc', models.TextField(verbose_name='简介')),
                ('context', DjangoUeditor.models.UEditorField(default='', verbose_name='内容')),
            ],
            options={
                'db_table': 'blogs_article',
                'verbose_name_plural': '文章',
                'verbose_name': '文章',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('category', models.CharField(max_length=30, verbose_name='分类')),
            ],
            options={
                'db_table': 'blogs_category',
                'verbose_name_plural': '分类',
                'verbose_name': '分类',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='ChickenSoup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('context', models.TextField(verbose_name='内容')),
            ],
            options={
                'db_table': 'blogs_chicken',
                'verbose_name_plural': '鸡汤',
                'verbose_name': '鸡汤',
            },
        ),
        migrations.CreateModel(
            name='ClickWorld',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('world', models.CharField(max_length=50, verbose_name='点击词汇')),
            ],
            options={
                'db_table': 'blogs_world',
                'verbose_name_plural': '点击词汇',
                'verbose_name': '点击词汇',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=50, verbose_name='昵称')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('url', models.URLField(verbose_name='网址')),
                ('head_img', models.CharField(max_length=100, verbose_name='头像')),
                ('context', DjangoUeditor.models.UEditorField(default='', verbose_name='内容')),
                ('article', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blogs.Article', verbose_name='所属文章')),
            ],
            options={
                'db_table': 'blogs_comment',
                'verbose_name_plural': '评论',
                'verbose_name': '评论',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='InterviewQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('title', models.TextField(verbose_name='题目')),
                ('answer', models.TextField(verbose_name='答案')),
            ],
            options={
                'db_table': 'blogs_interview',
                'verbose_name_plural': '面试题',
                'verbose_name': '面试题',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('rank', models.IntegerField(verbose_name='排名')),
                ('name', models.CharField(max_length=100, verbose_name='称呼')),
                ('url', models.URLField(verbose_name='链接')),
                ('image', models.CharField(max_length=100, verbose_name='头像')),
                ('desc', models.TextField(verbose_name='描述')),
            ],
            options={
                'db_table': 'blogs_link',
                'verbose_name_plural': '友情链接',
                'verbose_name': '友情链接',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='ReplyComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=50, verbose_name='昵称')),
                ('head_img', models.CharField(max_length=100, verbose_name='头像')),
                ('context', DjangoUeditor.models.UEditorField(default='', verbose_name='内容')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.Article', verbose_name='所属文章')),
                ('comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blogs.Comment', verbose_name='所属评论')),
            ],
            options={
                'db_table': 'blogs_reply',
                'verbose_name_plural': '回复',
                'verbose_name': '回复',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('tag', models.CharField(max_length=30, verbose_name='标签')),
            ],
            options={
                'db_table': 'blogs_tag',
                'verbose_name_plural': '标签',
                'verbose_name': '标签',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='WebsiteDesc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('context', models.TextField(verbose_name='网站简介')),
            ],
            options={
                'db_table': 'blogs_web_desc',
                'verbose_name_plural': '网站简介',
                'verbose_name': '网站简介',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(to='blogs.Category', verbose_name='分类'),
        ),
        migrations.AddField(
            model_name='article',
            name='interview',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.InterviewQuestion', verbose_name='面试题'),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(to='blogs.Tag', verbose_name='标签'),
        ),
    ]
