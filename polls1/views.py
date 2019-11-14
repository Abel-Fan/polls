from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
# Create your views here.
from .models import Questions

def index(request):
    questions = Questions.objects.all()
    return render(request,"polls1/index.html",{'questions':questions})

def question(request,id):
    question = get_object_or_404(Questions, pk=id)
    if request.method == "GET":
        return render(request,'polls1/question.html',{'question':question})
    elif request.method == "POST":
        cid = request.POST.get("choice")
        choice = question.choices_set.filter(id=cid)[0]
        choice.votes+=1
        choice.save()
        return redirect("/detail/%s"%id)

def detail(request,id):
    question = get_object_or_404(Questions, pk=id)
    return render(request,"polls1/detail.html",{'question':question})
