from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        min_length=2,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your name',
                'id': 'name'
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your email address',
                'id': 'email'
            }
        )
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Describe your order',
                'id': 'message',
                'cols': '30',
                'rows': '10'
            }
        )
    )
