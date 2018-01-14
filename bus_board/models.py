from django.db import models

# Create your models here.
class BusOrganisation(models.Model):
    '''
    Class to define a bus company
    '''
    name = models.CharField(max_length=255)

    logo = models.ImageField(upload_to="logo-pic/", blank=True) 

    def __str__(self):
        return self.name

    @classmethod
    def get_bus_organisations(cls):
        '''
        Function to get all the buses in the database

        Return
            bus_organisations : list of all the Bus Organisation objects in the database
        '''
        bus_organisations = cls.objects.all()

        return bus_organisations

    @classmethod
    def get_single_bus_organisation(cls, bus_organisation_id):
        '''
        Function to get a bus organisation with the specific id 

        Args
            bus_organisation_id : the bus organisation id 

        Return
            single_bus_origanisation : Bus Organisation object with the specified id 
        '''
        single_bus_origanisation = cls.objects.get(id=bus_organisation_id)

        return single_bus_origanisation

