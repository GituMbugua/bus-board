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

        # Get the input arrival location
        search_arrival_location = request.GET.get('arrival-location')

        # Get the input date
        travel_date = request.GET.get('travel-date')

        # Convert string input to date type
        convert_to_date = datetime.strptime(travel_date, '%Y-%m-%d').date()

        # Get the route 
        result_route = Route.get_search_route(search_departure_location,search_arrival_location)

        # Check if route exists found
        if result_route != None :
            print(result_route.id)

            # Schedule with the same depature date
            schedule_with_depature_date = Schedule.get_departure_buses(convert_to_date, result_route.id)

            if len(schedule_with_depature_date) > 0:

                print(schedule_with_depature_date)

            else:

                print('No schedule buses')

        # Otherwise
        else:
            print('Not route found')

    title = 'Result'

    return render(request, 'search.html', {'title':title, 'result_route':result_route})
