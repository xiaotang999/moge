from django.conf.urls import url, include
from django.views.static import serve
from moge.settings import MEDIA_ROOT
from moge.settings import STATIC_ROOT

from vip8j888.views import VIP8j888IndexView

urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}), # 静态上传文件路径
    url(r'^static/(?P<path>.*)$', serve, {"document_root": STATIC_ROOT}),
    url('^', VIP8j888IndexView.as_view(), name='vip-index'),
]