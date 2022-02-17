from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.forms.widgets import PasswordInput, TextInput

class registerForm(forms.Form):
    username = forms.CharField(max_length=50, label='İstifadəçi adı', widget=forms.TextInput(attrs={'class': 'register_username', 'placeholder': 'İstifadəçi adı daxil edin'}))
    first_name = forms.CharField(max_length=50, label='Adınız', widget=forms.TextInput(attrs={'class':'register_firstname','placeholder': 'Adinizi daxil edin'}))
    last_name = forms.CharField(max_length=50, label='Soyadınız', widget=forms.TextInput(attrs={'class':'register_lastname','placeholder': 'Soyadınızı daxil edin'}))
    email = forms.CharField(max_length=200,  label='Emailinizi yazın', widget=forms.EmailInput(attrs={'class':'register_email','placeholder': 'Emailinizi yazın'}))
    password = forms.CharField(max_length=50, label='Şifrənizi yazın', widget=forms.PasswordInput(attrs={'class': 'register_password', 'placeholder': 'Şifrə daxil edin'}))
    confirm = forms.CharField(max_length=50, label='Şifrənizi təsdiqləyin', widget=forms.PasswordInput(attrs={'class': 'register_confirm', 'placeholder': 'Şifrəni təkrar edin'}))

    def clean(self):
        username = self.cleaned_data.get('username')
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        email = self.cleaned_data.get('email')
        password = self .cleaned_data.get('password')
        confirm = self.cleaned_data.get('confirm')
        if password and confirm and password != confirm:
            raise
        values = {'username': username, 'password': password, 'first_name':first_name, 'last_name':last_name, "email":email}
        return values

class loginForm(forms.Form):
    username = forms.CharField(max_length=50, label='İstifadəçi adı', widget=forms.TextInput(attrs={'class': 'login_username', 'placeholder': 'İstifadəçi adı'}))
    password = forms.CharField(max_length=50, label='Şifrənizi yazın', widget=forms.PasswordInput(attrs={'class': 'login_password', 'placeholder': 'Şifrəniz'}))

class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')
        widgets = {
            'username': TextInput(attrs={'class':'input','placeholder':'İstifadəçi adı'}),
            'first_name': TextInput(attrs={'class':'input','placeholder':'Ad'}),
            'last_name': TextInput(attrs={'class':'input','placeholder':'Soyad'}),
            'email': TextInput(attrs={'class':'input','placeholder':'Email'}),
        }

