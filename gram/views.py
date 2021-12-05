from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .models import Image, Profile, Like
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from .forms import ImageForm, ProfileForm, CommentForm
from django.contrib.auth import logout# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user
    images = Image.objects.all().order_by('-posted_at')
    profiles = Profile.objects.filter(user_id = current_user.id).all()
    
    if request.method == 'POST':  
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            com = form.save(commit=False)
            com.user = request.user
            com.save()
            return redirect('index')
    
    else:
        form = CommentForm()
        
    return render(request, 'index.html',{"current_user": current_user, "images":images, "profiles":profiles, "form":form})
