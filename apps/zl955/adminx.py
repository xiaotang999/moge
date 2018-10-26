# -*- coding: utf-8 -*-
import xadmin

from .models import Settings, Guanggao, OpenAutoOne, OpenNew, Open, Bottoms, PiaoChuan, IpApp
from xadmin import views
from xadmin.views import ListAdminView

class GlobalSetting(object):
    """后台全局设置"""
    site_title = "网站管理"
    site_footer = "网站管理"
    menu_style = 'accordion'

class SettingsAdmin(object):
    """网站设置"""
    list_display = ["name", "add_time"]
    ordering = ["name"]
    model_icon = 'fa fa-html5'
class GuanggaoAdmin(object):
    """广告设置"""
    list_display = ["name", "href", "is_show", "add_time"]
    ordering = ["id"]
    list_editable = ["is_show"]
    model_icon = 'fa fa-html5'
class OpenAutoOneAdmin(object):
    """自动开奖一"""
    list_display = ["expect", "no1", "no2", "no3", "no4", "no5", "no6", "no7", "is_open", "add_time"]
    list_editable = ('no1', 'no2', 'no3', 'no4', 'no5', 'no6', 'no7')
    ordering = ["-id"]
    model_icon = 'fa fa-html5'
class OpenNewAdmin(object):
    """最新开奖"""
    list_display = ["issue", "no1", "no2", "no3", "no4", "no5", "no6", "no7", "add_time"]
    list_editable = ('no1', 'no2', 'no3', 'no4', 'no5', 'no6', 'no7')
    ordering = ["issue"]
    style_fields = {"desc": "ueditor"}
    model_icon = 'fa fa-html5'
class OpenAdmin(object):
    """开奖"""
    list_display = ["issue", "add_time"]
    ordering = ["-id"]
    style_fields = {"desc": "ueditor"}
    model_icon = 'fa fa-html5'
class BottomsAdmin(object):
    """底部信息"""
    list_display = ["name", "add_time"]
    ordering = ["name"]
    style_fields = {"desc": "ueditor"}
    model_icon = 'fa fa-html5'
class PiaoChuanAdmin(object):
    """左右飘窗"""
    list_display = ["name", "add_time"]
    ordering = ["name"]
    model_icon = 'fa fa-html5'
class IpAppAdmin(object):
    """访问IP"""
    list_display = ["name", "no", "ip", "add_time"]
    list_display_links = ("id")
    list_editable = "name"
    ordering = ["-add_time"]
    model_icon = 'fa fa-html5'
    get_add = ['ip']
    # data_charts = {
    #     "zl955-ip": {
    #         'title': "用户访问量", 
    #         "x-field": "add_time", 
    #         "y-field": ("no"),
    #         "order": ('add_time',)
    #     }
    # }

# 
xadmin.site.register(views.CommAdminView, GlobalSetting)
# 
xadmin.site.register(Settings, SettingsAdmin)
xadmin.site.register(Guanggao, GuanggaoAdmin)
xadmin.site.register(OpenAutoOne, OpenAutoOneAdmin)
xadmin.site.register(OpenNew, OpenNewAdmin)
xadmin.site.register(Open, OpenAdmin)
xadmin.site.register(Bottoms, BottomsAdmin)
xadmin.site.register(PiaoChuan, PiaoChuanAdmin)
xadmin.site.register(IpApp, IpAppAdmin)
