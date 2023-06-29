from django.contrib import admin
from .models import Category, Blog,SocialLink


# Register your models here.

class BlogModel(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'author','status', 'is_featured')
    search_fields  = ('title', 'category', 'author','status')
    list_editable = ('is_featured',)


admin.site.register(Category)
admin.site.register(Blog, BlogModel)
admin.site.register(SocialLink)