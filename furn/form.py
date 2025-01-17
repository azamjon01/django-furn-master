from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
from furn.models import Profile
from django import forms

User = get_user_model()

class UptadeUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'email']
        
class UptadeProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'phone_number']
        
class Registration(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password1", "password2",]


        

