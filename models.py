from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class LogBookEntry(models.Model):
    username= models.ForeignKey(User, )
    flight_date = models.DateField()
    plane = models.ForeignKey('Airplane')
    airport_from = models.CharField(max_length=4)
    airport_to  = models.CharField(max_length=4)
    remarks = models.TextField(null=True,blank=True)
    number_instructor_app =  models.DecimalField(decimal_places=1,max_digits=3,null=True,blank=True)
    number_landings = models.DecimalField(decimal_places=1,max_digits=3,null=True,blank=True)
    airplane_sel = models.DecimalField(decimal_places=1,max_digits=3,null=True,blank=True)
    airplane_mel = models.DecimalField(decimal_places=1,max_digits=3,null=True,blank=True)
    cross_country = models.DecimalField(decimal_places=1,max_digits=3,null=True,blank=True)
    day_time = models.DecimalField(decimal_places=1,max_digits=3,null=True,blank=True)
    night_time = models.DecimalField(decimal_places=1,max_digits=3,null=True,blank=True)
    actual_instrument = models.DecimalField(decimal_places=1,max_digits=3,null=True,blank=True)
    simulated_instrument = models.DecimalField(decimal_places=1,max_digits=3,null=True,blank=True)
    ground_trainer = models.DecimalField(decimal_places=1,max_digits=3,null=True,blank=True)
    dual_received = models.DecimalField(decimal_places=1,max_digits=3,null=True,blank=True)
    pilot_in_command = models.DecimalField(decimal_places=1,max_digits=3,null=True,blank=True)
    instructor = models.CharField(max_length=30,null=True,blank=True)
    total_duration_of_flight = models.DecimalField(decimal_places=1,max_digits=3)
    link = models.CharField(max_length=200,null=True,blank=True)

    def __unicode__(self):
        return "Date: %s Total: %s" % (self.flight_date,self.total_duration_of_flight)

class Airplane(models.Model):
    make = models.CharField(max_length=30)
    airplane_model = models.CharField(max_length=30)
    year  = models.CharField(max_length=4)
    ident = models.CharField(max_length=6)

    def __unicode__(self):
        return "%s" % (self.airplane_model)
    
    
