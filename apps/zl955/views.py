from django.shortcuts import render
from django.views.generic import View
#
import json 
from django.http import HttpResponse
from django.template import loader
# Create your views here.
from .models import Settings, Guanggao, OpenNew, Open, Bottoms, PiaoChuan, IpApp
from bbs.models import CommentSet
from users.models import User

class ZL955IndexView(View):
	# get
	def get(self, request):
		_settings = Settings.objects.all()
		_guanggao = Guanggao.objects.all()
		_opennew = OpenNew.objects.all()
		_open = Open.objects.order_by('-id')
		_bottoms = Bottoms.objects.all()
		_piaochuan = PiaoChuan.objects.all()
		_people = User.objects.all().count()
		_num = CommentSet.objects.all().count()
		_messages = CommentSet.objects.order_by('-id')[:5]
		# 
		if 'HTTP_X_FORWARDED_FOR' in request.META:
			get_ip = request.META['HTTP_X_FORWARDED_FOR']
			get_ip = client_ip.split(",")[0]
			# 需要搭配NGINX
		else:
			get_ip = request.META.get('REMOTE_ADDR')#这里获得代理ip
		# print(request.META)
		# 
		find_ip = IpApp.objects.filter(ip=get_ip)

		if  find_ip:
			print(get_ip+' '+'IP已经存在，增加访问次数')
			find_ip[0].no += 1
			find_ip[0].save()
		else:
			print(get_ip+' IP未存在，保存数据')
			add = IpApp()
			add.ip = get_ip
			add.save()
		return render(request, 'zl955/index.html',{
			"settings" : _settings,
			"guanggao" : _guanggao,
			"opennew" : _opennew,
			"open" : _open,
			"bottoms" : _bottoms,
			"piaochuan" : _piaochuan,
        	'people' : _people,
            'num' : _num,
			'messages':_messages,
		})
	def post(self, request):
		if request.user.is_authenticated():
			_desc = request.POST.get("desc", "")
			_open_speak = request.POST.get("open_speak", "")
			_limit_speak_no = request.POST.get("limit_speak_no", "")
			_changdu = len(_desc)
			if request.user.group.open_speak:
				if _changdu <= request.user.group.limit_speak_no:
					_bbs = CommentSet()
					_bbs.username = User.objects.get(username=request.user.username)
					_bbs.desc = _desc
					_bbs.save()
					_status = {'msg':'发表成功！','icon':'1'}
					return HttpResponse(json.dumps(_status),content_type='application/json')
				else:
					_status = {'msg':'发布失败！','icon':'5'}
					return HttpResponse(json.dumps(_status),content_type='application/json')
			else:
				_status = {'msg':'发布失败！','icon':'5'}
				return HttpResponse(json.dumps(_status),content_type='application/json')
		else:
			_status = {'msg':'发布失败！','icon':'5'}
			return HttpResponse(json.dumps(_status),content_type='application/json')

# 刷新获取新数据
class zl955NewOpen(View):
	def get(self, request):
		_opennew = OpenNew.objects.all()
		_opennew = [
			_opennew[0].no1,
			_opennew[0].no2,
			_opennew[0].no3,
			_opennew[0].no4,
			_opennew[0].no5,
			_opennew[0].no6,
			_opennew[0].no7,
			]
		return HttpResponse(json.dumps(_opennew),content_type='application/json')

class zl955Good(View):
	def post(self, request):
		if request.user.is_authenticated():
			pass
