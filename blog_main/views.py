

from django.shortcuts import render
from blogs.models import Category,Blog


def home(request):
    is_featured = Blog.objects.filter(is_featured=True)
    return render(request, 'home.html', {'is_featured':is_featured})