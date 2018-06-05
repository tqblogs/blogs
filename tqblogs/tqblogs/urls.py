
from django.conf.urls import url, include
from django.contrib import admin
from . import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

import DjangoUeditor
import xadmin
from xadmin.plugins import xversion

from blogs import views

xadmin.autodiscover()
xversion.register_models()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', include(xadmin.site.urls)),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico')),
    url(r'^ueditor/', include('DjangoUeditor.urls', namespace='ueditor')),
    url(r'^search/', include('haystack.urls', namespace='haystack')),
    url(r'^', include('blogs.urls', namespace='blogs')),
]

handler404 = views.page_not_found
handler500 = views.page_error

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
