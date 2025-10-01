from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserregistrationForm(UserCreationForm):
    """
    Customer form for user registration that includes the email field.
    """
    class Meta:
        model = user
        fields = ('username', 'email', 'password', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # nake email required
        self.fields['email'].required = True
