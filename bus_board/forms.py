from django import forms
# from django.contrib.auth.forms import AuthenticationForm
from .models import Ticket
import phonenumbers

class TicketForm(forms.ModelForm):
  '''
  Class to create a form for a user to get a ticket
  '''
  class Meta:
    model = Ticket
    fields = ('first_name', 'last_name', 'email', 'phone_number', 'transaction_code')


  def clean_phone_number(self):
    '''
    Function for validating phone number
    '''

    phone_number = self.cleaned_data.get('phone_number')

    add_country_code = '+254' + phone_number

    string_to_phonenumber = phonenumbers.parse(add_country_code, "KE")

    check_valid_number = phonenumbers.is_possible_number(string_to_phonenumber)

    if check_valid_number != True:
      
      raise forms.ValidationError("Please enter a valid number")

    return phone_number




