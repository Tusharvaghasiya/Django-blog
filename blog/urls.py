from django.urls import path, include
from . import views
from . views import (PostListView, 
	PostDetailView, 
	PostDetailView,
	PostCreateView,
	PostUpdateView)
# <app>/<model>_<viewtype>.html
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='blog-detail'),
    path('new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='blog-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('about/', views.about, name='blog-about'),


]
