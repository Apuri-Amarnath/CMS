from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterForm, UserLoginForm
from django.views.generic import ListView, DetailView
from .models import Blog_post
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404

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


class Detail_Blogpost_view(DetailView):
    model = Blog_post
    template_name = 'individual_blog_post.html'
    context_object_name = 'post'



class all_post_view(ListView):
    model = Blog_post
    queryset = Blog_post.objects.all().order_by('-modified')
    template_name = 'index.html'

class MyPostListView(ListView):
    model = Blog_post
    template_name = 'users/myposts.html'

    def get_queryset(self):
        return Blog_post.objects.filter(author=self.request.user)
