from django import forms
from django.contrib.auth.models import User
from .models import Profile, UserRequest

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    remember_me = forms.BooleanField(required=False,widget=forms.CheckboxInput())

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
   
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('photo','admin_user', 'direccion','telefono','pisos','comunal','RUC')

class UserRequestForm(forms.ModelForm):
    class Meta:
        model = UserRequest
        fields = ('admin_user','edificio', 'direccion','email','phonenumber')

