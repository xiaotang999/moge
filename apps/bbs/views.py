import json 
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.template import loader
from django.db.models import Count

# Create your views here.
from .models import CommentSet

class CommentSetView(View):
    def get(self, request):
        _messages = CommentSet.objects.order_by('-id')[:5]
        _num = CommentSet.objects.annotate(Count('id'))
        return render(request, "zl955/test.html", {
            'messages':_messages,
            'num' : _num,
        })