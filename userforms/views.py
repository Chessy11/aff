from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
#import validation error
from django.core.exceptions import ValidationError
# Create your views here.
from .models import Contact


def user_forms(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            context = {'form': form}
            return render(request, 'thanks/thanks.html', context)
        else:
            if form.errors:
                print(form.errors)
    context = {'form': form}

    
    return render(request, 'user-forms/user-forms.html', context)