import json 
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

# Create your views here.
from .models import CommentSet






class CommentSetView(View):
    def get(self, request):
        _messages = 'asd'
        return render(request, "zl955/test.html", {'_messages':_messages})