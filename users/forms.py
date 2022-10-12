from django import forms
from allauth.account.forms import SignupForm


class CustomSignupForm(SignupForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.', widget=forms.EmailInput
                             (attrs={'class': 'form-style', 
                                     'type': 'email', 
                                     'placeholder': 'Email',
                                     'id': 'logemail',
                                     'autocomplete': 'off',
                                     }))
    
    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields.pop('password1')
    
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.email = self.cleaned_data['email']
        user.save()
        return user
