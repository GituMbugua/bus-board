# Bus Board

## By **[Gitu Mbugua](https://github.com/GituMbugua)**, **[John Mutavi](https://github.com/jonnygovish)** and **[Carol Wanjohi](https://github.com/carolwanjohi)**

## Description
[This](https://bus-board.herokuapp.com/) is a web application that allows users to search for buses by entering their starting point and destination. The results list has buses arranged with the cheapest bus at the top of the list. The user can select a bus and book a seat in the bus.

## User Stories
As a user I would like to:
* search for a bus by entering the departure location and arrival location
* select a bus
* see information on the selected bus
* pay for the selected bus and get a ticket

## Specifications
| Behavior        | Input           | Outcome  |
| ------------- |:-------------:| -----:|
| Search for a bus | Departure location: Nakuru <br> <br> Arrival Location: Nairobi <br> <br> Travel Date: 02/02/2018 | Display list of buses found |
| Select a bus | Click **select** button | Display information about the selected bus and a form for user to input their information |
| Get a ticket | Click **confirm and book** | Display pdf with ticket information |

## Setup/Installation Requirements

### Prerequisites
* Python 3.6.2
* Virtual environment
* Postgres Database
* Internet

### Installation Process
1. Copy repolink
2. Run `git clone REPO-URL` in your terminal
3. Write `cd bus-board`
4. Create a virtual environment with `virtualenv virtual` or try `python3.6 -m venv virtual`
5. Create .env file `touch .env` and add the following:
```
SECRET_KEY=<your secret key>
DEBUG=True
```
6. Enter your virtual environment `source virtual/bin/activate`
7. Run `pip install -r requirements.txt` or `pip3 install -r requirements.txt`
8. Create Postgres Database

```
psql
CREATE DATABASE bus-board
```
9. Change the database informatioin in `/settings.py` 
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bus-board',
        'USER': *POSTGRES_USERNAME*,
        'PASSWORD': *POSTGRES_USERNAME*,
    }
}
``` 
10. Run `./manage.py runserver` or `python3.6 manage.py runserver` to run the application

### Africas Talking API
1. Visit [this](https://account.africastalking.com/auth/register) site and register a new account or log into your Africas Talking account
2. Click **Go to Sandbox App** button
3. Click **Settings** on the side bar menu and click **API Key**
4. Enter **your password** in the form field
5. Copy the generated **API KEY** 
6. Go to the `.env` file and paste the api key
```
API_KEY_AFRICAS_TALKING = <your api key>
```

## Known Bugs

* open ticket pdf after callback url is sent back

## Technologies Used
- Python 3.6.2
- Django 1.11.7
- Bootstrap 3
- Postgres Database
- CSS
- HTML
- Heroku
- xhtml2pdf
- Africas Talking API

### License

MIT (c) 2017 **[Gitu Mbugua](https://github.com/GituMbugua)**, **[John Mutavi](https://github.com/jonnygovish)** and **[Carol Wanjohi](https://github.com/carolwanjohi)**





