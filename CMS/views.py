from django.shortcuts import render, redirect ,get_object_or_404
from django.views import View
from .forms import UserRegisterForm, UserLoginForm , add_PostForm
from django.views.generic import ListView, DetailView
from .models import Blog_post
from django.contrib.auth.views import LoginView
from django.shortcuts import render

class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'Users/register.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to a success page, change to the appropriate URL
        else:
            # Handle the case where the form is not valid
            return render(request, 'Users/register.html', {'form': form})

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
class add_new_post(View):
    template_name = 'addpost.html'

    def get(self, request):
        form = add_PostForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = add_PostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)  # Use commit=False to avoid saving to the database just yet
            blog_post.author = request.user  # Set the author based on the current user
            blog_post.save()  # Save the new Blog_post instance

            # No need to specify 'APP_MEDIA_ROOT' here
            return redirect('index')

        return render(request, self.template_name, {'form': form})

class DeletePostConfirmationView(View):
    template_name = 'delete_post_confirmation.html'

    def get(self, request, post_id):
        blog_post = get_object_or_404(Blog_post, post_id=post_id)
        return render(request, self.template_name, {'post': blog_post})

    def post(self, request, post_id):
        blog_post = get_object_or_404(Blog_post, post_id=post_id)
        blog_post.delete()
        return redirect('index')  # Redirect to the desired page after deleting the post