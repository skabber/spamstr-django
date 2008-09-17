from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    company = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=200)
    email = models.EmailField()
    url = models.URLField(blank=True, verify_exists=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "people"    
    
    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)
    
    def get_absolute_url(self):
        return "/person/%s/" % self.id
    
class PhoneNumber(models.Model):
    number = models.CharField(max_length=32)
    label = models.CharField(max_length=32)
    person = models.ForeignKey(Person)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "phones"
    
    def __unicode__(self):
        return u"%s %s" % (self.label, self.number)
