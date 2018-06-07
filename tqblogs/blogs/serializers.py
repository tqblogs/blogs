
from rest_framework import serializers
from .models import Article
from tqblogs import settings

# 文章
class ArticleSerializer(serializers.ModelSerializer):

    create_time = serializers.SerializerMethodField(method_name='change_time')
    category = serializers.SerializerMethodField(method_name='change_category')
    url = serializers.SerializerMethodField(method_name='gain_article_url')
    image = serializers.SerializerMethodField(method_name='gain_article_image')
    original_url = serializers.SerializerMethodField(method_name='gain_original_url')
    category_url = serializers.SerializerMethodField(method_name='gain_category_url')

    class Meta:
        model = Article
        fields = ('id','title','create_time','url','image','original_url','category_url','original', 'view', 'like', 'category','desc')

    def change_time(self, obj):
        time = obj.create_time
        time = time.strftime('%Y年%m月%d日 %H:%M')

        return time

    def change_category(self, obj):

       for cate in obj.category.all():
           return cate.category

    def gain_article_url(self, obj):

        if settings.DEBUG:

            return 'https://'+settings.ALLOWED_HOSTS[0]+':8000/details/'+str(obj.id)
        else:
            return 'https://'+settings.ALLOWED_HOSTS[2]+'/details/'+str(obj.id)

    def gain_article_image(self, obj):

        if settings.DEBUG:
            return 'https://' + settings.ALLOWED_HOSTS[0] + ':8000/static/upload/' + str(obj.image)
        else:
            return 'https://' + settings.ALLOWED_HOSTS[2] + '/static/upload/' + str(obj.image)

    def gain_original_url(self, obj):
        if settings.DEBUG:
            return 'https://'+settings.ALLOWED_HOSTS[0]+':8000/articles/'+str(obj.original)
        else:
            return 'https://'+settings.ALLOWED_HOSTS[2]+'/articles/'+str(obj.original)

    def gain_category_url(self, obj):

        if settings.DEBUG:
            for cate in obj.category.all():
                return 'https://'+settings.ALLOWED_HOSTS[0]+':8000/articles/'+str(cate.category)
        else:
            for cate in obj.category.all():
                return 'https://'+settings.ALLOWED_HOSTS[2]+'/articles/'+str(cate.category)





