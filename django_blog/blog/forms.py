from django import forms
from .models import Post, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True

# creation and editing


class PostForm(forms.ModelForm):
    """
    A ModelForm for the Post model, used for creating and updating posts.
    """
    class Meta:
        model = Post
        # We only let the user input title and content.
        # 'author' will be set automatically by the view.
        fields = ['title', 'content']
        widgets = {
            # Make content textarea larger
            'content': forms.Textarea(attrs={'rows': 10}),
        }
