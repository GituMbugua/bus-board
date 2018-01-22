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
  
  # first_name = forms.CharField(max_length = 255)

  # last_name = forms.CharField(max_length = 255)
  
  # email = forms.EmailField(max_length = 254)

  # phone_number = forms.CharField(max_length = 255)

  # transaction_code = forms.CharField(max_length = 255)

  # def clean_phone_number(self):
  #   '''
  #   Function for validating phone number
  #   '''
  #   print(self['phone_number'])

  #   phone_number = self.cleaned_data['phone_number']

  #   add_country_code = '+254' + phone_number

  #   string_to_phonenumber = phonenumbers.parse(add_country_code, "KE")

  #   check_valid_number = phonenumbers.is_possible_number(string_to_phonenumber)

  #   if check_valid_number == False:

  #     print('Invalid number')
      
  #     raise forms.ValidationError("Please enter a valid number")

  #   return phone_number




