from django.conf.urls import url, include
from django.views.static import serve
from moge.settings import MEDIA_ROOT
from moge.settings import STATIC_ROOT

from zl955.views import ZL955IndexView
from users.views import LoginView, RegisterView, LogoutView

urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}), # 静态上传文件路径
    url(r'^static/(?P<path>.*)$', serve, {"document_root": STATIC_ROOT}),
    # 
    url(r'^captcha/', include('captcha.urls')),# 验证码
    # 
    url('^reg/$', RegisterView.as_view(), name="reg"),
    url('^login/$', LoginView.as_view(), name="login"),
    url('^logout/$', LogoutView.as_view(), name="logout"),

    url('^$', ZL955IndexView.as_view(), name='zl-index'),
]