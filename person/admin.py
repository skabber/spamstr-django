from django.contrib import admin
from spamstr.person.models import Person, PhoneNumber, EmailAddress

class PhoneNumberInline(admin.StackedInline):
    model = PhoneNumber
    extra = 2

class EmailAddressInline(admin.StackedInline):
    model = EmailAddress
    extra = 2

class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'title')
    inlines = [PhoneNumberInline, EmailAddressInline]

admin.site.register(Person, PersonAdmin)