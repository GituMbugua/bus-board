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

    title = 'Result'

    if ('depature-location' in request.GET and request.GET['depature-location']) and ('arrival-location' in request.GET and request.GET['arrival-location']) and ('travel-date' in request.GET and request.GET['travel-date']):

        # Get the input departure
        search_departure_location = request.GET.get('depature-location').title()

        # Get the input arrival location
        search_arrival_location = request.GET.get('arrival-location').title()

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

                for schedule in schedule_with_depature_date:

                    estimation_duration = Schedule.get_travel_estimation(schedule.id)

                return render(request, 'search.html', {'title':title, 'search_departure_location':search_departure_location, 'search_arrival_location':search_arrival_location, 'convert_to_date':convert_to_date, 'buses':schedule_with_depature_date, 'estimation_duration':estimation_duration})

            else:
                no_scheduled_bus_message = 'No scheduled buses'

                return render(request, 'search.html', {'title':title, 'no_scheduled_bus_message':no_scheduled_bus_message, 'search_departure_location':search_departure_location, 'search_arrival_location':search_arrival_location, 'convert_to_date':convert_to_date})

        # Otherwise
        else:
            
            no_route_message = 'Bus route not found'

            return render(request, 'search.html', {'title':title, 'no_route_message':no_route_message, 'search_departure_location':search_departure_location, 'search_arrival_location':search_arrival_location, 'convert_to_date':convert_to_date})

