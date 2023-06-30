from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q

from blog_main.forms import RegistrationForm

from .models import Blog, Category
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

# Create your views here.


def posts_by_category(request, category_id):
    #Fetch the posts that belogs to the category with the category_id
    blogs = Blog.objects.filter(status=1, category=category_id)
    category = get_object_or_404(Category, id=category_id)
    return render(request, 'posts_by_category.html', {'blogs':blogs, 'category':category})


def blogs(request, slug):
    blog = get_object_or_404(Blog, slug=slug, status=1)
    return render(request, 'blogs.html', {'blog':blog})


def search(request):
    search = request.GET['search'].strip()
    blogs = Blog.objects.filter(Q(title__icontains=search) | Q(short_description__icontains=search) | Q(blog_body__icontains=search), status=1)
    return render(request, 'search.html', {'blogs':blogs, 'search':search})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    else:
         form = RegistrationForm()
    return render(request, 'register.html', {'form': form})



def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ]
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
            return redirect('home')
    else:
          form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout(request):
    auth.logout(request)
    return redirect('home')
   