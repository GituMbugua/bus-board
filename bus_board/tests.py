from django.test import TestCase
from .models import BusOrganisation, Route, Bus, Schedule
from datetime import datetime, date, time
from django.utils import timezone

# Create your tests here.
class BusOrganisationTestClass(TestCase):
    '''
    Test case for the Bus Organisation class
    '''
    def setUp(self):
        '''
        Method that creates an instance of Bus Organisation class
        '''
        # Create instance of Bus Organisation class
        self.new_bus_organisation = BusOrganisation(name='Kiki And Son ltd')

    def test_instance(self):
        '''
        Test case to check if self.new_bus_organisation in an instance of Bus Organisation class
        '''
        self.assertTrue( isinstance(self.new_bus_organisation, BusOrganisation) )

    def test_get_bus_organisations(self):
        '''
        Test to check if all bus organisations are gotten from the database
        '''
        self.new_bus_organisation.save()

        self.test_bus_organisation = BusOrganisation(name="Anothe Bus Ltd")

        self.test_bus_organisation.save()

        gotten_buses = BusOrganisation.get_bus_organisations()

        bus_organisations = BusOrganisation.objects.all()

        self.assertTrue( len(gotten_buses) == len(bus_organisations) )

    def test_get_single_bus_organisation(self):
        '''
        Test to check if the specified bus organisation is gotten from the database
        '''
        self.new_bus_organisation.save()

        self.test_bus_organisation = BusOrganisation(name="Another Bus Ltd")

        self.test_bus_organisation.save()

        gotten_bus = BusOrganisation.get_single_bus_organisation(self.new_bus_organisation.id)

        # bus_organisations = BusOrganisation.objects.all()
        
        self.assertTrue( isinstance(gotten_bus, BusOrganisation))

class RouteTestClass(TestCase):
    '''
    Test case for the Route class
    '''
    def setUp(self):
        '''
        Method that creates an instance of Route class
        '''
        # Create instance of Route class
        self.new_route = Route(departure_location='Nairobi', destination_location='Mombasa')

    def test_instance(self):
        '''
        Test case to check if self.new_route in an instance of Route class
        '''
        self.assertTrue( isinstance(self.new_route, Route) )

    def test_get_routes(self):
        '''
        Test to check if all routes are gotten from the database
        '''
        self.new_route.save()

        self.test_route = Route(departure_location='Nakuru', destination_location='Nairobi')

        self.test_route.save()

        gotten_routes = Route.get_routes()

        routes = Route.objects.all()

        self.assertTrue( len(gotten_routes) == len(routes) )

    def test_get_single_route(self):
        '''
        Test to check if the specified route is gotten from the database
        '''
        self.new_route.save()

        self.test_route = Route(departure_location='Naivasha', destination_location='Nairobi')

        self.test_route.save()

        gotten_route= Route.get_single_route(self.new_route.id)

        # routes = Route.objects.all()
        
        self.assertTrue( isinstance(gotten_route, Route))

    def test_get_search_route(self):
        '''
        Test to check if the route with the specified depature and arrival locations is gotten from the database
        '''
        self.new_route.save()

        self.test_route = Route(departure_location='Naivasha', destination_location='Nairobi')

        self.test_route.save()

        self.test_route2 = Route(departure_location='Naivasha', destination_location='Nairobi')

        self.test_route2.save()

        search_departure_location = 'Naivasha'

        search_destination_location = 'Nairobi'

        gotten_route = Route.get_search_route(search_departure_location, search_destination_location)

        # routes = Route.objects.all()
        
        self.assertTrue( isinstance(gotten_route, Route))

class BusTestClass(TestCase):
    '''
    Test case for the Bus class
    '''
    def setUp(self):
        '''
        Method that creates an instance of Bus class
        '''
        # Create instance of Bus Organisation class
        self.test_bus_organisation = BusOrganisation(name='Kiki And Son ltd')

        self.test_bus_organisation.save()

        # Create instance of Route class
        self.test_route = Route(departure_location='Nairobi', destination_location='Mombasa')

        self.test_route.save()

        # Create instance of Bus class
        self.new_bus = Bus(bus_organisation=self.test_bus_organisation, number_plate='KBC 243J', route=self.test_route, capacity=34 )

    def test_instance(self):
        '''
        Test case to check if self.new_bus in an instance of Route class
        '''
        self.assertTrue( isinstance(self.new_bus, Bus) )

    def test_get_buses(self):
        '''
        Test to check if all buses are gotten from the database
        '''
        self.new_bus.save()

        self.another_bus_organisation = BusOrganisation(name="Another Bus Ltd")

        self.another_bus_organisation.save()

        self.another_route = Route(departure_location='Nakuru', destination_location='Nairobi')

        self.another_route.save()

        self.test_bus = Bus(bus_organisation=self.another_bus_organisation, number_plate='KCJ 523T', route=self.another_route, capacity=44 )

        self.test_bus.save()

        gotten_buses = Bus.get_buses()

        buses = Bus.objects.all()

        self.assertTrue( len(gotten_buses) == len(buses) )

    def test_get_single_bus(self):
        '''
        Test to check if the specified bus is gotten from the database
        '''
        self.new_bus.save()

        self.another_bus_organisation = BusOrganisation(name="Another Bus Ltd")

        self.another_bus_organisation.save()

        self.another_route = Route(departure_location='Nakuru', destination_location='Nairobi')

        self.another_route.save()

        self.test_bus = Bus(bus_organisation=self.another_bus_organisation, number_plate='KCJ 523T', route=self.another_route, capacity=44 )

        self.test_bus.save()

        gotten_bus = Bus.get_single_bus(self.new_bus.id)

        # buses = Bus.objects.all()
        
        self.assertTrue( isinstance(gotten_bus, Bus))

    def test_get_bus_organisation_buses(self):
        '''
        Test to check if all buses for a specific bus organisation are gotten from the database
        '''
        self.new_bus.save()

        self.another_bus_organisation = BusOrganisation(name="Another Bus Ltd")

        self.another_bus_organisation.save()

        self.another_route = Route(departure_location='Nakuru', destination_location='Nairobi')

        self.another_route.save()

        self.test_bus = Bus(bus_organisation=self.another_bus_organisation, number_plate='KCJ 523T', route=self.another_route, capacity=44 )

        self.test_bus.save()

        self.test_bus2 = Bus(bus_organisation=self.another_bus_organisation, number_plate='KBY 312T', route=self.test_route, capacity=38 )

        self.test_bus2.save()

        gotten_buses = Bus.get_bus_organisation_buses(self.another_bus_organisation.id)

        buses = Bus.objects.all()

        self.assertTrue( len(gotten_buses) != len(buses) )

    def test_get_route_buses(self):
        '''
        Test to check if all buses for a specific bus route are gotten from the database
        '''
        self.new_bus.save()

        self.another_bus_organisation = BusOrganisation(name="Another Bus Ltd")

        self.another_bus_organisation.save()

        self.another_route = Route(departure_location='Nakuru', destination_location='Nairobi')

        self.another_route.save()

        self.test_bus = Bus(bus_organisation=self.another_bus_organisation, number_plate='KCJ 523T', route=self.another_route, capacity=44 )

        self.test_bus.save()

        self.test_bus2 = Bus(bus_organisation=self.test_bus_organisation, number_plate='KBY 312T', route=self.another_route, capacity=38 )

        self.test_bus2.save()

        gotten_buses = Bus.get_route_buses(self.another_route.id)

        buses = Bus.objects.all()

        self.assertTrue( len(gotten_buses) != len(buses) )

class ScheduleTestClass(TestCase):
    '''
    Test case for the Schedule class
    '''
    def setUp(self):
        '''
        Method that creates an instance of Schedule class
        '''
        # Create instance of Bus Organisation class
        self.test_bus_organisation = BusOrganisation(name='Kiki And Son ltd')

        self.test_bus_organisation.save()

        # Create instance of Route class
        self.test_route = Route(departure_location='Nairobi', destination_location='Mombasa')

        self.test_route.save()

        # Create instance of Bus class
        self.test_bus = Bus(bus_organisation=self.test_bus_organisation, number_plate='KBC 243J', route=self.test_route, capacity=34 )

        self.test_bus.save()

        # Create instance of Schedule class
        departure_date = date(2018, 10, 19)

        arrival_date = date(2018, 10, 19)

        departure_time_input = time(10, 45, 00, 000000 ,tzinfo=timezone.get_current_timezone())

        arrival_time_input = time( 19, 00, 00, 231245 ,tzinfo=timezone.get_current_timezone())

        departure_datetime = datetime.combine(departure_date, departure_time_input )

        arrival_datetime = datetime.combine(arrival_date, arrival_time_input )

        self.new_schedule = Schedule(departure_time=departure_datetime, arrival_time=arrival_datetime, bus=self.test_bus, price=500.00)

    def test_instance(self):
        '''
        Test case to check if self.new_schedule in an instance of Schedule class
        '''
        self.assertTrue( isinstance(self.new_schedule, Schedule) )

    def test_get_schedules(self):
        '''
        Test to check if all schedules are gotten from the database
        '''
        self.new_schedule.save()

        another_departure_date = date(2018, 11, 19)

        another_arrival_date = date(2018, 11, 19)

        another_departure_time_input = time( 9, 45, 00, 786956 ,tzinfo=timezone.get_current_timezone())

        another_arrival_time_input = time(18, 00, 00, 876578, tzinfo=timezone.get_current_timezone())

        another_departure_datetime = datetime.combine(another_departure_date, another_departure_time_input )

        another_arrival_datetime = datetime.combine(another_arrival_date, another_arrival_time_input )

        self.test_schedule = Schedule(departure_time=another_departure_datetime, arrival_time=another_arrival_datetime, bus=self.test_bus, price=450.00)

        self.test_schedule.save()

        gotten_schedules = Schedule.get_schedules()

        schedules = Schedule.objects.all()

        self.assertTrue( len(gotten_schedules) == len(schedules) )

    def test_get_single_schedule(self):
        '''
        Test to check if the specified schedule is gotten from the database
        '''
        self.new_schedule.save()

        another_departure_date = date(2018, 11, 19)

        another_arrival_date = date(2018, 11, 19)

        another_departure_time_input = time(9, 45, 00, 786956 ,tzinfo=timezone.get_current_timezone())

        another_arrival_time_input = time(18, 00, 00, 876578, tzinfo=timezone.get_current_timezone())

        another_departure_datetime = datetime.combine(another_departure_date, another_departure_time_input )

        another_arrival_datetime = datetime.combine(another_arrival_date, another_arrival_time_input )

        self.test_schedule = Schedule(departure_time=another_departure_datetime, arrival_time=another_arrival_datetime, bus=self.test_bus, price=450.00)

        self.test_schedule.save()

        gotten_schedule = Schedule.get_single_schedule(self.new_schedule.id)

        # schedules = Schedule.objects.all()
        
        self.assertTrue( isinstance(gotten_schedule, Schedule))

    def test_get_bus_schedules(self):
        '''
        Test to check if all the schedules for the specified bus are gotten from the database
        '''
        self.new_schedule.save()

        self.another_bus = Bus(bus_organisation=self.test_bus_organisation, number_plate='KCA 907L', route=self.test_route, capacity=44 )

        self.another_bus.save()

        another_departure_date = date(2018, 11, 19)

        another_arrival_date = date(2018, 11, 19)

        another_departure_time_input = time(9, 45, 00, 786956 ,tzinfo=timezone.get_current_timezone())

        another_arrival_time_input = time(18, 00, 00, 876578, tzinfo=timezone.get_current_timezone())

        another_departure_datetime = datetime.combine(another_departure_date, another_departure_time_input )

        another_arrival_datetime = datetime.combine(another_arrival_date, another_arrival_time_input )

        self.test_schedule = Schedule(departure_time=another_departure_datetime, arrival_time=another_arrival_datetime, bus=self.test_bus, price=450.00)

        self.test_schedule.save()

        different_departure_date = date(2018, 9, 19)

        different_arrival_date = date(2018, 9, 19)

        different_departure_time_input = time(11, 45, 00, 127325, tzinfo=timezone.get_current_timezone())

        different_arrival_time_input = time(18, 00 , 00, 423063, tzinfo=timezone.get_current_timezone())

        different_departure_datetime = datetime.combine(different_departure_date, different_departure_time_input )

        different_arrival_datetime = datetime.combine(different_arrival_date, different_arrival_time_input )

        self.test_schedule2 = Schedule(departure_time=different_departure_datetime, arrival_time=different_arrival_datetime, bus=self.another_bus, price=480.00)

        self.test_schedule2.save()

        gotten_schedules = Schedule.get_bus_schedules(self.test_bus.id)

        schedules = Schedule.objects.all()
        
        self.assertTrue( len(gotten_schedules) != len(schedules))

    def test_get_travel_estimation(self):
        '''
        Test case to check if the travel estimation for the specific schedule is calculated
        '''
        self.new_schedule.save()

        another_departure_date = date(2018, 11, 19)

        another_arrival_date = date(2018, 11, 19)

        another_departure_time_input = time(9, 45, 00, 786956, tzinfo=timezone.get_current_timezone())

        another_arrival_time_input = time(18, 00, 00, 876578, tzinfo=timezone.get_current_timezone())

        another_departure_datetime = datetime.combine(another_departure_date, another_departure_time_input )

        another_arrival_datetime = datetime.combine(another_arrival_date, another_arrival_time_input )

        self.test_schedule = Schedule(departure_time=another_departure_datetime, arrival_time=another_arrival_datetime, bus=self.test_bus, price=450.00)

        self.test_schedule.save()

        calculate_travel_estimation = self.test_schedule.arrival_time - self.test_schedule.departure_time

        travel_estimation = str(calculate_travel_estimation.seconds//3600) + ' hours ' + str(calculate_travel_estimation.seconds//60 % 60) + ' minutes'

        gotten_travel_estimation = Schedule.get_travel_estimation(self.test_schedule.id)
        
        self.assertTrue( gotten_travel_estimation == travel_estimation )

    def test_get_departure_buses(self):
        '''
        Test case to check if schedules with the specific departure date are gotten from the database
        '''
        self.new_schedule.save()

        # Create instance of Bus class
        self.another_bus = Bus(bus_organisation=self.test_bus_organisation, number_plate='KCA 907L', route=self.test_route, capacity=44 )

        self.another_bus.save()

        # Create instance of Route class
        self.another_route = Route(departure_location='Nairobi', destination_location='Mombasa')

        self.another_route.save()

        # Create another instance of Bus class
        self.diffent_bus = Bus(bus_organisation=self.test_bus_organisation, number_plate='KCA 907L', route=self.another_route, capacity=44 )

        self.diffent_bus.save()

        # Create new departure and arrival date
        another_departure_date = date(2018, 11, 19)

        another_arrival_date = date(2018, 11, 19)

        another_departure_time_input = time(9, 45, 00, 786956, tzinfo=timezone.get_current_timezone())

        another_arrival_time_input = time(18, 00, 00, 876578, tzinfo=timezone.get_current_timezone())

        another_departure_datetime = datetime.combine(another_departure_date, another_departure_time_input )

        another_arrival_datetime = datetime.combine(another_arrival_date, another_arrival_time_input )

        # Create new schedule
        self.test_schedule = Schedule(departure_time=another_departure_datetime, arrival_time=another_arrival_datetime, bus=self.test_bus, price=450.00)

        self.test_schedule.save()

        # Create another schedule
        self.test_schedule2 = Schedule(departure_time=another_departure_datetime, arrival_time=another_arrival_datetime, bus=self.another_bus, price=480.00)

        self.test_schedule2.save()

        # Create another departure and arrival date
        different_departure_date = date(2018, 11, 19)

        different_arrival_date = date(2018, 11, 19)

        different_departure_time_input = time(23, 59, 59, 127325, tzinfo=timezone.get_current_timezone())

        different_arrival_time_input = time(16, 45 , 00, 423063, tzinfo=timezone.get_current_timezone())

        different_departure_datetime = datetime.combine(different_departure_date, different_departure_time_input )

        different_arrival_datetime = datetime.combine(different_arrival_date, different_arrival_time_input )

        # Create another schedule
        self.test_schedule3 = Schedule(departure_time=different_departure_datetime, arrival_time=different_arrival_datetime, bus=self.diffent_bus, price=425.00)

        self.test_schedule3.save()

        gotten_departure_buses = Schedule.get_departure_buses(another_departure_date, self.test_route.id)

        schedules = Schedule.objects.all()
        
        self.assertTrue( len(gotten_departure_buses) != len(schedules) )










