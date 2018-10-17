from django.db import models
from datetime import datetime

from users.models import User

class CommentSet(models.Model):
    """网站评论"""
    username = models.ForeignKey(User, verbose_name="会员账号")
    desc = models.CharField(max_length=250, verbose_name="评论信息", help_text="请输入小于200字符的描述！")
    good = models.IntegerField(verbose_name="点赞数量", null=True, blank=True, default=0)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="更新时间")

    class Meta:
        verbose_name = "网站评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '网站评论'
