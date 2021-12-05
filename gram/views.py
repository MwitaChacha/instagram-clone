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
    
    return render(request, 'index.html')