from django import forms
from post.models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    category = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    class Meta:
        model = Post
        fields = [
            'title',
            'category',
            'description',
        ]
        labels = {
            'title': 'Title',
            'category': 'Category',
            'description': 'Description',
        }
