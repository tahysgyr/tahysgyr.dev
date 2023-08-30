"""tahysgyr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main import views
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'Рут-панель'
admin.site.index_title = 'Администрирование сайта TaHySgYr'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_render, name='main'),
    path('blog/', views.blog_render, name='blog'),
    path('contacts/', views.contacts_render, name='contacts'),
    path('add_post/', views.for_posts, name='add_post'),
    path('blog/<int:id_blog>', views.blog_id, name='blog_id'),
    path('login/', views.login, name='authentication'),
    path('register/', views.register, name='registration'),
    path('api/v2/blog',views.BlogAPIView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)