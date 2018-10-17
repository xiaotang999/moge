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

        print(_messages)
        return HttpResponse(json.dumps(_messages),content_type='application/json')
    def post(self, request):
        pass