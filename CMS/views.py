from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from .forms import UserRegisterForm, UserLoginForm
from django.views.generic import ListView, DetailView
from .models import Blog_post
from django.contrib.auth.views import LoginView


class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'Users/register.html', {'form': form})

    def post(self, request):
        form = UserLoginForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect('index')


class CustomLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'


class BlogListView(ListView):
    model = Blog_post
    queryset = Blog_post.objects.all().order_by('-modified')
    template_name = 'index.html'
    context_object_name = 'blog_posts'


class Detail_Blogpost_view(DetailView):
    model = Blog_post
    template_name = 'blog_post.html'


class MyPostListView(ListView):
    model = Blog_post
    template_name = 'users/myposts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Blog_post.objects.filter(author=self.request.user).order_by('author__username')
