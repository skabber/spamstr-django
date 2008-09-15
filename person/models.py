from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    company = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    url = models.URLField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    
    class Meta:
        db_table = "people"    
    
    def __unicode__(self):
        return u"%s %s - %s" % (self.first_name, self.last_name, self.title)
    
    def get_absolute_url(self):
        return "/person/%s/" % self.id

class PhoneNumber(models.Model):
    number = models.CharField(max_length=32)
    label = models.CharField(max_length=32)
    person = models.ForeignKey(Person)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    
    class Meta:
        db_table = "phones"
    
    def __unicode__(self):
        return u"%s %s" % (self.label, self.number)

class EmailAddress(models.Model):
    email = models.EmailField()
    label = models.CharField(max_length=32)
    person = models.ForeignKey(Person)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    
    class Meta:
        db_table = "emails"
    
    def __unicode__(self):
        return u"%s %s" % (self.label, self.emailAddress)
