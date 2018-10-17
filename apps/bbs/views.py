import json 
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

# Create your views here.
from .models import CommentSet



class CommentSetView(View):
    """用户注册"""
    def get(self, request):
        _messages = CommentSet.objects.all()
        # _status= {'msg':'网络错误，请联系管理员','icon':'5'}
        return HttpResponse(_messages,content_type='application/json')
    def post(self, request):
        pass
        
        
 


# class LogoutView(View):
#     """用户登出"""
#     def get(self, request):
#         logout(request)
#         return HttpResponseRedirect(reverse("zl-index"))

# class LoginView(View):
#     """用户登录"""
#     def get(self, request):
#         if request.user.is_authenticated():
#             return HttpResponseRedirect(reverse("zl-index"))
#         else:
#             return render(request, "zl955/login.html", {})
#     def post(self, request):
#         login_form = LoginForm(request.POST)
#         if login_form.is_valid():
#             user_name = request.POST.get("username", "")
#             pass_word = request.POST.get("password", "")
#             user = authenticate(username=user_name, password=pass_word)
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     _status= {'msg':'登录成功','icon':'1'}
#                     return HttpResponse(json.dumps(_status),content_type='application/json')
#                 else:
#                     _status= {'msg':'账户未激活，请联系管理员','icon':'5'}
#                     return HttpResponse(json.dumps(_status),content_type='application/json')
#             else:
#                 _status= {'msg':'用户名或密码错误！','icon':'5'}
#                 return HttpResponse(json.dumps(_status),content_type='application/json')
#         else:
#             _status= {'msg':'网络错误，请联系管理员','icon':'5'}
#             return HttpResponse(json.dumps(_status),content_type='application/json')
