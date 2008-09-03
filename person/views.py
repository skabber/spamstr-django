from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from spamstr.person.models import Person
from spamstr.person.forms import PersonForm

def all(request):
    people = Person.objects.all()
    return render_to_response('index.html', {'people': people})

def add(request):
    if request.method == "GET":
        form = PersonForm()
    else:
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            person = form.save()
            print person
    return render_to_response('add.html', {'form': form})

def delete(request, id):
    person = Person.objects.get(id=id)
    person.delete()
    return HttpResponseRedirect('/')

def detail(request, id):
    person = Person.objects.get(id=id)
    return render_to_response('detail.html', {'person': person})