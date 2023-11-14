from django.shortcuts import render,get_object_or_404
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .forms import *
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy,reverse
import requests


# Create your views here.
def home_view(request):
    news=News.objects.order_by('published_time')[:6]
    login_form=CustomLoginForm(request.POST or None , request.FILES or None)
    return render(request,'main/home.html',{'news':news,'log_form':login_form})
def news_view(request):
    news=News.objects.all()
    return render(request,'main/news.html',{'news':news})
def sign(request):
    form=CustomUserCreationForm(request.POST or None , request.FILES or None)
    if form.is_valid():
        user=form.save()
        login(request,user)
        return redirect('home')
    return render(request,'main/auth_sign.html',{'form':form})

def comview(request):
    all=Post.objects.all()
    form = New_p(request.POST or None, request.FILES or None)
    if request.method=="POST":
        if form.is_valid():
            pst=form.save(commit=False)
            pst.author2=request.user
            pst.save() 
            return HttpResponseRedirect(reverse('compage'))
              
    return render(request,"main/com.html",{'posts':all,'form':form,})
def dislikeview(request,pk):
    post=get_object_or_404(Post,id=request.POST.get('post_id'))
    post.votdown.add(request.user)
    return HttpResponseRedirect(reverse('compage'))
def likeview(request,pk):
    post=get_object_or_404(Post,id=request.POST.get('post_id'))
    post.votup.add(request.user)
    return HttpResponseRedirect(reverse('compage'))
def postpagedef(request,post_id):
    main_post=Post.objects.get(pk=post_id)
    comment_form=New_com(request.POST or None ,request.FILES or None)
    if comment_form.is_valid():
        comy=comment_form.save(commit=False)
        comy.author=request.user
        comy.post_id=main_post
        comy.save()
        return redirect('post_page',post_id=post_id)
    return render(request,'main/post_page.html',{'post':main_post,'comment_form':comment_form})
def my_accountdef(request):
    if Profile.objects.filter( user=request.user).exists():
        lprofile=request.user.profile
        up_profile=New_profile(request.POST or None ,request.FILES or None,instance=lprofile)
        if up_profile.is_valid():
            up_profile.save()
            return redirect('home')
    else:
        up_profile=New_profile(request.POST or None ,request.FILES or None)
        if up_profile.is_valid():
             comy=up_profile.save(commit=False)
             comy.user=request.user
             comy.save()
             return redirect('home')

    return render(request,'main/upd_prof.html',{'form':up_profile,})
class CustomLoginView(LoginView):
    form_class = CustomLoginForm
