from django.shortcuts import render
from django.http import HttpResponse
from . models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# handle traffic from homepage
# render looks at templates folder directly
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)



class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'

	# loopable variable
	context_object_name = 'posts'
	ordering = ['date_posted']


class PostDetailView(DetailView):
	model = Post
	context_object_name = 'posts'
	

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content']

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		else:
			return False


# To save user id
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


