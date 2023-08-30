from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.responce import Responce
from rest_framework.view import APIView
from django.contrib import messages
from .models import Blog, Tag
from .serializer import BlogSerializer
from .forms import UserLoginForm, UserRegisterForm
# Create your views here.

class BlogAPIView(APIView):
    def get(self, request):
	    return Responce({'result': 'True'})


def main_render(request):
	return render(request, 'main/index.html')


def blog_render(request):
	return render(request, 'main/blog.html', {'blog': Blog.objects.all().order_by('-id')})


def contacts_render(request):
	return render(request, 'main/contacts.html')


def for_posts(request):
	if request.method == "POST":
		form = Blog()
		form.post_id = request.POST.get('id')
		form.title = request.POST.get('title')
		form.file = request.POST.get('image')
		form.description = request.POST.get('description')
		form.date = request.POST.get('date')
		form.user = request.POST.get('user')
		form.save()
		return redirect('blog')

	return render(request, 'main/addpost.html')

def blog_id(request, id_blog : int):
	id_setting = get_object_or_404(Blog, id = id_blog)

	return render(request, 'main/blog_id.html', {'id_setting': id_setting, 'id': id_blog, 'blog': Blog.objects.all()})

def login(request):
	if request.method == 'POST':
		form = UserLoginForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return redirect('main')
		else:
			messages.error(request, 'Ошибка авторизации или пользователь не обнаружен(')
	else:
		form = UserLoginForm()
	return render(request, 'main/login.html', {'form': form})

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, 'Поздравляю с регистрацией!')
			return redirect('main')
		else:
			messages.error(request, 'Регистрация не выполнена(')
	else:
		form = UserRegisterForm()
	return render(request, 'main/register.html', {'form': form})