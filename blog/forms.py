from django import forms
from blog.models import Post, Comment


class PostForms (forms.Form):

    class Meta():
        model = Post
        fields = {'author', 'title', 'text'}

        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }


class CommentForm (forms.Form):

    class Meta():
        model = Comment
        fields = {'author', 'text'}

    widgets = {
        'author':forms.TextInput(attrs={'class':'textinputclass'}),
        'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
    }