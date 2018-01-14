from django.test import TestCase
from .models import BusOrganisation

# Create your tests here.
class BusOrganisationeTestClass(TestCase):
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

        test_bus_organisation = BusOrganisation(name="Anothe Bus Ltd")

        test_bus_organisation.save()

        gotten_buses = BusOrganisation.get_bus_organisations()

        bus_organisations = BusOrganisation.objects.all()

        self.assertTrue( len(gotten_buses) == len(bus_organisations) )

    def test_get_single_bus_organisation(self):
        '''
        Test to check if the specified bus organisation is gotten from the database
        '''
        self.new_bus_organisation.save()

        test_bus_organisation = BusOrganisation(name="Another Bus Ltd")

        test_bus_organisation.save()

        gotten_bus = BusOrganisation.get_single_bus_organisation(self.new_bus_organisation.id)

        # bus_organisations = BusOrganisation.objects.all()
        
        self.assertTrue( isinstance(gotten_bus, BusOrganisation))





