from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control rounded-4",
            "placeholder": "Enter password",
        }),
        label="Password",
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control rounded-4",
            "placeholder": "Confirm password",
        }),
        label="Confirm password",
    )

    class Meta:
        model = get_user_model()
        fields = ("email",)

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get("password1")
        p2 = cleaned_data.get("password2")
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError("Passwords must match")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your email",
            "id": "floatingInput",
        }),
        label="Email",
    )