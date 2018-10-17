from django.shortcuts import render
from django.views.generic import View
#
import json 
from django.http import HttpResponse
from django.template import loader
# Create your views here.
from .models import Settings, Guanggao, OpenNew, Open, Bottoms, PiaoChuan, IpApp
from bbs.models import CommentSet

class ZL955IndexView(View):
	def post(self, request):
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

	def get(self, request):
		_settings = Settings.objects.all()
		_guanggao = Guanggao.objects.all()
		_opennew = OpenNew.objects.all()
		_open = Open.objects.order_by('-id')
		_bottoms = Bottoms.objects.all()
		_piaochuan = PiaoChuan.objects.all()
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
		})

# 
class ZL955TestView(View):
	def post(self, request):
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

	def get(self, request):
		_settings = Settings.objects.all()
		_guanggao = Guanggao.objects.all()
		_opennew = OpenNew.objects.all()
		_open = Open.objects.order_by('-id')
		_bottoms = Bottoms.objects.all()
		_piaochuan = PiaoChuan.objects.all()
		_messages = CommentSet.objects.order_by('-add_time')
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
		return render(request, 'zl955/test.html',{
			"settings" : _settings,
			"guanggao" : _guanggao,
			"opennew" : _opennew,
			"open" : _open,
			"bottoms" : _bottoms,
			"piaochuan" : _piaochuan,
			"_messages" : _messages,
		})