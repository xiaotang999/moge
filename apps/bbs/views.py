import json 
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.template import loader

# Create your views here.
from .models import CommentSet
from users.models import User

class CommentSetView(View):
    def get(self, request):
        _groups = 'null'
        if request.user.is_authenticated():
            _groups = User.objects.all()
        _messages = CommentSet.objects.order_by('-id')[:5]
        _people = User.objects.all().count()
        _num = CommentSet.objects.all().count()
        return render(request, "zl955/test.html", {
            'messages':_messages,
            'people' : _people,
            'num' : _num,
            'groups' :_groups,
        })