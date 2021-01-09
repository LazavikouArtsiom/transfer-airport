from django import forms
from .models import Booking

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields= '__all__'
        widgets = {'order_date':DateInput(),
                   'back_date':DateInput(),
                   'notes':forms.Textarea(),
                   
                   }
