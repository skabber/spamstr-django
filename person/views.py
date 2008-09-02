from django.shortcuts import get_object_or_404, render_to_response
from spamstr.person.models import Person

def all(request):
    people = Person.objects.all()
    return render_to_response('index.html', {'people': people})
