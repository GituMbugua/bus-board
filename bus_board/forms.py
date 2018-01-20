from django import forms
# from django.contrib.auth.forms import AuthenticationForm
from .models import Ticket

class TicketForm(forms.ModelForm):
  '''
  Class to create a form for a user to get a ticket
  '''
  class Meta:
    model = Ticket
    fields = ('first_name', 'last_name', 'email', 'phone_number', 'transaction_code')

