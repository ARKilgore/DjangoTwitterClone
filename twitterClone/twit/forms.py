
from django import forms
from twit.models import *
from models import *
from django.conf import settings
import datetime

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    
class RegisterForm(forms.ModelForm):
    error_messages = {
        'duplicate_username': "A user with that username already exists.",
        'password_mismatch': "The two password fields didn't match.",
    }
    username = forms.RegexField(label="Username", max_length=30)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput, help_text="Enter the same password as above, for verification.")

    class Meta:
        model = User
        fields = ('email','username')
        widgets={
	        'email': forms.EmailInput(attrs={'class': 'form-control text-center', 'placeholder': 'Email Address'}),
            'username':forms.TextInput(attrs={'class':'form-control text-center','placeholder':'Username'}),
            }

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            User._default_manager.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user