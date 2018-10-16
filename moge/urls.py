"""moge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import xadmin
from django.conf.urls import url, include
from django.views.static import serve
from moge.settings import MEDIA_ROOT
# from moge.settings import STATIC_ROOT

from zl955.views import IndexView
from vip8j888.views import IndexView
from users.views import LoginView, RegisterView, LogoutView

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^ueditor/', include('DjangoUeditor.urls')), # 富文本路径
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}), # 静态上传文件路径
    # url(r'^static/(?P<path>.*)$', serve, {"document_root": STATIC_ROOT}),
    # 
    url(r'^captcha/', include('captcha.urls')),# 验证码
    
    # url('^$', IndexView.as_view(), name='index'),
    url('^vip8j888/$', IndexView.as_view(), name='vip-index'),
    url('^zl955/$', IndexView.as_view(), name='zl-index'),
    # url('^zl955/$', IndexView.as_view(), name='index'),
    url('^reg/$', RegisterView.as_view(), name="reg"),
    url('^login/$', LoginView.as_view(), name="login"),
    url('^logout/$', LogoutView.as_view(), name="logout"),
    # url('^login/$', LoginView.as_view(), name="login"),
]
