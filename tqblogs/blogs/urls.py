
from django.conf.urls import url
from blogs import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^categorys/([\u4e00-\u9fa5_a-zA-Z0-9]+)/$', views.ListView.as_view(), name='article'),
    url(r'^details/(\d+)/$', views.DetailView.as_view(), name='detail'),
]
