from django.shortcuts import render
from django.views.generic import View
#
import json 
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core import serializers
# Create your views here.
from .models import Settings, Guanggao, OpenAutoOne, OpenNew, Open, Bottoms, PiaoChuan, IpApp
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
		"""发布评论"""
		if request.user.is_authenticated():
			_desc = request.POST.get("desc", "")
			_open_speak = request.POST.get("open_speak", "")
			_limit_speak_no = request.POST.get("limit_speak_no", "")
			_changdu = len(_desc)
			if _desc != '':
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
				_status = {'msg':'不允许提交空评论','icon':'5'}
				return HttpResponse(json.dumps(_status),content_type='application/json')
		else:
			_status = {'msg':'发布失败！','icon':'5'}
			return HttpResponse(json.dumps(_status),content_type='application/json')

class zl955NewOpen(View):
	"""刷新获取开奖新数据"""
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
	"""点赞功能只向上叠加"""
	def get(self, request):
		_id = request.GET.get("id", "")
		_bbs = CommentSet.objects.get(id=_id)
		_bbs.good += 1
		_bbs.save()
		_status = {'status':'ok','num':_bbs.good}
		return HttpResponse(json.dumps(_status),content_type='application/json')


class zl955GetBBS(View):
	"""
	获取BBS前5条记录
	"""
	def get(self, request):
		_bbs_5s = CommentSet.objects.order_by('-id')[:5]
		_bbs_5= json.loads(serializers.serialize("json", _bbs_5s))
		for z in _bbs_5:
			zs = User.objects.get(id=z['fields']['username'])
			_avatar = zs.avatar
			_nickname = zs.nickname
			z['fields']['avatar'] = str(_avatar)
			z['fields']['nickname'] = str(_nickname)

		return HttpResponse(json.dumps(_bbs_5),content_type='application/json')


class zl955GetNew(View):
	"""获取品论新数据"""
	def get(self, request):
		_pages = request.GET.get("pages", "")
		p = int(_pages)
		_s = p*5
		_e = 5*(p+1)
		data = {}
		book = CommentSet.objects.order_by('-id')[_s:_e]
		data['list'] = json.loads(serializers.serialize("json", book))
		n = 0
		for i in data['list']:
			info = User.objects.get(id=i['fields']['username'])
			_avatar = info.avatar
			_nickname = info.nickname
			i['fields']['avatar'] = str(_avatar)
			i['fields']['nickname'] = str(_nickname)
			n+=1
		return HttpResponse(json.dumps(data),content_type='application/json')


class zl955getSixOne(View):
	"""获取六合彩"""
	def get(self, request):
		check_token = "kdsjfhsh29*/djk.*3dsa.1x1as"
		_status = {}
		# 
		token = request.GET.get("token")
		expect = request.GET.get("expect")
		no1 = request.GET.get("no1")
		no2 = request.GET.get("no2")
		no3 = request.GET.get("no3")
		no4 = request.GET.get("no4")
		no5 = request.GET.get("no5")
		no6 = request.GET.get("no6")
		no7 = request.GET.get("no7")
		old_expect = OpenAutoOne.objects.order_by('-id')[:1]
		info = json.loads(serializers.serialize("json", old_expect))
		if token == check_token:
			print("token正确")
			if not info or expect != info[0]['fields']['expect']:
				print("期号不存在，写入数据库")
				up = OpenAutoOne()
				up.expect = expect
				up.no1 = no1
				up.no2 = no2
				up.no3 = no3
				up.no4 = no4
				up.no5 = no5
				up.no6 = no6
				up.no7 = no7
				if no7:
					up.is_open = True
				up.save()
			else: # 更新操作
				if not info[0]['fields']['is_open']: # 判断是否开完？
					print("期号存在，未全部开完，继续写入")
					find_expect = OpenAutoOne.objects.get(expect=expect)
					# updates = json.loads(serializers.serialize("json", find_expect))
					find_expect.no1 = no1
					find_expect.no2 = no2
					find_expect.no3 = no3
					find_expect.no4 = no4
					find_expect.no5 = no5
					find_expect.no6 = no6
					find_expect.no7 = no7
					if no7:
						find_expect.is_open = True
					find_expect.save()
		return HttpResponse(json.dumps(_status),content_type='application/json')
		
		