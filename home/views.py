from django.shortcuts import render
from django.views import generic
from .models import Post
from django.views.generic.base import TemplateView

# Create your views here.
class Home(TemplateView):
	template_name = 'home.html'

class PostList(generic.ListView):
	queryset = Post.objects.filter(post_status = 1).order_by('-created_on')
	template_name = 'blog-list.html'

class PostDetail(generic.DetailView):
	model = Post
	template_name = 'post_detail.html'

class AboutMe(TemplateView):
	template_name = 'about_me.html'
