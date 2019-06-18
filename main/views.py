from django.shortcuts import render
from django.http import HttpResponse
from main.models import comments
from main.models import que
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.shortcuts import render
import datetime

def add_que(request):
    if request.method == "POST":
        ques = que()
        ques.email = request.POST.get("name")
        ques.save()
    return HttpResponseRedirect("/main/index.html")

def create(request):
    if request.method == "POST":
        com = comments()
        com.person = request.POST.get("person")
        com.city = request.POST.get("city")
        com.text = request.POST.get("text")
        com.data_comments = datetime.datetime.now() 
        com.use = False;
        com.save()
    return HttpResponseRedirect("/main/comment.html")

def index(request):
    return render(request, "main/index.html")

def about(request):
    return render(request, "main/about.html")

def news(request):
    return render(request, "main/news.html")

def team(request):
    return render(request, "main/team.html")

def contact(request):
    return render(request, "main/contact.html")

def comment(request):
    return render(request, "main/comment.html")



