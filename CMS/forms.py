from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        # Override widget attributes to set placeholders and hide labels
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Username',
            'class': 'form-control',
           # You can add other classes or attributes as needed
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Password',
            'class': 'form-control',  # You can add other classes or attributes as needed
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Confirm Password',
            'class': 'form-control',  # You can add other classes or attributes as needed
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'Email',
            'class': 'form-control',  # You can add other classes or attributes as needed
        })
        self.fields['username'].label = False
        self.fields['password1'].label = False
        self.fields['password2'].label = False
        self.fields['email'].label = False
    class Meta:
       model = User
       fields = ['username', 'email', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

        # Override widget attributes to set placeholders and hide labels
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Username',
            'class': 'form-control',
           # You can add other classes or attributes as needed
        })
        self.fields['password'].widget.attrs.update({
            'placeholder': 'Password',
            'class': 'form-control',  # You can add other classes or attributes as needed
        })
        self.fields['username'].label =False
        self.fields['password'].label = False

    class Meta:
        fields = ['username', 'password']