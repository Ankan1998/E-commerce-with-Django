from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class GuestForm(forms.Form):
    email    = forms.EmailField(label='         ',widget=forms.EmailInput(
                    attrs={
                        "class": "form-control", 
                        "placeholder": "Your email"
                    }
                    ))


class LoginForm(forms.Form):
    username = forms.CharField(label='          ',widget=forms.TextInput(
                    attrs={
                        "class": "form-control", 
                        "placeholder": "Username"
                    }
                    )
            )
    password = forms.CharField(label='          ',widget=forms.PasswordInput(attrs={
                        "class": "form-control", 
                        "placeholder": "Password"
                    }))



class RegisterForm(forms.Form):
    username = forms.CharField(label='          ',widget=forms.TextInput(
                    attrs={
                        "class": "form-control", 
                        "placeholder": "Username"
                    }
                    ))
    email    = forms.EmailField(label='         ',widget=forms.EmailInput(
                    attrs={
                        "class": "form-control", 
                        "placeholder": "Your email"
                    }
                    ))
    password = forms.CharField(label='          ',widget=forms.PasswordInput(attrs={
                        "class": "form-control", 
                        "placeholder": "Password"
                    }))
    password2 = forms.CharField(label='         ', widget=forms.PasswordInput(attrs={
                        "class": "form-control", 
                        "placeholder": "Re-type Password"
                    }))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2 != password:
            raise forms.ValidationError("Passwords must match.")
        return data

