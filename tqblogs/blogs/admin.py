
import xadmin
from xadmin import views
from blogs.models import Category, Tag, Links, InterviewQuestion,\
    Article, Comment, ReplyComment, ChickenSoup, ClickWorld, WebsiteDesc

# xadmin 配置
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True
    menu_style = 'accordion'

xadmin.site.register(views.BaseAdminView, BaseSetting)

# xadmin 配置
class GlobalSetting(object):
    site_title = "博客管理系统"
    site_footer = "黔ICP备17011880号-2"
    menu_style = "accordion"

xadmin.site.register(views.CommAdminView, GlobalSetting)

# 分类
class CategoryAdmin(object):
    list_display = ('id','category')
    ordering = ('-id',)
    list_per_page = 20

xadmin.site.register(Category, CategoryAdmin)

# 标签
class TagAdmin(object):
    list_display = ('id', 'tag')
    ordering = ('-id',)
    list_per_page = 20

xadmin.site.register(Tag, TagAdmin)

# 友情链接
class LinksAdmin(object):
    list_display = ('rank','name','url','image', 'desc')
    ordering = ('-id',)
    list_per_page = 20

xadmin.site.register(Links, LinksAdmin)

# 面试题
class InterviewQuestionAdmin(object):
    list_display = ('title','answer')
    ordering = ('-id',)
    list_per_page = 20

xadmin.site.register(InterviewQuestion, InterviewQuestionAdmin)

# 文章
class ArticleAdmin(object):
    list_display = ('title','id','author','view','like','original','category','tag')
    ordering = ('-view',)
    list_per_page = 20
    style_fields = {"context": "ueditor"}

xadmin.site.register(Article, ArticleAdmin)

# 评论
class CommentAdmin(object):
    list_display = ('name','id','email','url','article','context','head_img')
    ordering = ('-id',)
    list_per_page = 20
    style_fields = {"context": "ueditor"}

xadmin.site.register(Comment, CommentAdmin)

# 回复
class ReplyCommentAdmin(object):
    list_display = ('name','id','comment','article','head_img','context')
    ordering = ('-id',)
    list_per_page = 20
    style_fields = {"context": "ueditor"}

xadmin.site.register(ReplyComment, ReplyCommentAdmin)

# 鸡汤
class ChickenSoupAdmin(object):
    list_display = ('id','context')
    ordering = ('-id',)
    list_per_page = 50

xadmin.site.register(ChickenSoup, ChickenSoupAdmin)

# 点击词汇
class ClickWorldAdmin(object):
    list_display = ('id','world')
    ordering = ('-id',)
    list_per_page = 50

xadmin.site.register(ClickWorld, ClickWorldAdmin)

# 网站简介
class WebsiteDescAdmin(object):
    list_display = ('id','context')
    ordering = ('-id',)
    list_per_page = 50

xadmin.site.register(WebsiteDesc, WebsiteDescAdmin)





