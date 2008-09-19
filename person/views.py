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
    # This does the exact same thing, but in one line.
    #return render_to_response("index.html", {'page_name': 'index', 'people': Person.objects.all()}, RequestContext(request))

def add_or_edit(request, id):
    if id is None:
        person = None
        page_name = "add"
    else:
        person = get_object_or_404(Person, id=id)
        page_name = "edit"
    if request.method == "GET":
        form = PersonForm(instance=person)
        phone_forms = PhoneNumberFormSet(instance=person)
    if request.method == "POST":
        form = PersonForm(request.POST, instance=person)
        phone_forms = PhoneNumberFormSet(request.POST, instance=person)
        if form.is_valid() and phone_forms.is_valid():
            person = form.save()
            phone_forms = PhoneNumberFormSet(request.POST, instance=person)
            phone_forms.is_valid()
            phone_forms.save()
            return HttpResponseRedirect('/person/%s/' % person.id)
    return render_to_response('add.html', {'page_name': page_name, 'form': form, 'phone_forms': phone_forms, 'person': person}, RequestContext(request))

def delete(request, id):
    person = Person.objects.get(id=id)
    person.delete()
    return HttpResponseRedirect('/')

def detail(request, id):
    person = Person.objects.get(id=id)
    return render_to_response('detail.html', {'page_name': 'detail','person': person}, RequestContext(request))