from django import forms

from comment.models import ProductComment, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment', 'user']


class CommentProductForm(forms.ModelForm):
    class Meta:
        model = ProductComment
        fields = ['comment', 'user']
