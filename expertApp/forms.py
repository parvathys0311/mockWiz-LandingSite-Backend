from django.forms import ModelForm, ModelChoiceField, TextInput, EmailInput, Select

from pagesApp.models import Function
from .models import Expert
from django import forms

class Expertform(ModelForm):
    expertiseFunction = ModelChoiceField(Function.objects.all(), empty_label="Primary Function")
    class Meta:
        model=Expert
        fields=('firstName','email','expertiseFunction','yearsInterviewedFor'
               )
        widgets = {
            'firstName': TextInput(attrs={'id': 'Name', 'placeholder': 'First Name', 'class': 'ex-input'}),
            'email': EmailInput(attrs={'id': 'Email', 'placeholder': 'Email Address', 'class': 'ex-input'}),
            'expertiseFunction': Select(attrs={'id': 'Function', 'class': 'ex-input'}),
            'yearsInterviewedFor': Select(attrs={'id': 'yearsInterviewed', 'class': 'ex-input'})
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if (Expert.objects.filter(email=email).exists()):
            # this condition is true while registering a new form record
            raise forms.ValidationError('Email already exists. Looks like you have made an inquiry already. We will get back to you soon.')
        return email