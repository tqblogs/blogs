
import re
import random
from django.views import View
from rest_framework.views import APIView
from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from blogs.models import Article, Category, Tag, Links, ChickenSoup, ClickWorld
from blogs.serializers import ArticleSerializer

from tqblogs import settings

categorys = Category.objects.all()
link = Links.objects.all().order_by('-rank')
carousel = Article.objects.all().order_by('-like')
carousel_first = Article.objects.all().order_by('create_time')
chicken = ChickenSoup.objects.all()
world = ClickWorld.objects.all()


class LimitDatePager(LimitOffsetPagination):
    max_limit = 20
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    default_limit = 6
    template = None

class NumberDatePager(PageNumberPagination):

    page_size = 6
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 1000
    template = None

# 首页
class IndexView(APIView):

    def get(self, request):
        article = Article.objects.all().order_by('-view')
        chicken_id_list = []
        for c in chicken:
            chicken_id_list.append(c.id)
        chicken_soup = ChickenSoup.objects.get(id=random.choice(chicken_id_list))

        context = {
            'article':article[:6],
            'category':categorys,
            'links':link,
            'carousel':carousel[:5],
            'carousel_first':carousel_first[:1],
            'chicken_soup':chicken_soup,
            'world':world
        }

        return render(request, 'blogs/index.html', context)

    def post(self, request):

        article = Article.objects.all().order_by('-view')
        pager = LimitDatePager()
        pager_list = pager.paginate_queryset(queryset=article, request=request, view=self)
        serializer = ArticleSerializer(instance=pager_list, many=True)

        return JsonResponse({'code':200, 'data':serializer.data})

# 列表页
class ListView(APIView):

    def get(self, request, category):

        if category == '原创':
            article = Article.objects.filter(original=category)
            type = category
        elif category == '转载':
            article = Article.objects.filter(original=category)
            type = category
        else:
            cate = Category.objects.get(category=category)
            article = Article.objects.filter(category__article__category=cate.id)
            type = cate.category

        chicken_id_list = []
        for c in chicken:
            chicken_id_list.append(c.id)
        chicken_soup = ChickenSoup.objects.get(id=random.choice(chicken_id_list))

        context = {
            'articles':article[:6],
            'type':type,
            'category': categorys,
            'links': link,
            'carousel': carousel[:5],
            'carousel_first': carousel_first[:1],
            'chicken_soup': chicken_soup,
            'world': world
        }

        return render(request, 'blogs/article.html', context)

    def post(self, request, category):

        if category == '原创':
            article = Article.objects.filter(original=category)

        elif category == '转载':
            article = Article.objects.filter(original=category)
        else:

            cate = Category.objects.get(category=category)
            article = Article.objects.filter(category__article=cate.id)

        pager = NumberDatePager()
        pager_list = pager.paginate_queryset(queryset=article, request=request, view=self)
        serializer = ArticleSerializer(instance=pager_list, many=True)

        try:
            if not pager.page.next_page_number():
                return JsonResponse({'code': 404})
            else:
                return JsonResponse({'code': 200, 'data': serializer.data})

        except Exception as e:
            return JsonResponse({'code': 200, 'data': serializer.data})
            # return JsonResponse({'code': 404})


# 详情页
class DetailView(APIView):

    def get(self, request, id):
        blogs = Article.objects.get(id=id)
        blogs.add_view()

        html = re.compile(r'</?\w+[^>]*>', re.S)
        text = html.sub('', blogs.context)
        text = str(text).replace('&nbsp;', '').replace('&quot;', '').replace('&#39', '').replace(' ', '')
        number = len(text)
        minute = str(int(number)/900)

        chicken_id_list = []
        for c in chicken:
            chicken_id_list.append(c.id)
        chicken_soup = ChickenSoup.objects.get(id=random.choice(chicken_id_list))

        try:
            previous = Article.objects.get(id=int(id)-1)
        except Exception as e:
            previous = 0
        try:
            next = Article.objects.get(id=int(id)+1)
        except Exception as e:
            next = 0

        context = {
            'blogs':blogs,
            'category': categorys,
            'links': link,
            'carousel': carousel[:5],
            'carousel_first': carousel_first[:1],
            'chicken_soup': chicken_soup,
            'number':number,
            'minute':minute[:4],
            'previous':previous,
            'next':next,
            'world': world
        }
        session_id = request.COOKIES.get(settings.SESSION_COOKIE_NAME, None)
        request.session['session_id'] = session_id

        return render(request, 'blogs/detail.html', context)

    def post(self, request,id):

        blogs_id = request.POST.get('blogs_id')
        session_id = request.COOKIES.get(settings.SESSION_COOKIE_NAME, None)
        
        if request.session.get('session_blogs_id_'+blogs_id, None):
            return JsonResponse({'code':201})
        
        request.session['session_blogs_id_'+blogs_id] = session_id + '_'+blogs_id
        blogs = Article.objects.get(id=blogs_id)
        blogs.add_like()

        return JsonResponse({'code':200,'like':blogs.like})

@csrf_exempt
def page_not_found(request):
    return render_to_response('404.html')

@csrf_exempt
def page_error(request):
    return render_to_response('500.html')





