
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
from blogs import views as BlogsView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name='home' ),
    path('category/', include('blogs.urls')),
    path('blogs/<slug:slug>/', BlogsView.blogs, name='slug'),
    path('blogs/search/', BlogsView.search, name='search'),
    path('register/', BlogsView.register, name='register'),
    path('login/', BlogsView.login, name='login'),
    path('logout/', BlogsView.logout, name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
