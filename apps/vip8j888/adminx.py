# -*- coding: utf-8 -*-

import xadmin

from .models import HtmlApp, AgentApp, HotApp, IpApp


class HtmlAdmin(object):
     list_display = ["name", "add_time"]
     ordering = ["name"]
     model_icon = 'fa fa-html5'
class AgentAdmin(object):
     list_display = ["id", "name", "urls", "add_time"]
     ordering = ["id"]
     model_icon = 'fa fa-location-arrow'
class HotAdmin(object):
     list_display = ["id", "name", "add_time"]
     ordering = ["id"]
     model_icon = 'fa fa-fire'
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

xadmin.site.register(HtmlApp, HtmlAdmin)
xadmin.site.register(AgentApp, AgentAdmin)
xadmin.site.register(HotApp, HotAdmin)
xadmin.site.register(IpApp, IpAppAdmin)
