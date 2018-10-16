from datetime import datetime

from django.db import models
from DjangoUeditor.models import UEditorField



class HtmlApp(models.Model):
	"""代理页面"""
	name = models.CharField(max_length=250, verbose_name="网站标题", help_text="请输入小于200字符的描述！")
	icons = models.ImageField(upload_to="icons/images/", null=True, blank=True, verbose_name="favicon图标")
	keywords = models.CharField(max_length=250, verbose_name="网站关键词 - 有助于SEO推广", help_text="请输入小于200字符的描述！")
	description =  models.CharField(max_length=250, verbose_name="网站表述 - 有助于SEO推广", help_text="请输入小于200字符的描述！")
	service =  models.CharField(max_length=250, verbose_name="客服地址", help_text="请输入小于200字符的描述！")
	top = models.ImageField(upload_to="top/images/", null=True, blank=True, verbose_name="顶部图片")
	add_time = models.DateTimeField(default=datetime.now, verbose_name="更新时间")

	class Meta:
		verbose_name = '代理页面'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name

class AgentApp(models.Model):
	"""代理信息"""
	name = models.CharField(max_length=250, verbose_name="代理信息", help_text="请输入小于200字符的描述！")
	urls = models.CharField(max_length=250, verbose_name="代理地址", help_text="请输入小于200字符的描述！")
	add_time = models.DateTimeField(default=datetime.now, verbose_name="更新时间")

	class Meta:
		verbose_name = '代理信息'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name

class HotApp(models.Model):
	"""活动图片"""
	name = models.CharField(max_length=250, verbose_name="活动名称", null=True, blank=True, help_text="请输入小于200字符的描述！")
	urls = models.CharField(max_length=250, verbose_name="活动跳转地址", null=True, blank=True, help_text="请输入小于200字符的描述！")
	images = models.ImageField(upload_to="hot/images/", null=True, blank=True, verbose_name="活动图片")
	add_time = models.DateTimeField(default=datetime.now, verbose_name="更新时间")

	class Meta:
		verbose_name = '活动图片'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name

class IpApp(models.Model):
    """访问IP"""
    name = models.CharField(max_length=250, verbose_name="地址描述", null=True, blank=True, help_text="请输入小于200字符的描述！")
    ip = models.CharField(max_length=250, verbose_name="IP地址", null=True, blank=True)
    no = models.IntegerField(verbose_name="访问次数", null=True, blank=True, default=1)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="更新时间")
    
    class Meta:
        unique_together = ('ip',)
        verbose_name = '访问IP'
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return '访问IP'