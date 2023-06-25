from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Blog, Category

# Create your views here.


def posts_by_category(request, category_id):
    #Fetch the posts that belogs to the category with the category_id
    blogs = Blog.objects.filter(status=1, category=category_id)
    category = get_object_or_404(Category, id=category_id)
    return render(request, 'posts_by_category.html', {'blogs':blogs, 'category':category})