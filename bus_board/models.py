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

class Route(models.Model):
    '''
    Class to define a bus route
    '''
    departure_location = models.CharField(max_length=255)

    destination_location = models.CharField(max_length=255)

    def __str__(self):
        return self.departure_location + '-' + self.destination_location

    @classmethod
    def get_routes(cls):
        '''
        Function to get all the bus routes in the database

        Return
            routes : list of all the Route objects in the database
        '''
        routes = cls.objects.all()

        return routes

    @classmethod
    def get_single_route(cls, route_id):
        '''
        Function to get a bus route with the specific id 

        Args
            route_id : the bus route id 

        Return
            single_route : Route object with the specified id 
        '''
        single_route = cls.objects.get(id=route_id)

        return single_route

class Bus(models.Model):
    '''
    Class to define a bus 
    '''
    bus_organisation = models.ForeignKey(BusOrganisation, on_delete=models.CASCADE)

    number_plate = models.CharField(max_length=50)

    route = models.ForeignKey(Route, on_delete=models.CASCADE)

    capacity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.bus_organisation.name + ' Bus No.' + self.id

    @classmethod
    def get_buses(cls):
        '''
        Function to get all the buses in the database

        Return
            buses : list of all the Bus objects in the database
        '''
        buses = cls.objects.all()

        return buses

    @classmethod
    def get_single_bus(cls, bus_id):
        '''
        Function to get a bus with the specific id 

        Args
            bus_id : the bus id 

        Return
            single_bus : Bus object with the specified id 
        '''
        single_bus = cls.objects.get(id=bus_id)

        return single_bus

    @classmethod
    def get_bus_organisation_buses(cls, bus_organisation_id):
        '''
        Function to get buses belonging to the bus organisation with the specific id 

        Args
            bus_organisation_id : the bus organisation id 

        Return
            bus_origanisation_buses : list of all the Bus objects in the database with the specified bus organisation id
        '''
        bus_origanisation_buses = cls.objects.filter(bus_organisation=bus_organisation_id)

        return bus_origanisation_buses

    @classmethod
    def get_route_buses(cls, route_id):
        '''
        Function to get buses belonging to the bus route with the specific id 

        Args
            route_id : the route id 

        Return
            route_buses : list of all the Bus objects in the database with the specified route id
        '''
        route_buses = cls.objects.filter(route=route_id)

        return route_buses



