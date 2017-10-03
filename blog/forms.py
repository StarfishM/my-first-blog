from django import forms

from .models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'language',)


class ImageForm(forms.Form):
    image = forms.ImageField(
        label='Select a file',
        help_text='max. 1 MB'
    )


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
