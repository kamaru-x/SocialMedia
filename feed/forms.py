from django import forms
from feed.models import Post

class NewPostForm(forms.ModelForm):
    picture = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control text-primary'}))
    caption = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control text-primary','placeholder':'Caption'}))
    tag = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control text-primary','placeholder':'Enter tags'}))

    class Meta:
        model = Post
        fields = ['picture','caption','tag']