from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterForm
from django.views.generic import ListView,DetailView
from .models import Blog_post

class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'Users/register.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

class BlogListView(ListView):
    model = Blog_post
    queryset = Blog_post.objects.all().order_by('-modified')
    template_name = 'index.html'
    context_object_name = 'blog_posts'
class Detail_Blogpost_view(DetailView):
    model = Blog_post
    template_name = 'blog_post.html'