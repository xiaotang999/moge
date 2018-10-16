from django.shortcuts import render
from django.views.generic import View
import httplib2

# Create your views here.
from .models import HtmlApp, AgentApp, HotApp, IpApp

class VIP8j888IndexView(View):
	def get(self, request):
		htmlx = HtmlApp.objects.all()
		agentx = AgentApp.objects.all()
		hotx = HotApp.objects.all()
		# 
		if 'HTTP_X_FORWARDED_FOR' in request.META:
			get_ip = request.META['HTTP_X_FORWARDED_FOR']
			get_ip = client_ip.split(",")[0]
			# 需要搭配NGINX
		else:
			get_ip = request.META.get('REMOTE_ADDR')#这里获得代理ip
		# print(request.META)

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
		return render(request, 'vip8j888/index.html',{
			'htmlx':htmlx,
			'agentx':agentx,
			'hotx':hotx
		})
