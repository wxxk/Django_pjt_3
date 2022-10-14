from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = get_user_model()
        fields = [
            "username",
            "first_name",
            "last_name",
            "password1",
            "password2",
            "email",
        ]


class CustomUserChangeForm(UserChangeForm):
    password = None

    class Meta(UserChangeForm):
        model = get_user_model()
        fields = ["username", "email"]
