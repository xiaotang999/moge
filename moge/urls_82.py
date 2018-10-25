from django.conf.urls import url, include
from django.views.static import serve
from moge.settings import MEDIA_ROOT
from moge.settings import STATIC_ROOT

from zl955.views import ZL955IndexView, zl955NewOpen, zl955Good, zl955GetNew, zl955GetBBS
from users.views import LoginView, RegisterView, LogoutView, UploadImageView
from bbs.views import CommentSetView

urlpatterns = [
    url('^$', ZL955IndexView.as_view(), name='zl-index'),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}), # 静态上传文件路径
    url(r'^static/(?P<path>.*)$', serve, {"document_root": STATIC_ROOT}),
    # 
    url(r'^captcha/', include('captcha.urls')),# 验证码
    # 
    url('^reg/$', RegisterView.as_view(), name="reg"),
    url('^login/$', LoginView.as_view(), name="login"),
    url('^logout/$', LogoutView.as_view(), name="logout"),
    # 
    url('^bbs/', CommentSetView.as_view(), name="bbs"),
    url('^newopen/', zl955NewOpen.as_view(), name='zl-newopen'),
    url('^good/', zl955Good.as_view(), name='zl-good'),
    url('^getbbs/', zl955GetBBS.as_view(), name='zl-getbbs'),
    url('^getnew/', zl955GetNew.as_view(), name='zl-getnew'),
    url(r'^image/upload/$', UploadImageView.as_view(), name="image_upload"),
]

