from .models import Comment
from django import forms

# instead of html forms, Django provides a class to use forms  https://docs.djangoproject.com/en/4.1/topics/forms/https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/
# there are also other options todo django forms that are not from models https://docs.djangoproject.com/en/4.1/ref/forms/fields/
class CommentForm(forms.ModelForm):
    class Meta:
        # doing this as a class is not really necessary but we're following https://djangocentral.com/creating-comments-system-with-django/
        model = Comment
        fields = ('name', 'email', 'body')