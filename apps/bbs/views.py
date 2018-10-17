import json 
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.template import loader

# Create your views here.
from .models import CommentSet

class CommentSetView(View):
    def get(self, request):
        _messages = CommentSet.objects.order_by('-id')[:5]
        return render(request, "zl955/test.html", {'messages':_messages})