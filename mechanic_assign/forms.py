from django import forms
from mechanic_assign.models import CustomUser, booking, comparison
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *






class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username','email','password')
    
    
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username','email','password')
        
        
class bookingform(forms.ModelForm):
    class Meta:
        model = booking
        fields = ('address', 'time','services','is_inspection')
        
class comparison_img(forms.ModelForm): 
  
    class Meta: 
        model = comparison 
        fields = ['before_image', 'after_image', 'booking'] 
        

