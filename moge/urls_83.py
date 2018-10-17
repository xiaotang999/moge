import xadmin
from django.conf.urls import url, include
from django.views.static import serve
from moge.settings import MEDIA_ROOT
from moge.settings import STATIC_ROOT

# from zl955.views import ZL955IndexView
# from vip8j888.views import VIP8j888IndexView
# from users.views import LoginView, RegisterView, LogoutView

urlpatterns = [
    url(r'^', xadmin.site.urls),
    url(r'^ueditor/', include('DjangoUeditor.urls')), # 富文本路径
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}), # 静态上传文件路径
    url(r'^static/(?P<path>.*)$', serve, {"document_root": STATIC_ROOT}),
]