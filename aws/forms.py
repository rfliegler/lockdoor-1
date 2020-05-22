from django import forms

class PostForm(forms.Form):
         post = forms.CharField(label='')
