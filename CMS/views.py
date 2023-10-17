from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterForm

class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'Users/register.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)  # Instantiate the form with request data

        if form.is_valid():
            form.save()
            return redirect('index')

def index(request):
    contextvars = {}
    return render(request, 'index.html', contextvars)
