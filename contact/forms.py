from django import forms
from contact.models import Contact

class Email(forms.Form):
    Email = forms.EmailField()

    def __str__(self):
        return self.Email

class MyCommentForm(forms.ModelForm):
    class Meta(object):
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                    }
                ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control'
                    }
                ),
            'subject': forms.TextInput(
                attrs={
                    'class': 'form-control'
                     }
                ),
            'message': forms.Textarea(
                attrs={
                    'class': 'form-control'
                    }
                 ),
             }            
