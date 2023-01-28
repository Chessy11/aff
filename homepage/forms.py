# from django import forms
# from .models import Contact, CRYPTO_CHOICES, DECIDED_TO_INVEST_CHOICES
# from django.utils.translation import gettext as _
# from phonenumber_field.formfields import PhoneNumberField
# from phonenumber_field.widgets import PhoneNumberPrefixWidget

# # Create your forms here.


# class ContactForm(forms.ModelForm):
#     name = forms.CharField(label='name', 
#                     widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
#     last_name = forms.CharField(label='last_name', 
#                             widget=forms.TextInput(attrs={'placeholder': 'Enter your last name'}))
#     email = forms.EmailField(label='email', 
#                     widget=forms.TextInput(attrs={'placeholder': 'Enter your email'}))
#     #phone codes for countries to choose and write number
    
#     phone = PhoneNumberField(
#                         widget=PhoneNumberPrefixWidget(initial='DE', attrs={'placeholder': 'Your phone number', 
#                         'class': 'form-control',
#                         'style': 'display: inline; width: 10%;'}))
#     experience_in_crypto = forms.ChoiceField(label='experience_in_crypto', choices=CRYPTO_CHOICES,
#                         widget=forms.Select(attrs={'placeholder': 'Do you have experience in crypto?', 'style': 'width: 100%; height: 30px; background-color: #fff; border-radius: 5px; '}))
    
#     if_decided_to_invest = forms.ChoiceField(label='if_decided_to_invest', choices=DECIDED_TO_INVEST_CHOICES,
#                         widget=forms.Select(attrs={'placeholder': 'If you decided to invest, how much would you invest?', 'style': 'width: 100%; height: 30px; background-color: #fff; border-radius: 5px; '}))

#     #if user already filled the form, then he can't fill it again    
# #
    
#     class Meta:
#         model = Contact
#         fields = ('name', 'last_name',  'email', 'phone', 'experience_in_crypto', 'if_decided_to_invest')
        


    