from django.contrib.auth.forms import AuthenticationForm, forms
from django.core.exceptions import ValidationError


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class:': 'form-control'}))
    password = forms.PasswordInput()

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise ValidationError("This account is inactive.", code='inactive', )
        if not user.is_admin:
            raise ValidationError("Invalid user type", code='inactive', )
