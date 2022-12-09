from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Se requiere un email valido de hasta 254 caracteres")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email ya registrado")
        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link']
        widgets = {
            'avatar': forms.ClearableFileInput(),
            'bio': forms.Textarea(attrs={'placeholder': 'biografía'}),
            'link': forms.URLInput(attrs={'placeholder': 'Link'})
        }


class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text="Se requiere un email valido de hasta 254 caracteres")

    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("Email ya registrado")
        return email
