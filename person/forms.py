from django.forms import ModelForm
from django.forms.formsets import formset_factory
from django import forms
from spamstr.person.models import Person

class PersonForm(ModelForm):
    class Meta:
        model = Person

class PhoneNumberForm(forms.Form):
    number = forms.CharField()
    label = forms.CharField()

PhoneNumberFormSet = formset_factory(PhoneNumberForm, extra=2)