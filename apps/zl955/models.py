from django.db import models
from datetime import datetime
from DjangoUeditor.models import UEditorField

# Create your models here.

class Settings(models.Model):
    """网站设置"""
    name = models.CharField(max_length=250, verbose_name="网站标题", help_text="请输入小于200字符的描述！")
    keywords = models.CharField(max_length=250, verbose_name="SEO-网站关键词", help_text="请输入小于200字符的描述！")
    description =  models.CharField(max_length=250, verbose_name="SEO-网站介绍词", help_text="请输入小于200字符的描述！")
    icons = models.ImageField(upload_to="zl955/setting/", null=True, blank=True, verbose_name="favicon图标")
    logo_pic = models.ImageField(upload_to="zl955/setting/", null=True, blank=True, verbose_name="网站标题图片")
    water_pic = models.ImageField(upload_to="zl955/setting/", null=True, blank=True, verbose_name="水印背景图片")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="更新时间")

    class Meta:
        verbose_name = "网站设置"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Guanggao(models.Model):
    """广告设置 """
    name = models.CharField(max_length=250, verbose_name="广告名字", help_text="请输入小于200字符的描述！")
    image = models.ImageField(upload_to="zl955/abb/", null=True, blank=True, verbose_name="广告图片")
    href = models.CharField(max_length=250, verbose_name="广告链接", help_text="请输入小于200字符的描述！")
    is_show = models.BooleanField(choices=((True,u'显示'),(False,u'不显示')),max_length=2,verbose_name=u'是否显示', default=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="更新时间")
    
    class Meta:
        verbose_name = "广告设置"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class OpenAutoOne(models.Model):
    """自动开奖一"""
    expect = models.CharField(max_length=55, verbose_name="期号", help_text="请输入小于50字符的描述！")
    no1 = models.CharField(max_length=55, verbose_name="第1位", null=True, blank=True, help_text="请输第1位号码！", default='0')
    no2 = models.CharField(max_length=55, verbose_name="第2位", null=True, blank=True, help_text="请输第2位号码！", default='0')
    no3 = models.CharField(max_length=55, verbose_name="第3位", null=True, blank=True, help_text="请输第3位号码！", default='0')
    no4 = models.CharField(max_length=55, verbose_name="第4位", null=True, blank=True, help_text="请输第4位号码！", default='0')
    no5 = models.CharField(max_length=55, verbose_name="第5位", null=True, blank=True, help_text="请输第5位号码！", default='0')
    no6 = models.CharField(max_length=55, verbose_name="第6位", null=True, blank=True, help_text="请输第6位号码！", default='0')
    no7 = models.CharField(max_length=55, verbose_name="第7位", null=True, blank=True, help_text="请输第7位号码！", default='0')
    is_open = models.BooleanField(choices=((True,u'已开'),(False,u'未开')),max_length=2,verbose_name=u'是否开完', default=False)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="更新时间")

    class Meta:
        verbose_name = "自动开奖一"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.expect

class OpenNew(models.Model):
    """最新开奖"""
    issue = models.CharField(max_length=55, verbose_name="开奖期号", help_text="请输入小于50字符的描述！")
    no1 = models.CharField(max_length=55, verbose_name="第1位", null=True, blank=True, help_text="请输第1位号码！", default='0')
    no2 = models.CharField(max_length=55, verbose_name="第2位", null=True, blank=True, help_text="请输第2位号码！", default='0')
    no3 = models.CharField(max_length=55, verbose_name="第3位", null=True, blank=True, help_text="请输第3位号码！", default='0')
    no4 = models.CharField(max_length=55, verbose_name="第4位", null=True, blank=True, help_text="请输第4位号码！", default='0')
    no5 = models.CharField(max_length=55, verbose_name="第5位", null=True, blank=True, help_text="请输第5位号码！", default='0')
    no6 = models.CharField(max_length=55, verbose_name="第6位", null=True, blank=True, help_text="请输第6位号码！", default='0')
    no7 = models.CharField(max_length=55, verbose_name="第7位", null=True, blank=True, help_text="请输第7位号码！", default='0')
    desc = UEditorField(verbose_name=u"详细信息",width=900, height=300, imagePath="zl955/ueditor/opennew/", filePath="ueditor/", default='')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="更新时间")

    class Meta:
        verbose_name = "最新开奖"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.issue

class Open(models.Model):
    """新增开奖"""
    issue = models.CharField(max_length=55, verbose_name="期号", help_text="请输入小于50字符的描述！")
    top = models.CharField(max_length=250, verbose_name="开头文字简述", help_text="请输入小于200字符的描述！")
    desc = UEditorField(verbose_name=u"详细信息",width=900, height=300, imagePath="zl955/ueditor/open/", filePath="ueditor/", default='')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="更新时间")

    class Meta:
        verbose_name = "新增开奖"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.issue

class Bottoms(models.Model):
    """底部信息 """
    name = models.CharField(max_length=250, verbose_name="底部信息", help_text="请输入小于200字符的描述！")
    desc = UEditorField(verbose_name=u"细节",width=900, height=300, imagePath="zl955/ueditor/bottoms/", filePath="ueditor/", default='')
    explain = models.CharField(max_length=250, verbose_name="网站声明", help_text="请输入小于200字符的描述！")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="更新时间")

    class Meta:
        verbose_name = "底部信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class PiaoChuan(models.Model):
    """左右飘窗"""
    name = models.CharField(max_length=250, verbose_name="左右飘窗", help_text="请输入小于200字符的描述！")  
    leftt = models.ImageField(upload_to="zl955/float/", null=True, blank=True, verbose_name="左飘窗")
    leftt_herf = models.CharField(max_length=250, verbose_name="左飘窗链接", help_text="请输入小于200字符的描述！")
    rightt = models.ImageField(upload_to="zl955/float/", null=True, blank=True, verbose_name="右飘窗")
    rightt_herf = models.CharField(max_length=250, verbose_name="右飘窗链接", help_text="请输入小于200字符的描述！")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="更新时间")

    class Meta:
        verbose_name = "左右飘窗"
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
		

      

