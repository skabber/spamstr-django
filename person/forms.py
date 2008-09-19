from django.forms import ModelForm
from django.forms.formsets import formset_factory
from django.forms.models import inlineformset_factory
from django import forms
from spamstr.person.models import Person, PhoneNumber

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

PhoneNumberFormSet = inlineformset_factory(Person, PhoneNumber, fk_name='person', extra=2)
#PhoneNumberFormSet = formset_factory(PhoneNumberForm, extra=2)