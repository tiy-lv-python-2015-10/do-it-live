from django import forms
from django.forms import Textarea
from post.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'description', 'price', 'user_email', 'phone_number', 'zipcode', 'images',
                  'sub_category')
        widgets = {
            'description': Textarea(attrs={'rows': 10})

        }
