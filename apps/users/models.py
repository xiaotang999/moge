from django.db import models
from datetime import datetime

from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserSetting(models.Model):
    """会员组别-发言数等"""
    name = models.CharField(max_length=250, verbose_name="会员组名", help_text="请输入小于200字符的描述！")
    limit_speak_no = models.IntegerField(verbose_name="限制字数", null=True, blank=True, default=100)
    open_speak = models.BooleanField(choices=((True,u'激活'),(False,u'未激活')),max_length=2,verbose_name=u'是否激活', help_text='激活后使用发言等功能', default=False)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="更新时间")

    class Meta:
        verbose_name = "会员组别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
        
# 获取默认值
def get_group_default():
    return UserSetting.objects.get(id=1)

class User(AbstractUser):
    """本站会员"""
    group = models.ForeignKey(UserSetting, null=True, blank=True, verbose_name="会员组", default=get_group_default)
    # name = models.CharField(max_length=25, verbose_name="会员昵称", help_text="请输入小于20字符的描述！")
    avatar = models.ImageField(upload_to="users/avatar/%Y/%m", null=True, blank=True, default=u"users/avatar/default.png", max_length=100)
    ip = models.CharField(max_length=100, null=True, blank=True, verbose_name="注册IP")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="更新时间")

    class Meta:
        verbose_name = "本站会员"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


