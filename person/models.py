from django.db import models

class Person(models.Model):
    firstName = models.CharField(max_length=32)
    lastName = models.CharField(max_length=32)
    companyName = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    bangledeshiTitle = models.CharField(max_length=200, blank=True)
    
    def __unicode__(self):
        return u"%s %s - %s" % (self.firstName, self.lastName, self.title) 

class PhoneNumber(models.Model):
    number = models.CharField(max_length=32)
    label = models.CharField(max_length=32)
    person = models.ForeignKey(Person)

    def __unicode__(self):
        return u"%s %s" % (self.label, self.number)

class EmailAddress(models.Model):
    emailAddress = models.EmailField()
    label = models.CharField(max_length=32)
    person = models.ForeignKey(Person)
    
    def __unicode__(self):
        return u"%s %s" % (self.label, self.emailAddress)
