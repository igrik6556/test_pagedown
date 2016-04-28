from django import forms
from .models import Post
from pagedown.widgets import PagedownWidget


class EditPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text',)
        widgets = {'text': PagedownWidget}
