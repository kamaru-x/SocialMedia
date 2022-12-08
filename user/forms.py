from django import forms
from user.models import Profile

class EditProfileForm(forms.ModelForm):
    model = Profile
    fields = '__all__'