from django.shortcuts import get_object_or_404, redirect, render

from blogs.models import Blog, Category
from django.contrib.auth.decorators import login_required

from dashboard.form import CategoryForm

# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()
    return render(request, 'dashboard/dashboard.html', {'category_count': category_count, 'blogs_count':blogs_count})


def categories(request):
    return render(request, 'dashboard/categories.html')


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm()
    return render(request, 'dashboard/add_category.html', {'form': form})



def edit_category(request, category_id):
    category =  get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
         form = CategoryForm(request.POST, instance=category)
         if form.is_valid():
             form.save()
             return redirect('categories')
    form = CategoryForm(instance=category)
    return render(request, 'dashboard/edit_category.html', {'form': form, "category": category})


def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    return redirect('categories')