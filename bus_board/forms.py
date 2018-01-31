from django import forms
# from django.contrib.auth.forms import AuthenticationForm
from .models import Ticket
import phonenumbers

class TicketForm(forms.ModelForm):
  '''
  Class to create a form for a user to get a ticket
  '''
  # phone_number = forms.CharField(max_length = 255)

  class Meta:
    model = Ticket

    fields = ('first_name', 'last_name', 'email', 'phone_number')

  def clean(self):
    
    cleaned_data = super(TicketForm, self).clean()

    gotten_phone_number = cleaned_data.get('phone_number')

    # Check if phone number begins with the Kenyan country code
    if gotten_phone_number[:4] == '+254':
    
        # print('country code detected')

        # Convert string to phone number
        string_to_phonenumber = phonenumbers.parse(gotten_phone_number, "KE")

        print(len(gotten_phone_number))

        # Check if the phonenumber is not a valid Kenyan number
        if phonenumbers.is_possible_number(string_to_phonenumber) != True or len(gotten_phone_number) != 13:
          
            # print('Not a valid Kenyan number')
            raise forms.ValidationError('The phone number is not a valid Kenyan phone number')
    
    # Check if the number begins with a 0
    elif gotten_phone_number[:2] == '07':
    
        # print('number without country code')
        
        # Phone number string without 0
        without_zero = gotten_phone_number[1:]
        
        # Add Kenyan country code to the beginning
        add_country_code = '+254' + without_zero

        # Convert string to phone number
        string_to_phonenumber = phonenumbers.parse(add_country_code, "KE")

        # Check if the phonenumber is not a valid Kenyan number
        if phonenumbers.is_possible_number(string_to_phonenumber) != True or len(add_country_code) != 13:
            
            # print('Not a valid Kenyan number')
            raise forms.ValidationError('The phone number is not a valid Kenyan phone number')

    # Otherwise
    else:
      
        # print('number with non-Kenyan country code')
        raise forms.ValidationError('The phone number is not a valid Kenyan phone number')

    return cleaned_data
        
  
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




