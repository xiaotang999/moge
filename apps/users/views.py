# _*_ encoding:utf-8 _*_
import  json

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, HttpResponseRedirect
# from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse

from captcha.models import CaptchaStore  
from captcha.helpers import captcha_image_url  


from .models import User
from .forms import LoginForm, RegisterForm, CheckCode, UploadImageForm
# from .forms import UserInfoForm
# from utils.email_send import send_register_email
from utils.mixin_utils import LoginRequiredMixin


# from .models import Banner

# 继承原始的会员登陆方式
class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None

# class AciveUserView(View):
#     def get(self, request, active_code):
#         all_records = EmailVerifyRecord.objects.filter(code=active_code)
#         if all_records:
#             for record in all_records:
#                 email = record.email
#                 user = User.objects.get(email=email)
#                 user.is_active = True
#                 user.save()
#         else:
#             return render(request, "active_fail.html")
#         return render(request, "login.html")

# 



class RegisterView(View):
    """用户注册"""
    def get(self, request):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse("zl-index"))
        else:
            hashkey = CaptchaStore.generate_key()
            imgage_url = captcha_image_url(hashkey)
            return render(request, "zl955/reg.html", {'hashkey':hashkey,'imgage_url':imgage_url})
    def post(self, request):
        register_form = RegisterForm(request.POST)
        check_code = CheckCode(request.POST)
        if check_code.is_valid():
            if register_form.is_valid():
                print('ok 经过RegisterForm验证 ok')
                _status = ''
                nick_name = request.POST.get("nickname", "")
                user_name = request.POST.get("username", "")
                pass_word = request.POST.get("password", "")
                pass_words = request.POST.get("passwords", "")
                if User.objects.filter(username=user_name):
                    _status = {'msg':'账号已经重复','icon':'5'}
                    return HttpResponse(json.dumps(_status),content_type='application/json')
                if pass_word != pass_words:
                    _status = {'msg':'两次密码不对','icon':'5'}
                    return HttpResponse(json.dumps(_status),content_type='application/json')
                # 
                if 'HTTP_X_FORWARDED_FOR' in request.META:
                    get_ip = request.META['HTTP_X_FORWARDED_FOR']
                    get_ip = client_ip.split(",")[0]
                else:
                    get_ip = request.META.get('REMOTE_ADDR')#这里获得代理ip
                print(get_ip)
                # 
                user_profile = User()
                user_profile.nickname= nick_name
                user_profile.username = user_name
                user_profile.email = user_name+'@admin.com'
                user_profile.ip = get_ip
                user_profile.is_active = True
                user_profile.password = make_password(pass_word)
                user_profile.save()
                user = authenticate(username=user_name, password=pass_word)
                login(request, user)
                _status = {'msg':'注册成功','icon':'1'}
                return HttpResponse(json.dumps(_status),content_type='application/json')
            else:
                print('err 没有经过RegisterForm验证 err')
                _status= {'msg':'网络错误，请联系管理员','icon':'5'}
                return HttpResponse(json.dumps(_status),content_type='application/json')
        else:
            _status= {'msg':'验证码错误！','icon':'5'}
            return HttpResponse(json.dumps(_status),content_type='application/json')

        
 


class LogoutView(View):
    """用户登出"""
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("zl-index"))

class LoginView(View):
    """用户登录"""
    def get(self, request):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse("zl-index"))
        else:
            return render(request, "zl955/login.html", {})
    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    _status= {'msg':'登录成功','icon':'1'}
                    return HttpResponse(json.dumps(_status),content_type='application/json')
                else:
                    _status= {'msg':'账户未激活，请联系管理员','icon':'5'}
                    return HttpResponse(json.dumps(_status),content_type='application/json')
            else:
                _status= {'msg':'用户名或密码错误！','icon':'5'}
                return HttpResponse(json.dumps(_status),content_type='application/json')
        else:
            _status= {'msg':'网络错误，请联系管理员','icon':'5'}
            return HttpResponse(json.dumps(_status),content_type='application/json')



class UploadImageView(LoginRequiredMixin, View):
    """
    用户修改头像
    """
    def get(self, request):
        return render(request, "zl955/upload.html", {})
    def post(self, request):
        # image  FILES
        # _img = request.FILES['file']
        _img = request.FILES['avatar']
        image_form = UploadImageForm(request.POST, _img, instance=request.user)
        if image_form.is_valid():
            image_form.save()
            return HttpResponse('上传成功~', content_type='application/json')
        else:
            return HttpResponse('上传失败，请重试！', content_type='application/json')





# class UserinfoView(LoginRequiredMixin, View):
#     """
#     用户个人信息
#     """
#     def get(self, request):
#         return render(request, 'usercenter-info.html', {})

#     def post(self, request):
#         user_info_form = UserInfoForm(request.POST, instance=request.user)
#         if user_info_form.is_valid():
#             user_info_form.save()
#             return HttpResponse('{"status":"success"}', content_type='application/json')
#         else:
#             return HttpResponse(json.dumps(user_info_form.errors), content_type='application/json')




# class UploadImageView(LoginRequiredMixin, View):
#     """
#     用户修改头像
#     """
#     def post(self, request):
#         image_form = UploadImageForm(request.POST, request.FILES, instance=request.user)
#         if image_form.is_valid():
#             image_form.save()
#             return HttpResponse('{"status":"success"}', content_type='application/json')
#         else:
#             return HttpResponse('{"status":"fail"}', content_type='application/json')

