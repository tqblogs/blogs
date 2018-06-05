
from django.db import models
from db.base import BaseModels
from DjangoUeditor.models import UEditorField

# 分类
class Category(BaseModels):
    category = models.CharField(max_length=30, verbose_name='分类')

    class Meta:
        db_table = 'blogs_category'
        verbose_name = '分类'
        verbose_name_plural = verbose_name
        ordering = ('-id',)

    def __str__(self):
        return self.category

# 标签
class Tag(BaseModels):
    tag = models.CharField(max_length=30, verbose_name='标签')

    class Meta:
        db_table = 'blogs_tag'
        verbose_name = '标签'
        verbose_name_plural = verbose_name
        ordering = ('-id',)

    def __str__(self):
        return self.tag

# 友情链接
class Links(BaseModels):
    rank = models.IntegerField(verbose_name='排名')
    name = models.CharField(max_length=100, verbose_name='称呼')
    url = models.URLField(verbose_name='链接')
    image = models.CharField(max_length=100, verbose_name='头像')
    desc = models.TextField(verbose_name='描述')

    class Meta:
        db_table = 'blogs_link'
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name
        ordering = ('-id', )

    def __str__(self):
        return self.name

# 面试题
class InterviewQuestion(BaseModels):
    title = models.TextField(verbose_name='题目')
    answer = models.TextField(verbose_name='答案')

    class Meta:
        db_table = 'blogs_interview'
        verbose_name = '面试题'
        verbose_name_plural = verbose_name
        ordering = ('-id',)

    def __str__(self):
        return self.title

# 文章
class Article(BaseModels):
    ORIGINAL_TYPE = {'原创': '原创','转载': '转载'}
    original = models.CharField(default='原创', max_length=10, choices=((k,v) for k,v in ORIGINAL_TYPE.items()), verbose_name='是否原创')
    title = models.CharField(max_length=100, unique=True, verbose_name='标题')
    category = models.ManyToManyField(Category, verbose_name='分类')
    tag = models.ManyToManyField(Tag, verbose_name='标签')
    author = models.CharField(default='追梦者', max_length=10, verbose_name='作者')
    image = models.ImageField(upload_to='images/article/', verbose_name='图片')
    view = models.PositiveIntegerField(default=0, verbose_name='浏览量')
    like = models.PositiveIntegerField(default=0, verbose_name='点赞数')
    desc = models.TextField(verbose_name='简介')
    interview = models.ForeignKey(InterviewQuestion, null=False, verbose_name='面试题')
    context = UEditorField(toolbars='besttome', width=880,height=600, imagePath='images/', filePath='files/',
                           default=u'', verbose_name='内容')

    class Meta:
        db_table = 'blogs_article'
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ('-id',)

    def __str__(self):
        return self.title

    def add_view(self):
        self.view += 1
        self.save(update_fields=('view',))

    def add_like(self):
        self.like += 1
        self.save(update_fields=('like',))

# 评论
class Comment(BaseModels):
    name = models.CharField(max_length=50, verbose_name='昵称')
    email = models.EmailField(verbose_name='邮箱')
    url = models.URLField(verbose_name='网址')
    article = models.ForeignKey(Article, null=True, verbose_name='所属文章')
    head_img = models.CharField(max_length=100, verbose_name='头像')
    context = UEditorField(toolbars='besttome', width=600,height=200, imagePath='images/', filePath='files/',
                           default=u'', verbose_name='内容')

    class Meta:
        db_table = 'blogs_comment'
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        ordering = ('-id',)

    def __str__(self):
        return self.name

# 回复
class ReplyComment(BaseModels):
    name = models.CharField(max_length=50, verbose_name='昵称')
    comment = models.ForeignKey(Comment, null=True, verbose_name='所属评论')
    article = models.ForeignKey(Article, verbose_name='所属文章')
    head_img = models.CharField(max_length=100, verbose_name='头像')
    context = UEditorField(toolbars='besttome', width=600,height=200, imagePath='images/', filePath='files/',
                           default=u'', verbose_name='内容')

    class Meta:
        db_table = 'blogs_reply'
        verbose_name = '回复'
        verbose_name_plural = verbose_name
        ordering = ('-id',)

    def __str__(self):
        return self.name

# 鸡汤
class ChickenSoup(BaseModels):
    context = models.TextField(verbose_name='内容')

    class Meta:
        db_table = 'blogs_chicken'
        verbose_name = '鸡汤'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.context

# 个人网站简介
class WebsiteDesc(BaseModels):
    context = models.TextField(verbose_name='网站简介')

    class Meta:
        db_table = 'blogs_web_desc'
        verbose_name = '网站简介'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.context

# 页面点击词汇
class ClickWorld(BaseModels):
    world = models.CharField(max_length=50, verbose_name='点击词汇')

    class Meta:
        db_table = 'blogs_world'
        verbose_name = '点击词汇'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.world


















