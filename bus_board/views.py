from django.shortcuts import render, redirect
from .models import BusOrganisation, Route, Bus, Schedule
from datetime import datetime, date

def home(request):
    '''
    view function for landing page
    '''
    return render(request, 'home.html')

def search_results(request):
    '''
    View function to get the the requested departure and arrival locations from the database and display to the user
    '''
    if ('depature-location' in request.GET and request.GET['depature-location']) and ('arrival-location' in request.GET and request.GET['arrival-location']) and ('travel-date' in request.GET and request.GET['travel-date']):

        # Get the input departure
        search_departure_location = request.GET.get('depature-location')
        # print('Searched departure location:')
        # print(search_departure_location)
        # print('<><><><><><><>')

        # Get the input arrival location
        search_arrival_location = request.GET.get('arrival-location')
        # print('Searched arrival location:')
        # print(search_arrival_location)
        # print('<><><><><><><>')

        # Get the input date
        travel_date = request.GET.get('travel-date')

        # Convert string input to date type
        convert_to_date = datetime.strptime(travel_date, '%Y-%m-%d').date()
        # print('Searched date:')
        # print(travel_date)
        # print('<><><><><><><>')

        # Get the route 
        result_route = Route.get_search_route(search_departure_location,search_arrival_location)

        # Schedule with the same depature date
        schedule_with_depature_date = Schedule.get_departure_buses(convert_to_date)

        # Check if route and schedule is found
        if result_route != None and len(schedule_with_depature_date) != 0 :

            # Buses on the route
            route_buses = Bus.get_route_buses(result_route.id)

            print(schedule_with_depature_date)

        # Otherwise
        else:
            print('Not route found')

    return render(request, 'search.html')
