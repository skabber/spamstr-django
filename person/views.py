from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import Context, loader, RequestContext

from spamstr.person.models import Person, PhoneNumber
from spamstr.person.forms import PersonForm, PhoneNumberFormSet

def index(request):
    people = Person.objects.all()
    template = loader.get_template('index.html')
    context = RequestContext(request)
    context.update({'page_name': 'index', 'people': people})
    return HttpResponse(template.render(context))

def add(request):
    if request.method == "GET":
        form = PersonForm()
        phone_forms = PhoneNumberFormSet()
    else:
        form = PersonForm(request.POST)
        phone_forms = PhoneNumberFormSet(request.POST)
        if form.is_valid() and phone_forms.is_valid():
            person = form.save()
            for form in phone_forms.forms:
                print form.has_changed()
                if form.has_changed():
                    phone_number = PhoneNumber.objects.create(person=person, number=form.cleaned_data['number'], label=form.cleaned_data['label'])
            return HttpResponseRedirect('/')
    return render_to_response('add.html', {'page_name': 'add', 'form': form, 'phone_forms': phone_forms}, RequestContext(request))

def edit(request, id):
    person = Person.objects.get(id=id)
    if request.method == "GET":
        form = PersonForm(instance=person)
        phone_forms = PhoneNumberFormSet()
    return render_to_response('add.html', {'page_name': 'add', 'form': form, 'phone_forms': phone_forms}, RequestContext(request))

def delete(request, id):
    person = Person.objects.get(id=id)
    person.delete()
    return HttpResponseRedirect('/')

def detail(request, id):
    person = Person.objects.get(id=id)
    return render_to_response('detail.html', {'page_name': person,'person': person}, RequestContext(request))