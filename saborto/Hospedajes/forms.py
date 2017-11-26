from django import forms

from .models import Post

    class PostForm(forms.ModelForm):

        class Meta:
            model = Post
            fields = ('city', 'guest_amount', 'fecha')

#algo que colgue en seguir, lo copie y pegue de una pagina jaja