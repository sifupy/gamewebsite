from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    # Define a custom style for the form fields
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={'class': 'form-control my-form-field', 'style': 'background-color:#222; color: white;'}),
        help_text='Required.150 characters or fewer .Latters,digists and @/.-_ only',

    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control my-form-field', 'style': 'background-color: #222; color: white;'}),
        help_text='Your password should have at least 8 characters.<br>'
        '.Your password cant be a commonly used password.<br> ' '.Your password cant be entirely numerie',
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control my-form-field', 'style': 'background-color: #222; color: white;'}),
        help_text='Enter the same password as above for verification.',
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control my-form-field', 'style': 'background-color: #222 ; color: white;'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control my-form-field', 'style': 'background-color: #222; color: white;'}),
    )

class New_p(forms.ModelForm):
    class Meta:
        model=Post
        exclude=('author2','votup','votdown')
        widgets={
            'img':forms.ClearableFileInput(attrs={
                'class':"form-control my-form-field2 ",
                'style': 'max-width: 500px;background-color: #222 ; color: white;',
            }),
            'text1':forms.TextInput(attrs={
                'class':"form-control my-form-field2",
                'style': 'max-width: 500px;background-color: #222 ; color: white;',
                'placeholder':"drop thoughts",
            }),
            'text':forms.Textarea(attrs={
                'class':"form-control my-form-field2 ",
                'style': 'max-width: 500px;height:40px;max-height:120px;background-color: #222 ; color: white;',
                'placeholder':"if u have more to say ",
            })
        }
class New_com(forms.ModelForm):
    class Meta:
        model=Comment
        exclude=('author','post_id')
        widgets={
            'text':forms.Textarea(attrs={
                'class':"form-control my-form-field2 ",
                'style': 'max-width: 500px;height:90px;max-height:120px;background-color: #222 ; color: white;',
                'placeholder':"drop ur comment here  ",
            })
        }
        labels = {
            'text':"",
        }
class New_profile(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=('user',)
        widgets={
            'bio':forms.Textarea(attrs={
                'class':"form-control my-form-field2 ",
                'style': 'height:90px;max-height:120px;background-color: #222 ; color: white;',
                'placeholder':"write something about your self ur self like : hello i'm sif my pubg id is .....  ",
            }),
            'profile_pic':forms.ClearableFileInput(attrs={
                'class':"form-control my-form-field2",
                'style': 'background-color: #222 ; color: white;',
            }),
        }