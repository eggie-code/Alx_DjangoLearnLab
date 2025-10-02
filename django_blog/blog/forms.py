from django import forms
from .models import Post, Profile, comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
     email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True

# creation and editing

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location']



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


#comment form

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your comment here...'}),
        }
