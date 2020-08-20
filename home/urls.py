from . import views
from django.urls import path

urlpatterns = [
	path('', views.Home.as_view(), name = 'home'),
	path('blog-list', views.PostList.as_view(), name = 'blog-list'),
	path('<slug:slug>/', views.PostDetail.as_view(), name = 'post_detail'),
	path('about-me', views.AboutMe.as_view(), name = 'about-me'),
]