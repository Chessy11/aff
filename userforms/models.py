from django.db import models
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from phonenumber_field.modelfields import PhoneNumberField
#import validationerror
from django.core.exceptions import ValidationError

# Create your models here.
#create forms

CRYPTO_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)

DECIDED_TO_INVEST_CHOICES = (
    ('100$', '100$'),
    ('200$', '200$'),
    ('300$', '300$'),
    ('400$', '400$'),
    ('500$', '500$'),
    ('600$', '600$'),
    ('700$', '700$'),
    ('800$', '800$'),
    ('900$', '900$'),
    ('1000$', '1000$'),
)


class Contact(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, default='None')
    email = models.EmailField(max_length=100)
    # get phone number with country code
    phone = PhoneNumberField()
    experience_in_crypto = models.CharField(max_length=100, choices=CRYPTO_CHOICES, default='No')
    if_decided_to_invest = models.CharField(max_length=100, choices=DECIDED_TO_INVEST_CHOICES, default='500$')

    def clean(self):
        if Contact.objects.filter(email=self.email).exists():
            raise ValidationError({'email': 'Email already exists'})
        elif Contact.objects.filter(phone=self.phone).exists():
            raise ValidationError({'phone': 'Phone number already exists'})
        
    def country_code(self):
        return self.phone.country_code
    country_code.short_description = 'Country code'
    
    
    
    def __str__(self):
        return self.name