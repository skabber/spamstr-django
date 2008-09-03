from django.forms import ModelForm
from spamstr.person.models import Person

class PersonForm(ModelForm):
    class Meta:
        model = Person