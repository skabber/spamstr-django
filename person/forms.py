from django.forms import ModelForm
from django.forms.formsets import formset_factory
from django import forms
from spamstr.person.models import Person

LABEL_CHOICES = (
    ("home", "home"),
    ("mobile", "mobile"),
    ("work", "work"),
    ("fax", "fax")
)

class PersonForm(ModelForm):
    class Meta:
        model = Person

class PhoneNumberForm(forms.Form):
    number = forms.CharField()
    label = forms.ChoiceField(choices=LABEL_CHOICES)

PhoneNumberFormSet = formset_factory(PhoneNumberForm, extra=2)