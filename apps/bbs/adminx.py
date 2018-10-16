import xadmin

from .models import CommentSet
from xadmin import views




class CommentSetAdmin(object):
    """评论信息"""
    list_display = ["username", "desc", "good", "add_time"]
    ordering = ["-add_time"]
    model_icon = 'fa fa-html5'
# 
xadmin.site.register(CommentSet, CommentSetAdmin)
