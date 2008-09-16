from django.contrib import admin
from spamstr.person.models import Person, PhoneNumber

class PhoneNumberInline(admin.StackedInline):
    model = PhoneNumber
    extra = 2

class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'title')
    inlines = [PhoneNumberInline]

admin.site.register(Person, PersonAdmin)